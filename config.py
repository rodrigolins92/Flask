import os.path
import psycopg2

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@localhost/storage'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'bakanas'
