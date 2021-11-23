from flask_cors import CORS
from dotenv_config import Config as dotenvConfig
from os import environ

from models.db import createDB
from application import app
from routes import Routes

dotenvConfig('.env')
CORS(app)

db = createDB(app)

app.config['JWT_KEY'] = environ.get('JWT_KEY')
app.config['DB'] = db
Routes(app)

if __name__ == '__main__':
    app.run(host='localhost', port=3000)