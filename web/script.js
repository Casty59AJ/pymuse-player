let dl_count = 0;

// a function to update download button count and label
function download_btn_Click(event) {
    dl_count = dl_count + 1;
    
    // update text content of the label
    let dl_Label = document.getElementById("dl_Label");
    dl_Label.innerText = "Times downloaded: " + dl_count;

    // update text inside the span element
    let dlSpan = document.querySelector("div > div > span");
    if (dlSpan) {
        dlSpan.innerText = "Times downloaded: " + dl_count;
    }
}

// Attach the click event listener to the download button
document.addEventListener("DOMContentLoaded", function() {
    let downloadButton = document.querySelector("a[href='download.html']"); // select download button
    if (downloadButton) {
        downloadButton.addEventListener("click", download_btn_Click);
    }
});
