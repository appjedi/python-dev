from flask import Flask, render_template, url_for
import MySQLdb
app = Flask(__name__)

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


@app.route("/about")
def about():
    return render_template('about.html', title='About')

def getConn():
#db = MySQLdb.connect(host="localhost",user="root",password="maria1",database="test")
    db = MySQLdb.connect(host="127.0.0.1", user="root",
                     password="Jedi2023", database="dev")
    return db
if __name__ == '__main__':
    app.run(debug=True)
