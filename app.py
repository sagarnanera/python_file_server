from flask import Flask, render_template, request, send_from_directory, redirect
import os

app = Flask(__name__)

DATA_FOLDER = 'data'

app.config['DATA_FOLDER'] = DATA_FOLDER

@app.route('/')
def index():
    files = os.listdir(app.config['DATA_FOLDER'])
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'files' not in request.files:
        return 'No file part'

    files = request.files.getlist('files')

    for file in files:
        if file.filename == '':
            return 'No selected file'

        file.save(os.path.join(app.config['DATA_FOLDER'], file.filename))

    return redirect('/')

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['DATA_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)