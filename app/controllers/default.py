from flask import render_template, flash, redirect, url_for, session, Markup
from flask_login import login_user, logout_user, login_required
from app import app, db, lm

from app.models.forms import *
from app.models.tables import *


@lm.user_loader
def load_user(id):
    return Usuario.query.filter_by(id=id).first()

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

#Iniciando parte de login/logoff

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Usuário logado")
            return redirect(url_for("index"))
        else:
            flash("Login inválido")
    #else:
    #   return "erro no login"
    return render_template('login.html', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Usuário Deslogado")
    return redirect(url_for("index"))

#Iniciando parte de pedidos

@app.route("/pedidos", methods=["GET", "POST"])
@login_required
def pedidos():
    form = PedidoForm()
    if form.validate_on_submit():

        i = Pedido(form.servico.data,
            form.observacao.data, 
            form.data_pedido.data, 
            form.quantidade.data, 
            form.preco.data, 
            form.status_conclusao.data)

        db.session.add(i)
        db.session.commit()
        flash("Pedido adicionado com sucesso!!")

    return render_template('pedidos.html', form=form)


@app.route("/visualizar", methods=["GET", "POST"])
@login_required
def visualizar():
    pedidos_ativos = Pedido.query.filter_by(status_conclusao=False).all()
    pedidos_concluidos = Pedido.query.filter_by(status_conclusao=True).all()
    return render_template('visualizar.html', pedidos_ativos=pedidos_ativos, pedidos_concluidos=pedidos_concluidos)

@app.route('/visualizar/complete/<id>')
@login_required
def complete(id):
    pedido = Pedido.query.filter_by(id=int(id)).first_or_404()
    pedido.status_conclusao = True
    db.session.commit()
    return redirect(url_for('visualizar'))

@app.route("/visualizar/delete/<id>")
@login_required
def delete(id):
    pedido = Pedido.query.filter_by(id=int(id)).first_or_404()
    db.session.delete(pedido)
    db.session.commit()
    return redirect(url_for('visualizar'))

@app.route("/visualizar/confirmacao/<id>")
@login_required
def confirmacao(id):
    flash(Markup("Confirma a exclusão do pedido?</br></br><a href='/visualizar/delete/" + str(id) + "' class='btn btn-outline-danger btn-sm mr-3 ml-3'>Sim</a><a href='/visualizar' class='btn btn-outline-primary btn-sm ml-3 mr-3'>Não</a>"))
    return redirect(url_for('visualizar'))


#Iniciando parte de controle de estoque

@app.route('/estoque')
@login_required
def estoque():
    estoque = Estoque.query.order_by(Estoque.id).all()

    return render_template('estoque.html', estoque=estoque)

@app.route('/estoque/adicionar', methods=["GET", "POST"])
@login_required
def adicionarEstoque():
    form = EstoqueForm()
    if form.validate_on_submit():

        i = Estoque(form.nome_item.data, 
            form.quantidade_estoque.data, 
            form.quantidade_minimo.data, 
            form.data_atualizacao.data)

        db.session.add(i)
        db.session.commit()
        flash("Item adicionado com sucesso!!")

    return render_template('adicionar_estoque.html', form=form)

@app.route('/estoque/atualizar/<id>', methods=["GET", "POST"])
@login_required
def atualizarItem(id):
    item = Estoque.query.filter_by(id=int(id)).first()
    form = EstoqueForm()
    if form.validate_on_submit():
        
        item.nome_item = form.nome_item.data
        item.quantidade_estoque = form.quantidade_estoque.data
        item.quantidade_minimo = form.quantidade_minimo.data
        item.data_atualizacao = form.data_atualizacao.data

        
        i = Estoque(item.nome_item, 
            item.quantidade_estoque, 
            item.quantidade_minimo, 
            item.data_atualizacao)

        db.session.commit()
        flash("Atualização concluída..")

        return redirect(url_for('estoque'))

    return render_template('atualizar_estoque.html', form=form, item=item)

@app.route("/estoque/delete/<id>")
@login_required
def deleteItem(id):
    item = Estoque.query.filter_by(id=int(id)).first_or_404()
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('estoque'))

@app.route("/estoque/confirmacao/<id>")
@login_required
def confirmacaoEstoque(id):
    flash(Markup("Confirma a exclusão do item?</br></br><a href='/estoque/delete/" + str(id) + "' class='btn btn-outline-danger btn-sm mr-3 ml-3'>Sim</a><a href='/estoque' class='btn btn-outline-primary btn-sm ml-3 mr-3'>Não</a>"))
    return redirect(url_for('estoque'))