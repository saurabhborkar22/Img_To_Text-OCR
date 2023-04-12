from flask import Flask, render_template, request
import pytesseract
import cv2
import numpy as np

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    text = pytesseract.image_to_string(img)
    return render_template('result.html', text=text)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
