from app import app, db  # Importando a instância do Flask e o objeto db
from flask import render_template, request  # Importando a função render_template do Flask e a função request para recuperar os dados do formulário
from app.models import User  # Importando a classe User do arquivo models.py

@app.route('/', methods=['GET', 'POST'])  # Rota para a página inicial e método para recuperar os dados do formulário
def home():
# recuperando os dados do formuláriopara o banco de dados
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']

        user= User(nome=nome, email=email, assunto=assunto, mensagem=mensagem)  # Criando uma instância da classe User

        db.session.add(user)  # Adicionando o objeto User ao banco de dados
        db.session.commit()  # Salvando as alterações no banco de dados

    return render_template('index.html')