from flask import request, jsonify
from validate_email import validate_email
from utils.jwt import JWT

def Admin(app):
    @app.route('/admin/login', methods=['POST'])
    def login():
        try:
            JWT_KEY = app.config['JWT_KEY']
            db = app.config['DB']
            data = request.get_json()
            email = data['email']
            password = data['password']

            if not email:
                return 'Informe seu email'
            if not password:
                return 'Informe sua senha'
            
            isValidEmail = validate_email(email)
            if not isValidEmail:
                return 'Email-inválido'

            adminsDB = db.admins.find({ 'email': email })
            admins = list(adminsDB)

            if len(admins) == 0:
                return 'Esta conta não existe'

            admin = admins[0]
            if admin['password'] != password:
                return 'Senha incorreta'

            user = {}
            user['email'] = admin['email']
            token = JWT.encode(user, JWT_KEY)

            return jsonify({ 'token': token })
        except:
            return 'Erro'