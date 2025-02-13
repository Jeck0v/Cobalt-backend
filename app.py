from flask import Flask
from flask_restx import Api
from db.database import db
from api.auth import init_auth_routes
from api.products import init_products_routes
from api.orders import init_orders_routes
from api.ai import init_ia_routes
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['JWT_SECRET_KEY'] = 'web2'
jwt = JWTManager(app)

api = Api(
    app,
    version="1.0",
    title="Cobalt Backend API",
    description="API pour le mini site e-commerce Cobalt",
    doc="/swagger/",
    default="Default",
    default_label="Endpoints par défaut",
    validate=True
)

init_auth_routes(api)
init_products_routes(api)
init_orders_routes(api)
init_ia_routes(api)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)