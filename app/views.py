from app import app, db  # Importando a instância do Flask e o objeto db

from flask import render_template, request  # Importando a função render_template do Flask e a função request para recuperar os dados do formulário

from app.models import User  # Importando a classe User do arquivo models.py

from app.forms import UserForm  # Importando a classe UserForm do arquivo forms.py


@app.route('/', methods=['GET', 'POST'])  # Rota para a página inicial e método para recuperar os dados do formulário
def home():
    form= UserForm()  # Criando uma instância da classe UserForm

    if form.validate_on_submit():  # Verificando se o formulário foi submetido
        form.save()

     
    return render_template('index.html' , form=form)  # Renderizando o template index.html e passando o formulário como parâmetro