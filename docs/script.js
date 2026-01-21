const fileInput = document.getElementById("file-input");

fileInput.addEventListener("change", () => {
    const file = fileInput.files[0];
    if (file) uploadFile(file);
});

function uploadFile(file) {
    document.getElementById("loading").classList.remove("hidden");
    document.getElementById("results").classList.add("hidden");

    const formData = new FormData();
    formData.append("file", file);

    fetch("https://ai-meeting-summariser-c5tv.onrender.com/upload", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("loading").classList.add("hidden");

        document.getElementById("results").classList.remove("hidden");

        document.getElementById("transcript").innerText = data.transcript || "Not available";
        document.getElementById("summary").innerText = data.summary || "Not available";

        let kwBox = document.getElementById("keywords");
        kwBox.innerHTML = "";
        (data.keywords || []).forEach(k => {
            let li = document.createElement("li");
            li.innerText = k;
            kwBox.appendChild(li);
        });

        if (data.sentiment) {
            document.getElementById("sentiment").innerText =
                data.sentiment.overall || data.sentiment.label || "Unknown";

            document.getElementById("sentiment-reason").innerText =
                data.sentiment.reason || "";
        }
    })
    .catch(err => {
        document.getElementById("loading").innerText = "Error. Try Again.";
        console.error(err);
    });
}
