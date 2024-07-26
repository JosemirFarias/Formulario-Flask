from flask_wtf import FlaskForm  # Importando a classe FlaskForm do pacote flask_wtf
from wtforms import StringField, SubmitField  # Importando as classes StringField e SubmitField do pacote wtforms
from wtforms.validators import DataRequired, Email  # Importando a classe DataRequired do pacote wtforms.validators e a classe Email do pacote wtforms.validators para validar os campos do formulário
from app import db  # Importando a instância do Flask e o objeto db
from app.models import User  # Importando a classe User do arquivo models.py

class UserForm(FlaskForm):  # Criando a classe UserForm que herda da classe FlaskForm
    nome = StringField('Nome', validators=[DataRequired()])  # Criando o campo nome
    email = StringField('Email', validators=[DataRequired(), Email()])  # Criando o campo email
    assunto = StringField('Assunto', validators=[DataRequired()])  # Criando o campo assunto
    mensagem = StringField('Mensagem', validators=[DataRequired()])  # Criando o campo mensagem
    enviar = SubmitField('Enviar')  # Criando o botão de envio do formulário

    def save(self):  # Método para salvar os dados do formulário no banco de dados
        user = User(nome=self.nome.data, email=self.email.data, assunto=self.assunto.data, mensagem=self.mensagem.data)

        db.session.add(user)  # Adicionando o objeto User ao banco de dados
        db.session.commit()  # Salvando as alterações no banco de dados