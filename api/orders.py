from flask import request
from flask_restx import Namespace, Resource, fields
from db.database import db
from api.shopcart import cart_item_model

orders_ns = Namespace('orders', description='Opérations liées aux commandes')

order_model = orders_ns.model('Order', {
    'user_email': fields.String(required=True, description='Email de l\'utilisateur'),
    'cart_items': fields.List(fields.Nested(cart_item_model)),
    'total_price': fields.Float(required=True, description='Prix total de la commande'),
    'status': fields.String(required=True, description='Statut de la commande')
})


@orders_ns.route('/<string:user_id>')
class UserOrders(Resource):
    @orders_ns.marshal_list_with(order_model)
    def get(self, user_id):
        orders = list(db.orders.find({"user_email": user_id, "status": "validated"}))
        return orders, 200


@orders_ns.route('/<string:order_id>')
class OrderDetail(Resource):
    @orders_ns.marshal_with(order_model)
    def get(self, order_id):
        order = db.orders.find_one({"order_id": order_id, "status": "validated"})
        if not order:
            return {"msg": "Order not found or not validated"}, 404

        return order, 200


@orders_ns.route('/<string:user_id>/total')
class OrderTotal(Resource):
    def get(self, user_id):
        orders = list(db.orders.find({"user_email": user_id, "status": "validated"}))
        total = sum(order['total_price'] for order in orders)
        return {"total_price": total}, 200


def init_orders_routes(api):
    api.add_namespace(orders_ns)