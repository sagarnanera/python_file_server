# Flask File Manager

## Overview

This repository contains a simple Flask web application for managing files. It enables users to upload and download files, supporting a folder structure within the `data` directory.

## Features

- Upload multiple files simultaneously.
- Download files and folders.
- View the list of files and folders in the `data` directory.
- Supports subdirectories within the `data` directory.

## Prerequisites

- Python 3.x installed on your machine.
- Flask library installed. Install using:

  ```bash
  pip install Flask
  ```

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/flask-file-manager.git
   cd python_file_server
   ```

2. **Run the Flask application:**

   ```bash
   python app.py
   ```

3. **Open your browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access the file manager.**

## Usage

- **Upload Files:**
  - Click the "Upload" button.
  - Select one or more files to upload.

- **Download Files:**
  - Click on a file or folder link to download.

- **Folder Structure:**
  - Subdirectories within the `data` directory are supported.

- **Server IP Address:**
  - The IP address of the server will be displayed in the terminal when the application is started.

## Advanced Configuration

- Adjust the `DATA_FOLDER` variable in `app.py` to change the root directory for file storage.

## Notes

- This application does not support uploading entire folders due to browser security restrictions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
