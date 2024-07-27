from app import app, db  # Importando a instância do Flask e o objeto db

from flask import render_template, request, flash, redirect, url_for # Importando a função render_template do Flask, a função request para recuperar os dados do formulário, a função flash para exibir mensagens de erro e sucesso, a função redirect para redirecionar o usuário para outra página e a função url_for para gerar URLs para as rotas

from app.models import User  # Importando a classe User do arquivo models.py

from app.forms import UserForm  # Importando a classe UserForm do arquivo forms.py


@app.route('/', methods=['GET', 'POST'])  # Rota para a página inicial e método para recuperar os dados do formulário
def home():
    form= UserForm()  # Criando uma instância da classe UserForm

    if form.validate_on_submit():  # Verificando se o formulário foi submetido
        form.save()

        flash('Usuário cadastrado com sucesso!', 'success')  # Adicionando a mensagem de sucesso
        return redirect(url_for('home'))  # Redirecionando para a página inicial

     
    return render_template('index.html' , form=form)  # Renderizando o template index.html e passando o formulário como parâmetro

@app.route('/lista')  # Rota para a página de listagem
def lista():
    users = User.query.all()
    context = {'users': users}  # Criando um dicionário com a lista de usuários

    return render_template('lista.html', users=users)  # Renderizando o template lista.html e passando o dicionário como parâmetro