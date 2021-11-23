from os import environ
from flask_pymongo import PyMongo

def createDB(app):
    password = environ.get('DB_PASSWORD')

    app.config['SECRET_KEY'] = '17e131f0610fcce19f961823097d0c3922fcfbd8'
    app.config['MONGO_URI'] = 'mongodb+srv://benaram:%s@ben-store.9txs8.mongodb.net/speech-therapist?retryWrites=true&w=majority' % password

    mongodb_client = PyMongo(app)
    db = mongodb_client.db
    return db