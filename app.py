from flask import Flask, render_template, url_for

app = Flask(__name__)
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
if __name__ == '__main__':
    app.run(debug=True)
    
    
