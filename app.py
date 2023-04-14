import ast
from os import name
from flask import Flask, redirect, render_template, request, url_for

from detect import detect_objects

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    file = request.files['file']
    image_path = 'temp.jpg'
    file.save(image_path)
    predictions, class_names = detect_objects(image_path)
    if not predictions:
        return redirect(url_for('no_detections'))
    else:
        return redirect(url_for('results', predictions=predictions, class_names=class_names))

@app.route('/results')
def results():
    # Get the prediction results from the URL parameter
    predictions = request.args.getlist('predictions')
    class_names = request.args.getlist('class_names')

    # Render the results page with the prediction results and class names
    return render_template('results.html', predictions=predictions, class_names=class_names)

@app.route('/no_detections')
def no_detections():
    return render_template('no_detections.html')


if name == 'main':
    app.run(debug=True)
