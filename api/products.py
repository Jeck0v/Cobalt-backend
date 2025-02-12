from flask_restx import Namespace, Resource
from db.database import db

products_ns = Namespace('products', description='Opérations liées aux produits')

@products_ns.route('/')
class Products(Resource):
    def get(self):
        """Récupérer tous les produits"""
        products = list(db.products.find({}))
        return {"products": products}, 200

def init_products_routes(api):
    api.add_namespace(products_ns)