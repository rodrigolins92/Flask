from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	username = StringField("username", validators=[DataRequired()])
	password = PasswordField("password", validators=[DataRequired()])
	remember_me = BooleanField("remember_me")

class PedidoForm(FlaskForm):
	descricao = TextAreaField("descricao")
	data_pedido = DateField(format='%d-%m-%Y')
	quantidade = IntegerField()
	preco = DecimalField(places=2)
	status_conclusao = BooleanField()