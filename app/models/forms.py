from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired
from datetime import date, datetime


class LoginForm(FlaskForm):

	username = StringField("username", validators=[DataRequired()])
	password = PasswordField("password", validators=[DataRequired()])
	remember_me = BooleanField("remember_me")

class PedidoForm(FlaskForm):

	servico = SelectField("servico", choices=[('-- Selecione --', '-- Selecione --'),
												('Cópia preto e branco', 'Cópia preto e branco'), 
												('Cópia colorida', 'Cópia colorida'), 
												('Encadernação', 'Encadernação'), 
												('Plastificação', 'Plastificação'), 
												('Plotagem', 'Plotagem'), 
												('Outros', 'Outros')])
	observacao = TextAreaField("observacao")
	data_pedido = DateField(default=date.today())
	quantidade = IntegerField()
	preco = DecimalField(places=2)
	status_conclusao = BooleanField()

class EstoqueForm(FlaskForm):

	nome_item = StringField("nome_item", validators=[DataRequired()])
	quantidade_estoque = IntegerField()
	quantidade_minimo = IntegerField()
	data_atualizacao = DateTimeField(default=datetime.now())