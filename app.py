from flask import Flask, render_template, request, make_response
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'web2'
jwt = JWTManager(app)

users = [
    {"id": 1, "username": "admin", "password": "admin"}
]


@app.route('/connexion', methods=['POST'])
def connexion():
    username = request.form['username']
    password = request.form['password']

    for user in users:
        if user['username'] == username and user['password'] == password:
            access_token = create_access_token(identity=username)
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
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    user = {"id": len(users) + 1, "firstname": firstname, "name": name, "username": username, "password": password, "email": email}
    users.append(user)

    return "User added successfully" + str(users)

@app.route('/signup')
def signin():
   return "hello"


@app.route('/login')
def index():
    return "hello"


@app.route('/app')
@jwt_required()
def app():
    return "hello"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)