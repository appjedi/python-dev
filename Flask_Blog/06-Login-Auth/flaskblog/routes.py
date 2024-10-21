from flask import render_template, url_for, flash, redirect, request, g, session
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


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
users =[
    {
        'email':'testerb@test.com',
        'password':'$2b$12$7DVk/HiN6HfjPgh3/DXPKeTRDxvWWJaUzYppHycRwZsZDTxWNcc8K',
        'is_active':True,
        'remember':True
    }
   
]
users.append( {
        'email':'tester@test.com',
        'password':'$2b$12$7DVk/HiN6HfjPgh3/DXPKeTRDxvWWJaUzYppHycRwZsZDTxWNcc8K',
        'is_active':False,
        'remember':False
})
users.append( {
        'email':'bob@test.com',
        'password':'$2b$12$7DVk/HiN6HfjPgh3/DXPKeTRDxvWWJaUzYppHycRwZsZDTxWNcc8K',
        'is_active':False,
        'remember':False
})
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        print ("HASH PW:", hashed_password)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/hash/<word>", methods=['GET'])
def getHash(word):
    hashed_password = bcrypt.generate_password_hash(word).decode('utf-8')

@app.route("/user", methods=['GET'])
def getUserTest():
    #user=getUser(un)
    un=session['user']
    print ("USER",un)
    
    
    return un
@app.route("/user/<un>", methods=['GET'])
def setUserTest(un):

    session['user']=un
    #user=g.user
    print ("USER",un)
    
    return un
@app.route("/users", methods=['GET'])
def getUsers():

    #session['user']=un
    #user=g.user
    
    
    return users
def getUser(un):
    for user in users:
        if(user['email']==un):
            #return User(user['email'], user['password'])
            return user
    return None

# $2b$12$7DVk/HiN6HfjPgh3/DXPKeTRDxvWWJaUzYppHycRwZsZDTxWNcc8K
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    #if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    #user =getUser(form.email.data)
    print ("USER:", user)
    if user and bcrypt.check_password_hash(user.password, form.password.data):
            print ("AUTH")
            #login_user(user, remember=True)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
    else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
