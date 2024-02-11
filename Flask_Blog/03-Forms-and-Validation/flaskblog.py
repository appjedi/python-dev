from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import MySQLdb

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

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

def getConn():
#db = MySQLdb.connect(host="localhost",user="root",password="maria1",database="test")
    db = MySQLdb.connect(host="127.0.0.1", user="root",
                     password="Jedi2023", database="dev")
    return db

def getUser (un, pw):
    conn=getConn()
    cur = conn.cursor()
    cur.execute("select * from users WHERE username = %s AND password= %s", (un,pw))
    output = cur.fetchall()
    print(output)
    conn.close()
    return output

def registerUser(un,pw):
    conn=getConn()
    cur = conn.cursor()
    insert = "INSERT INTO users (username, password, role_id, status, createDt) VALUES(%s,%s,2,1,SYSDATE())"
    cur.execute(insert, (un,pw))
    conn.commit()
    conn.close()

@app.route("/users")
def getUsers():
    conn=getConn()
    cur = conn.cursor()
    cur.execute("select * from users")
    output = cur.fetchall()
    print(output)
    conn.close()
    return {'data': output}

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
        registerUser(form.email.data, form.password.data)
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #if form.email.data == 'admin@blog.com' and form.password.data == 'password':
        user=getUser(form.email.data,form.password.data)
        if len(user)>0:
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)

    # To close the connection
    