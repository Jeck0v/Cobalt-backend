from flask import request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from db.database import db

shopping_cart_ns = Namespace('shopcart', description='Opérations liées au panier')

cart_item_model = shopping_cart_ns.model('CartItem', {
    'product_id': fields.String(required=True, description='ID du produit'),
    'quantity': fields.Integer(required=True, description='Quantité du produit')
})


@shopping_cart_ns.route('/<string:user_id>')
class UserCart(Resource):
    @shopping_cart_ns.marshal_list_with(cart_item_model)
    @jwt_required()
    def get(self, user_id):
        """
        Récupérer le panier d'un utilisateur        """
        current_user_email = get_jwt_identity()

        if current_user_email != user_id:
            return {"msg": "Unauthorized access to cart"}, 403

        cart_items = list(db.shopping_cart.find({"user_email": user_id}))
        return cart_items, 200

    @shopping_cart_ns.expect(cart_item_model)
    @shopping_cart_ns.response(201, 'Produit ajouté au panier')
    @jwt_required()
    def post(self, user_id):
        """
        Ajouter un produit au panier d'un utilisateur        """
        current_user_email = get_jwt_identity()

        if current_user_email != user_id:
            return {"msg": "Unauthorized access to cart"}, 403

        data = request.get_json()
        product_id = data['product_id']
        product = db.products.find_one({"id": product_id})
        if not product:
            return {"msg": "Product not found"}, 404

        data['price'] = product['prix']
        data['user_email'] = user_id

        existing_item = db.shopping_cart.find_one({"user_email": user_id, "product_id": product_id})
        if existing_item:

            new_quantity = existing_item['quantity'] + data['quantity']
            db.shopping_cart.update_one(
                {"user_email": user_id, "product_id": product_id},
                {"$set": {"quantity": new_quantity}}
            )
            return {"msg": "Product quantity updated in cart"}, 200
        else:

            db.shopping_cart.insert_one(data)
            return {"msg": "Product added to cart successfully"}, 201

    @shopping_cart_ns.expect(cart_item_model)
    @shopping_cart_ns.response(200, 'Produit retiré du panier')
    @jwt_required()
    def delete(self, user_id):
        """
        Retirer un produit du panier d'un utilisateur        """
        current_user_email = get_jwt_identity()

        if current_user_email != user_id:
            return {"msg": "Unauthorized access to cart"}, 403

        data = request.get_json()
        db.shopping_cart.delete_one({"user_email": user_id, "product_id": data['product_id']})
        return {"msg": "Product removed from cart successfully"}, 200


@shopping_cart_ns.route('/<string:user_id>/validate')
class ValidateCart(Resource):
    @jwt_required()
    def post(self, user_id):
        """
        Valider le panier d'un utilisateur et créer une commande        """
        current_user_email = get_jwt_identity()

        if current_user_email != user_id:
            return {"msg": "Unauthorized access to cart"}, 403

        cart_items = list(db.shopping_cart.find({"user_email": user_id}))
        if not cart_items:
            return {"msg": "Cart is empty"}, 400

        total_price = 0
        for item in cart_items:
            product = db.products.find_one({"id": item['product_id']})
            if product:
                total_price += product['prix'] * item['quantity']

        order = {
            "user_email": user_id,
            "cart_items": cart_items,
            "total_price": total_price,
            "status": "validated"
        }
        db.orders.insert_one(order)

        db.shopping_cart.delete_many({"user_email": user_id})

        return {"msg": "Cart validated and order created successfully"}, 201


@shopping_cart_ns.route('/<string:user_id>/total')
class CartTotal(Resource):
    @jwt_required()
    def get(self, user_id):
        """
        Calculer le prix total du panier d'un utilisateur        """
        current_user_email = get_jwt_identity()

        if current_user_email != user_id:
            return {"msg": "Unauthorized access to cart"}, 403

        cart_items = list(db.shopping_cart.find({"user_email": user_id}))
        total = 0

        for item in cart_items:
            product = db.products.find_one({"id": item['product_id']})
            if product:
                total += product['prix'] * item['quantity']

        return {"total_price": total}, 200


def init_shopping_cart_routes(api):
    """
    Initialiser les routes API pour le panier    """
    api.add_namespace(shopping_cart_ns)