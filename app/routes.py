from flask import render_template, url_for, flash, redirect
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post
from flask_login import login_user, current_user

posts = [
    {
        'author': 'joao mesquita',
        'title':'Blog post 1',
        'content': 'First post',
        'date_posted':'February 21,2019'
    },
     {
        'author': 'joao mesquita',
        'title':'Blog post 2',
        'content': 'Second post',
        'date_posted':'February 21,2019'
    }
]

@app.route("/") #@app.route faz a rota para a página
def home(): #o nome da página pode ser qualquer, por padrão é index
    return render_template('index.html', posts=posts)

@app.route("/about") 
def about():
     return render_template('about.html', title='About') 
#via python aqui se envia pro html o objeto, variável, caractere ou qualquer coisa que seja e o html fica responsável por transmitir as infos

@app.route("/register", methods=['GET','POST']) 
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') #criptografando as senhas dos usuários por uma tabela hash
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in','success')
        #flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login", methods=['GET','POST']) 
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home')) 
        else:
      #  if form.email.data == 'admin@blog.com' and form.password.data == 'password':
       #     flash('You Have Been Logged In!','success')
        #    return redirect(url_for('home'))
         # else:
        
            flash('Login Unsuccessful. Please check email and password','danger')

    return render_template('login.html',title='Login',form=form)
