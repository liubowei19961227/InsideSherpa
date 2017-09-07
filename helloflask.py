from flask import Flask
from flask import render_template
from flask import request
from werkzeug import secure_filename
import os


app = Flask(__name__,static_url_path = '/static')

file_record = {}




@app.route("/")
def index():
  return render_template('try1.html')




@app.route("/upload_file",methods=['POST'])
def play_music():
	return render_template('upload2.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		if f.filename in file_record:
			return 'duplicated name found'
		file_record[f.filename] = 1
		


		APP_ROOT = os.path.dirname(os.path.abspath(__file__))
		UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads')
		app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
		filename = secure_filename(f.filename)
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		
		return 'file uploaded successfully'




'''@app.route("/download_music",methods=['POST'])
def dowload_music():
	return "download music"'''


'''@app.route("/read_input", methods=['POST'])
def login():
	return request.form['username']'''

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=9393)