<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST, GET");
header("Access-Control-Allow-Headers: Content-Type");


$uploadDir = "uploads/";

if (!is_dir($uploadDir)) {
    mkdir($uploadDir, 0777, true);
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_FILES['file'])) {
        $fileName = basename($_FILES['file']['name']);
        $targetFile = $uploadDir . $fileName;

        if (move_uploaded_file($_FILES['file']['tmp_name'], $targetFile)) {
            echo json_encode(["status" => "success", "message" => "File uploaded", "file" => $targetFile]);
        } else {
            echo json_encode(["status" => "error", "message" => "Failed to upload file"]);
        }
    } else {
        echo json_encode(["status" => "error", "message" => "No file provided"]);
    }
}

if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['filename'])) {
    $fileName = basename($_GET['filename']);
    $filePath = $uploadDir . $fileName;

    if (file_exists($filePath)) {

        header('Content-Type: text/plain');
        readfile($filePath);
    } else {
        http_response_code(404);
        echo json_encode(["status" => "error", "message" => "File not found"]);
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>File Upload & Read</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        input, button { margin: 5px 0; }
        #fileContent { white-space: pre-wrap; border: 1px solid #ccc; padding: 10px; margin-top: 10px; width: 100%; height: 200px; }
    </style>
</head>
<body>
    <h1>Upload a File</h1>
    <form id="uploadForm">
        <input type="file" name="file" id="fileInput" required>
        <button type="submit">Upload</button>
    </form>
    <p id="uploadStatus"></p>

    <h1>Read a File</h1>
    <input type="text" id="readFilename" placeholder="Enter filename to read">
    <button id="readButton">Read File</button>
    <div id="fileContent"></div>

    <script>
        const uploadForm = document.getElementById('uploadForm');
        const fileInput = document.getElementById('fileInput');
        const uploadStatus = document.getElementById('uploadStatus');
        const readButton = document.getElementById('readButton');
        const readFilename = document.getElementById('readFilename');
        const fileContent = document.getElementById('fileContent');

        const phpEndpoint = 'file_handler.php'; 
        uploadForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData();
            formData.append('file', fileInput.files[0]);

            try {
                const response = await fetch(phpEndpoint, {
                    method: 'POST',
                    body: formData
                });
                const result = await response.json();
                uploadStatus.textContent = result.message;
            } catch (err) {
                uploadStatus.textContent = 'Error uploading file.';
            }
        });


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
            } catch (err) {
                fileContent.textContent = 'Error reading file.';
            }
        });
    </script>
</body>
</html>
