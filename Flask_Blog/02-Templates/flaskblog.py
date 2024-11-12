import os
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/Users/roberttimlin/Documents/GitHub/python-dev/Flask_Blog/02-Templates/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
#import MySQLdb
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route("/upload2")
def uploadForm():
    return render_template('upload.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

def getConn():
    print ("getConn() called")
#db = MySQLdb.connect(host="localhost",user="root",password="maria1",database="test")
    #db = MySQLdb.connect(host="127.0.0.1", user="root",password="Jedi2023", database="dev")
    return None
if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5001
    )
