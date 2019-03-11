from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post

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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Acount created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login", methods=['GET','POST']) 
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You Have Been Logged In!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password','danger')

    return render_template('login.html',title='Login',form=form)
