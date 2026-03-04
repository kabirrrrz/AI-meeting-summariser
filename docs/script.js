// const fileInput = document.getElementById("file-input");

// fileInput.addEventListener("change", () => {
//     const file = fileInput.files[0];
//     if (file) uploadFile(file);
// });

// function uploadFile(file) {
//     console.log("UPLOAD STARTED"); // DEBUG

//     document.getElementById("loading").classList.remove("hidden");
//     document.getElementById("results").classList.add("hidden");

//     const formData = new FormData();
//     formData.append("file", file);

//     // ✅ LOCAL BACKEND
//     fetch("http://127.0.0.1:5000/upload", {
//         method: "POST",
//         body: formData
//     })
//     .then(res => {
//         console.log("SERVER RESPONSE STATUS:", res.status);
//         return res.json();
//     })
//     .then(data => {
//         console.log("SERVER DATA:", data);

//         document.getElementById("loading").classList.add("hidden");
//         document.getElementById("results").classList.remove("hidden");

//         document.getElementById("transcript").innerText =
//             data.transcript || "Not available";

//         document.getElementById("summary").innerText =
//             data.summary || "Not available";

//         let kwBox = document.getElementById("keywords");
//         kwBox.innerHTML = "";

//         (data.keywords || []).forEach(k => {
//             let li = document.createElement("li");
//             li.innerText = k;
//             kwBox.appendChild(li);
//         });

//         if (data.sentiment) {
//             document.getElementById("sentiment").innerText =
//                 data.sentiment.overall ||
//                 data.sentiment.label ||
//                 "Unknown";

//             document.getElementById("sentiment-reason").innerText =
//                 data.sentiment.reason || "";
//         }
//     })
//     .catch(err => {
//         console.error("FETCH FAILED:", err);

//         document.getElementById("loading").innerText =
//             "Error. Try Again.";
//     });
// }

const fileInput = document.getElementById("file-input");

fileInput.addEventListener("change", () => {
    const file = fileInput.files[0];
    if (file) {
        uploadFile(file);
    }
});

function uploadFile(file) {

    console.log("UPLOAD STARTED");

    const loading = document.getElementById("loading");
    const results = document.getElementById("results");

    loading.classList.remove("hidden");
    results.classList.add("hidden");

    const formData = new FormData();
    formData.append("file", file);

    fetch("https://ai-meeting-summariser-1.onrender.com/upload", {
        method: "POST",
        body: formData
    })
    .then(res => {
        console.log("SERVER STATUS:", res.status);

        if (!res.ok) {
            throw new Error("Server returned error");
        }

        return res.json();
    })
    .then(data => {

        console.log("SERVER DATA:", data);

        loading.classList.add("hidden");
        results.classList.remove("hidden");

        document.getElementById("transcript").innerText =
            data.transcript || "Transcript not available";

        document.getElementById("summary").innerText =
            data.summary || "Summary not available";

        const kwBox = document.getElementById("keywords");
        kwBox.innerHTML = "";

        if (data.keywords) {
            data.keywords.forEach(k => {
                const li = document.createElement("li");
                li.innerText = k;
                kwBox.appendChild(li);
            });
        }

        if (data.sentiment) {

            document.getElementById("sentiment").innerText =
                data.sentiment.overall ||
                data.sentiment.label ||
                "Unknown";

            document.getElementById("sentiment-reason").innerText =
                data.sentiment.reason || "";
        }

    })
    .catch(err => {

        console.error("FETCH FAILED:", err);

        loading.classList.remove("hidden");
        loading.innerText = "Error processing file. Please try again.";

        results.classList.add("hidden");

    });
}