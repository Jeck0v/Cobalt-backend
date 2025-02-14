from flask import request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from db.database import db
from models.user import User

# namespace pour les route d'auth
auth_ns = Namespace('auth', description='Opérations liées à l\'authentification')

# model User pour Swagger
user_model = auth_ns.model('User', {
    '_id': fields.String(description='ID unique de l\'utilisateur'),
    'firstname': fields.String(required=True, description='Prénom de l\'utilisateur'),
    'name': fields.String(required=True, description='Nom de l\'utilisateur'),
    'password': fields.String(required=True, description='Mot de passe de l\'utilisateur'),
    'email': fields.String(required=True, description='Email de l\'utilisateur')
})

# model Login pour Swagger
login_model = auth_ns.model('Login', {
    'email': fields.String(required=True, description='Email de l\'utilisateur'),
    'password': fields.String(required=True, description='Mot de passe de l\'utilisateur')
})

@auth_ns.route('/register')
class Register(Resource):
    @auth_ns.expect(user_model)
    @auth_ns.response(201, 'Utilisateur créé')
    @auth_ns.response(400, 'Utilisateur déjà existant')
    def post(self):
        """
        Register user
        """
        data = request.get_json()
        firstname = data.get('firstname')
        name = data.get('name')
        password = data.get('password')
        email = data.get('email')

        if db.users.find_one({"email": email}):
            return {"msg": "User already exists"}, 400

        user = User(firstname, name, password, email)
        db.users.insert_one(user.to_dict())

        # token jwt pour l'user
        access_token = create_access_token(identity=email)
        return {"access_token": access_token}, 201

@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.expect(login_model)
    @auth_ns.response(200, 'Connexion réussie', user_model)
    @auth_ns.response(401, 'Identifiants invalides')
    def post(self):
        """
        Login user
        """
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = db.users.find_one({"email": email, "password": password})
        if user:
            access_token = create_access_token(identity=email)
            user['_id'] = str(user['_id'])
            return {
                "access_token": access_token,
                "user": user
            }, 200
        else:
            return {"msg": "Bad username or password"}, 401
@auth_ns.route('/modify')
class Modify(Resource):
    @jwt_required()
    @auth_ns.expect(user_model)
    @auth_ns.response(200, 'Utilisateur modifié')
    @auth_ns.response(401, 'Utilisateur non connecté')
    def put(self):
        """
        Modifier les informations de l'utilisateur connecté
        """
        Aemail = get_jwt_identity()
        

        data = request.get_json()
        firstname = data.get('firstname')
        name = data.get('name')
        password = data.get('password')
        email = data.get('email')

        user = db.users.find_one({"email": Aemail})
        if user:
            db.users.update_one({"email": Aemail}, {"$set": {"firstname": firstname, "name": name, "password": password, "email": email}})
            return {"msg": "User modified"}, 200
        else:
            return {"msg": "No user connected"}, 401

@auth_ns.route('/view')
class View(Resource):
    @jwt_required()
    @auth_ns.marshal_with(user_model)
    def get(self):
        """
        Récupérer les informations de l'utilisateur connecté
        """
        email = get_jwt_identity()
        user = db.users.find_one({"email": email})
        if user:
            user["_id"] = str(user["_id"])
            # Ne pas renvoyer le mot de passe dans la réponse
            return user, 200
        else:
            return {"msg": "No user connected"}, 401

def init_auth_routes(api):
    """
    init routes API
    """
    api.add_namespace(auth_ns)