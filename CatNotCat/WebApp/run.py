import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)

import helper
import CatORNot as predictor

from PIL import Image


#Flask
from flask import Flask, render_template, json, jsonify, request,redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

## Config 
size = 64


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in helper.get_allowed_ext()


def getStats():
    OldStats = old_stats.OldStats()
    return OldStats.getStats()

@app.route("/")
def main():
    return render_template('home.html')


@app.route("/app")
def stats():
    return render_template('app.html')


@app.route("/v1/upload",methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            img = Image.open(file.stream)
            result = predictor.get_predction(img)
            return jsonify(results={'isCat':result})



if __name__ == "__main__":
    app.run()

