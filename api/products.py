from flask import request
from flask_restx import Namespace, Resource, fields
from db.database import db

# Namespace produits
products_ns = Namespace('products', description='Opérations liées aux produits')

# Model Swagger product
product_model = products_ns.model('Product', {
    'id': fields.String(required=True, description='ID du produit'),
    'titre': fields.String(required=True, description='Titre du produit'),
    'description': fields.String(required=True, description='Description du produit'),
    'categorie': fields.String(required=True, description='Catégorie du produit'),
    'prix': fields.Float(required=True, description='Prix du produit'),
    'quantite': fields.Integer(required=True, description='Quantité disponible en stock'),
    'image_url': fields.String(description='URL de l\'image du produit')
})

@products_ns.route('/')
class Products(Resource):
    @products_ns.marshal_list_with(product_model)
    def get(self):
        """
        Récupérer tous les produits
        """
        products = list(db.products.find({}))
        return products, 200

    @products_ns.expect(product_model)
    @products_ns.response(201, 'Produit ajouté')
    def post(self):
        """
        Ajouter un nouveau produit
        """
        data = request.get_json()
        db.products.insert_one(data)
        return {"msg": "Product added successfully"}, 201

@products_ns.route('/seed')
class SeedProducts(Resource):
    def post(self):
        """
        Remplir la collection products avec des produits fictifs
        """
        products = [
            {
                "id": "1",
                "titre": "Leather Bracelet",
                "description": "Genuine leather bracelet for men.",
                "prix": 29.99,
                "quantite": 50,
                "image_url": "https://www.lapetitecannoise.com/333-large_default/bracelet-homme-cuir-argent.jpg",
                "categorie": "Bracelets"
            },
            {
                "id": "2",
                "titre": "Elegant and Retro Watch",
                "description": "Elegant and retro leather watch for men.",
                "prix": 199.99,
                "quantite": 12,
                "image_url": "https://maison-fevre.fr/cdn/shop/products/bracelet-montre-retro-cuir-marron-homme-maison-fevre-fait-main_900x.jpg?v=1725021036",
                "categorie": "Watches"
            },
            {
                "id": "3",
                "titre": "Silver Ring",
                "description": "925 silver ring for men.",
                "prix": 49.99,
                "quantite": 20,
                "image_url": "https://itsara.net/cdn/shop/products/bague-homme-en-argent-ethnique-n027p1_Itsara_bijoux_2048x.jpg?v=1737535078",
                "categorie": "Rings"
            },
            {
                "id": "4",
                "titre": "Stainless Steel Necklace",
                "description": "Stainless steel necklace for men.",
                "prix": 49.99,
                "quantite": 40,
                "image_url": "https://www.ninanina.fr/wp-content/uploads/2019/12/n3575-chaine-figaro-homme-acier-inoxydable-argent-50-cm-bijoux-colliers-hommes-en-ligne-ninanina.jpg",
                "categorie": "Necklaces"
            },
            {
                "id": "5",
                "titre": "Cobalt Pendant",
                "description": "Elegant Cobalt pendant for men.",
                "prix": 299.99,
                "quantite": 15,
                "image_url": "https://caratsutra.in/cdn/shop/products/IMG_20220216_213558.jpg?v=1654097796",
                "categorie": "Pendants"
            },
            {
                "id": "6",
                "titre": "Gold Hoop Earrings",
                "description": "Stylish gold hoop earrings for men.",
                "prix": 179.99,
                "quantite": 30,
                "image_url": "https://www.gld.com/cdn/shop/products/micro-double-row-huggie-earrings-in-yellow-gold-gld-men-3_375x375_crop_center@2x.jpg?v=1680691085%20x2,%20//www.gld.com/cdn/shop/products/micro-double-row-huggie-earrings-in-yellow-gold-gld-men-3_375x375_crop_center.jpg?v=1680691085%20x1",
                "categorie": "Earrings"
            }
        ]

        db.products.insert_many(products)
        return {"msg": "Products added successfully"}, 201

@products_ns.route('/<string:product_id>')
class ProductDetail(Resource):
    @products_ns.marshal_with(product_model)
    @products_ns.response(200, 'Produit trouvé')
    @products_ns.response(404, 'Produit non trouvé')
    def get(self, product_id):
        """
        Récupérer un produit par ID
        """
        product = db.products.find_one({"id": product_id})
        if product:
            return product, 200
        else:
            return {"msg": "Product not found"}, 404

@products_ns.route('/categories')
class Categories(Resource):
    @products_ns.response(200, 'Catégories trouvées')
    def get(self):
        """
        Récupérer toutes les catégories disponibles
        """
        categories = db.products.distinct("categorie")
        return {"categories": categories}, 200

@products_ns.route('/products/<string:category>')
class ProductsByCategory(Resource):
    @products_ns.marshal_list_with(product_model)
    @products_ns.response(200, 'Produits trouvés')
    @products_ns.response(404, 'Aucun produit trouvé pour cette catégorie')
    def get(self, category):
        """
        Récupérer les produits par catégorie
        """
        products = list(db.products.find({"categorie": category}))
        if products:
            return products, 200
        else:
            return {"msg": f"No products found for category '{category}'"}, 404

def init_products_routes(api):
    """
    Initialiser les routes API
    """
    api.add_namespace(products_ns)