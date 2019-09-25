from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired
from datetime import date


class LoginForm(FlaskForm):

	username = StringField("username", validators=[DataRequired()])
	password = PasswordField("password", validators=[DataRequired()])
	remember_me = BooleanField("remember_me")

class PedidoForm(FlaskForm):

	descricao = TextAreaField("descricao")
	data_pedido = DateField(default=date.today())
	quantidade = IntegerField()
	preco = DecimalField(places=2)
	status_conclusao = BooleanField()