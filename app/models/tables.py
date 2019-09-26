from app import db
from sqlalchemy import func
import os
from datetime import datetime


class Usuario(db.Model):
	__tablename__ = "usuarios"

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, unique=True)
	password = db.Column(db.String)
	nome = db.Column(db.String)

	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False

	def get_id(self):
		return str(self.id)

	def __init__(self, username, password, nome):
		self.username = username
		self.password = password
		self.nome = nome
	
	def __repr__(self):
		return "<Usuario: %r>" % self.username

class Pedido(db.Model):

	__tablename__ = "pedidos"

	id = db.Column(db.Integer, primary_key=True)
	descricao = db.Column(db.Text)
	data_pedido = db.Column(db.Date, server_default=func.now())
	quantidade = db.Column(db.Integer)
	preco = db.Column(db.Float)
	status_conclusao = db.Column(db.Boolean)

	def __init__(self, descricao, data_pedido, quantidade, preco, status_conclusao):
		self.descricao = descricao
		self.data_pedido = data_pedido
		self.quantidade = quantidade
		self.preco = preco
		self.status_conclusao = status_conclusao

	def __repr__(self):
		return "<Pedido: %r>" % self.descricao

class Estoque(db.Model):

	__tablename__ = "estoque"

	id = db.Column(db.Integer, primary_key=True)
	nome_item = db.Column(db.String)
	quantidade_estoque = db.Column(db.Integer)
	quantidade_minimo = db.Column(db.Integer)
	data_atualizacao = db.Column(db.DateTime, server_default=func.now())

	def __init__(self, nome_item, quantidade_estoque, quantidade_minimo, data_atualizacao):
		self.nome_item = nome_item
		self.quantidade_estoque = quantidade_estoque
		self.quantidade_minimo = quantidade_minimo
		self.data_atualizacao = data_atualizacao

	def __repr__(self):
		return "<Item: %r>" % self.nome_item
