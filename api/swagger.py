from flask_restx import Api, fields

api = Api(
    version="1.0",
    title="Cobalt Backend API",
    description="API pour le mini site e-commerce Cobalt",
    doc="/swagger/"
)

user_model = api.model('User', {
    'firstname': fields.String(required=True, description='Prénom de l\'utilisateur'),
    'name': fields.String(required=True, description='Nom de l\'utilisateur'),
    'password': fields.String(required=True, description='Mot de passe de l\'utilisateur'),
    'email': fields.String(required=True, description='Email de l\'utilisateur')
})

order_model = api.model('Order', {
    'products_id': fields.List(fields.String, required=True, description='IDs des produits'),
    'quantite_sel': fields.Integer(required=True, description='Quantité sélectionnée')
})