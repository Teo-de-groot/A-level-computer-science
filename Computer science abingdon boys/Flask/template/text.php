<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST, GET");
header("Access-Control-Allow-Headers: Content-Type");
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Save & Read File</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        input, textarea, button { margin: 6px 0; width: 100%; }
        textarea { height: 200px; }
        #fileContent {
            white-space: pre-wrap;
            border: 1px solid #ccc;
            padding: 10px;
            margin-top: 10px;
            height: 200px;
        }
    </style>
</head>
<body>

<h1>Save a File</h1>

<input type="text" id="saveFilename" placeholder="Enter filename (example.txt)">
<textarea id="fileText" placeholder="Write your content here..."></textarea>
<button id="saveButton">Save</button>

<p id="uploadStatus"></p>

<hr>

<h1>Read a File</h1>

<input type="text" id="readFilename" placeholder="Enter filename to read">
<button id="readButton">Read File</button>

<div id="fileContent"></div>

<script>
const saveButton = document.getElementById('saveButton');
const saveFilename = document.getElementById('saveFilename');
const fileText = document.getElementById('fileText');
const uploadStatus = document.getElementById('uploadStatus');

const readButton = document.getElementById('readButton');
const readFilename = document.getElementById('readFilename');
const fileContent = document.getElementById('fileContent');

const phpEndpoint = 'file_handler.php';

/* SAVE FILE */
saveButton.addEventListener('click', async () => {
    const filename = saveFilename.value.trim();
    const content = fileText.value;

    if (!filename) {
        uploadStatus.textContent = 'Please enter a filename.';
        return;
    }

    try {
        const response = await fetch(phpEndpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ filename, content })
        });

        const result = await response.json();
        uploadStatus.textContent = result.message;
    } catch {
        uploadStatus.textContent = 'Error saving file.';
    }
});

/* READ FILE */
readButton.addEventListener('click', async () => {
    const filename = readFilename.value.trim();
    if (!filename) {
        fileContent.textContent = 'Please enter a filename.';
        return;
    }

    try {
        const response = await fetch(`${phpEndpoint}?filename=${encodeURIComponent(filename)}`);
        if (!response.ok) {
            const error = await response.json();
            fileContent.textContent = error.message;
            return;
        }
        const text = await response.text();
        fileContent.textContent = text;
    } catch {
        fileContent.textContent = 'Error reading file.';
    }
});
</script>

</body>
</html>
