from flask_restx import Namespace, Resource, fields
from db.database import db

orders_ns = Namespace('orders', description='Opérations liées aux commandes')

order_model = orders_ns.model('Order', {
    'products_id': fields.List(fields.String, required=True, description='IDs des produits'),
    'quantite_sel': fields.Integer(required=True, description='Quantité sélectionnée')
})

@orders_ns.route('/')
class Orders(Resource):
    @orders_ns.expect(order_model)
    def post(self):
        """Créer une nouvelle commande"""
        user_email = get_jwt_identity()
        user = db.users.find_one({"email": user_email})
        if not user:
            return {"msg": "User not found"}, 404
        order_details = request.json
        db.orders_users.insert_one({
            "user_id": user["_id"],
            "products_id": order_details["products_id"],
            "quantite_sel": order_details["quantite_sel"]
        })
        return {"msg": "Order created"}, 201

def init_orders_routes(api):
    api.add_namespace(orders_ns)