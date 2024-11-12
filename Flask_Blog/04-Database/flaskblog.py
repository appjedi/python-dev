from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
import pymysql

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
with open(".env", 'r') as file:
    env_data = file.read()
envValues=env_data.split("\n")
ENV_KEY_VALUES={}
for row in envValues:
    keyValue=row.split("=")
    ENV_KEY_VALUES[keyValue[0]]=keyValue[1]
print (ENV_KEY_VALUES)

db_conn_arr = ENV_KEY_VALUES['PROD_DB'].split("~")
print("db_conn_str:",db_conn_arr)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print ("login:", form.email.data, form.password.data)
    if form.validate_on_submit():
        user=login(form.email.data,form.password.data)
        if user==None:
            flash('Login Unsuccessful. Please check username and password', 'danger')

        else:
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))

    return render_template('login.html', title='Login', form=form)

def login (username, password):
    conn = mysqlconnect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    row = cur.fetchone()
    print("fetch row:",row)
    user = {'id': row[0], 'username': row[1], 'roleId': row[3], 'status': row[4]}
    print ("user:", user)

    # To close the connection
    conn.close()
    return user
@app.route("/api/users", methods=['GET'])
def listUsers():
    conn =mysqlconnect()
    cur = conn.cursor()
    cur.execute("select * from users")
    users = cur.fetchall()
    print ("users:",users)
    userList=[]
    for user in users:
        userList.append({"username": user[1], "email": user[2]})
    # To close the connection
    conn.close()
    return userList

def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host=db_conn_arr[0],
        user=db_conn_arr[1],
        password=db_conn_arr[2],
        db=db_conn_arr[3],
    )
    return conn

if __name__ == '__main__':
    app.run(debug=True)
