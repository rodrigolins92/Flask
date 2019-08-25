from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
# Foi enviado a configuração para o config.py
# Nova configuração com método config abaixo...

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
# Comandos para migração do DB e o comando completo 
# para o gerenciamento de migração

lm = LoginManager()
lm.init_app(app)

from app.models import tables
from app.controllers import default