from flask import Flask, render_template, request, redirect, url_for, g, send_from_directory, session
from PIL import Image
import io
import os
import reader

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/api/upload-image', methods=['POST'])
def upload():
    uploaded_file = request.files['photo']
    title = request.form['title']
    caption = request.form['caption']
    username = request.form['username_input']

    folder = 'static'
    file_path = os.path.join(folder, uploaded_file.filename)
    uploaded_file.save(file_path)
    filename = uploaded_file.filename

    # Process and encode the image
    img = Image.open(file_path)
    img_data = io.BytesIO()
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img.save(img_data, 'JPEG',)
    
    #! complete saving function

    return redirect(url_for('index'))