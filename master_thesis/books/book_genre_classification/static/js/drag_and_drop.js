document.addEventListener("DOMContentLoaded", function () {
    const dropZone = document.getElementById("drop-zone");
    const fileInput = document.getElementById("file-input");
    const submitBtn = document.getElementById("submit-btn");
    const upP = document.querySelector(".up-p");

    dropZone.addEventListener("click", function () {
        fileInput.click();
    });

    fileInput.addEventListener("change", function () {
        if (fileInput.files.length > 0) {
            upP.textContent = `${fileInput.files[0].name} selected`;
            submitBtn.disabled = false;
        } else {
            upP.textContent = "Drag your book file here or click in this area.";
            submitBtn.disabled = true;
        }
    });

    dropZone.addEventListener("dragover", function (event) {
        event.preventDefault();
        dropZone.classList.add("dragover");
    });

    dropZone.addEventListener("dragleave", function () {
        dropZone.classList.remove("dragover");
    });

    dropZone.addEventListener("drop", function (event) {
        event.preventDefault();
        dropZone.classList.remove("dragover");

        if (event.dataTransfer.files.length > 0) {
            fileInput.files = event.dataTransfer.files;
            upP.textContent = `${fileInput.files[0].name} selected`;
            submitBtn.disabled = false;
        }
    });
});




// // Drag-and-Drop functionality
// document.addEventListener("DOMContentLoaded", () => {
//     const dropZone = document.getElementById("drop-zone");
//     const fileInput = document.getElementById("file-input");
//     const upP = document.querySelector(".up-p");

//     // Highlight the drop zone when a file is dragged over it
//     dropZone.addEventListener("dragover", (e) => {
//         e.preventDefault();
//         dropZone.classList.add("drag-over");
//     });

//     dropZone.addEventListener("dragleave", () => {
//         dropZone.classList.remove("drag-over");
//     });

//     // Handle file drop
//     dropZone.addEventListener("drop", (e) => {
//         e.preventDefault();
//         dropZone.classList.remove("drag-over");

//         const files = e.dataTransfer.files;
//         if (files.length > 0) {
//             fileInput.files = files;
//             upP.textContent = `${files.length} file(s) selected`;
//         }
//     });

//     // Trigger file input when the drop zone is clicked
//     dropZone.addEventListener("click", () => {
//         fileInput.click();
//     });

//     // Update label when file input changes
//     fileInput.addEventListener("change", () => {
//         upP.textContent = `${fileInput.files.length} file(s) selected`;
//     });
// });
