from flask import Flask, render_template, request, make_response
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from pymango import MongoClient

app = Flask(__name__)

# tout rajouter dans un .env
server = "mongodb://localhost:27017/"
username = "cobaltDB"
password = ""
port = 27017

if server == "localhost":
    client = MongoClient("mongodb://mongo", username=username, password=password, port=port)

else:
    client = MongoClient(server, username=username, password=password, port=port)

# pour la bdd mongodb => 1 collection users =
'''
dans la collection users, un user contient: 
un id, un email, un nom, un prenom, un password, un user_token
'''

# 1 collection produits
'''
dans la collection produits, un produit contient: 
un id, un titre, une description, un prix, une quantité (la quantité total du produit en stockage)
'''
# 1 collection commandes_users
'''
dans la collection commande_users, une commande contient: 
un id, un user_id, les produits_id, quantite_sel
'''
# faire le docker-compose etc...
# faire en sorte de vérifier le jwt de l'user avec le token de l'user dans la de bdd mongodb,
# le back génère le jwt à l'inscription de l'user, donc 1 user 1 token qui permet de vérifier que le compte de l'user lui appartient bien.
# a la connexion on vérifie le jwt

app.config['JWT_SECRET_KEY'] = 'web2'
jwt = JWTManager(app)

users = [
    {"id": 1, "username": "admin", "password": "admin"}
]


@app.route('/connexion', methods=['POST'])
def connexion():
    email = request.form['email']
    password = request.form['password']

    for user in users:
        if user['email'] == username and user['password'] == password:
            access_token = create_access_token(identity=email)
            print(access_token)
            response = make_response(render_template('index.html'))
            response.set_cookie('access_token', access_token)
            return response
        else:
            return "Invalid credentials"

@app.route('/register', methods=['POST'])
def register():
    firstname = request.form['firstname']
    name = request.form['name']
    password = request.form['password']
    email = request.form['email']

    user = {"id": len(users) + 1, "firstname": firstname, "name": name, "password": password, "email": email}
    users.append(user)

    return "User added successfully" + str(users)

@app.route('/signin')
def signin():
   return render_template('signin.html')


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/app')
@jwt_required()
def app():
    return render_template('app.html')

@app.route('/app/produit',methods=['GET'])
@jwt_required()
def produit():
    return "on va chercher le prduit donc l'img + titre + prix + descr + quantité dans la bdd (collection produits"

@app.route('/app/quantite',methods=['GET'])
@jwt_required()
def quantite():
    return "on verif la quantité, si elle est supérieur à 0 alors on accepte la commande sinon, on préviens l'user qu'il n'y a pas de quantité"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)