from pymongo import MongoClient

client = MongoClient(
    host="mongo",
    port=27017,
    username="cobaltdb",
    password="-)i8N~x4r9cVX8"
)

db = client.cobalt_db


def initialize_database():
    """
    Initialise la base de données en créant les collections nécessaires si elles n'existent pas déjà,
    et les remplit avec des données de test si elles sont vides.
    """
    required_collections = ['users', 'products', 'orders']
    existing_collections = db.list_collection_names()
    for collection in required_collections:
        if collection not in existing_collections:
            db.create_collection(collection)
            print(f"Collection '{collection}' créée.")

    if db.products.count_documents({}) == 0:
        products = [
            {
                "id": "1",
                "titre": "Bracelet en cuir",
                "description": "Bracelet en cuir véritable pour homme.",
                "prix": 44.99,
                "quantite": 50,
                "image_url": "https://www.lapetitecannoise.com/333-large_default/bracelet-homme-cuir-argent.jpg"
            },
            {
                "id": "2",
                "titre": "Montre élégante et rétro",
                "description": "Montre élégante, et rétro en cuir pour homme. ",
                "prix": 199.99,
                "quantite": 12,
                "image_url": "https://maison-fevre.fr/cdn/shop/products/bracelet-montre-retro-cuir-marron-homme-maison-fevre-fait-main_900x.jpg?v=1725021036"
            },
            {
                "id": "3",
                "titre": "Bague en argent",
                "description": "Bague en argent 925 pour homme.",
                "prix": 82.99,
                "quantite": 20,
                "image_url": "https://itsara.net/cdn/shop/products/bague-homme-en-argent-ethnique-n027p1_Itsara_bijoux_2048x.jpg?v=1737535078"
            },
            {
                "id": "4",
                "titre": "Collier en acier",
                "description": "Collier en acier inoxydable pour homme.",
                "prix": 86.99,
                "quantite": 40,
                "image_url": "https://www.ninanina.fr/wp-content/uploads/2019/12/n3575-chaine-figaro-homme-acier-inoxydable-argent-50-cm-bijoux-colliers-hommes-en-ligne-ninanina.jpg"
            },
            {
                "id": "5",
                "titre": "Bague en or",
                "description": "Bague en or massif, dans un style à la fois moderne et contemporain.",
                "prix": 82.99,
                "quantite": 20,
                "image_url": "https://cdn-media.glamira.com/media/product/newgeneration/view/1/sku/8381feratibes/alloycolour/yellow.jpg"
            },
            {
                "id": "6",
                "titre": "Collier en argent massi",
                "description": "Collier en argent massif, dans un style moderne",
                "prix": 84.99,
                "quantite": 20,
                "image_url": "https://media.cdnws.com/_i/18487/12510/2963/10/collier-gourmette-ronde-7mm-argent-rhodie-1200p-l.jpeg"
            },
            {
                "id": "7",
                "titre": "Bague en argent",
                "description": "Bague en argent 925 pour homme.",
                "prix": 89.99,
                "quantite": 20,
                "image_url": "https://itsara.net/cdn/shop/products/bague-homme-en-argent-ethnique-n027p1_Itsara_bijoux_2048x.jpg?v=1737535078"
            },
            {
                "id": "8",
                "titre": "Collier en acier",
                "description": "Collier en acier inoxydable pour homme.",
                "prix": 79.99,
                "quantite": 40,
                "image_url": "https://www.ninanina.fr/wp-content/uploads/2019/12/n3575-chaine-figaro-homme-acier-inoxydable-argent-50-cm-bijoux-colliers-hommes-en-ligne-ninanina.jpg"
            },
            {
                "id": "9",
                "titre": "Collier en argent massi",
                "description": "Collier en argent massif, dans un style moderne",
                "prix": 87.99,
                "quantite": 20,
                "image_url": "https://media.cdnws.com/_i/18487/12510/2963/10/collier-gourmette-ronde-7mm-argent-rhodie-1200p-l.jpeg"
            },
            {
                "id": "10",
                "titre": "Bague en argent",
                "description": "Bague en argent 925 pour homme.",
                "prix": 120.99,
                "quantite": 20,
                "image_url": "https://itsara.net/cdn/shop/products/bague-homme-en-argent-ethnique-n027p1_Itsara_bijoux_2048x.jpg?v=1737535078"
            },
            {
                "id": "11",
                "titre": "Collier en acier",
                "description": "Collier en acier inoxydable pour homme.",
                "prix": 130.99,
                "quantite": 40,
                "image_url": "https://www.ninanina.fr/wp-content/uploads/2019/12/n3575-chaine-figaro-homme-acier-inoxydable-argent-50-cm-bijoux-colliers-hommes-en-ligne-ninanina.jpg"
            },
            {
                "id": "12",
                "titre": "Bracelet en cuir",
                "description": "Bracelet en cuir véritable pour homme.",
                "prix": 149.99,
                "quantite": 50,
                "image_url": "https://www.lapetitecannoise.com/333-large_default/bracelet-homme-cuir-argent.jpg"
            },
            {
                "id": "13",
                "titre": "Montre élégante et rétro",
                "description": "Montre élégante, et rétro en cuir pour homme. ",
                "prix": 76.99,
                "quantite": 12,
                "image_url": "https://maison-fevre.fr/cdn/shop/products/bracelet-montre-retro-cuir-marron-homme-maison-fevre-fait-main_900x.jpg?v=1725021036"
            },
            {
                "id": "14",
                "titre": "Bague en argent",
                "description": "Bague en argent 925 pour homme.",
                "prix": 89.99,
                "quantite": 20,
                "image_url": "https://itsara.net/cdn/shop/products/bague-homme-en-argent-ethnique-n027p1_Itsara_bijoux_2048x.jpg?v=1737535078"
            },
            {
                "id": "15",
                "titre": "Collier en acier",
                "description": "Collier en acier inoxydable pour homme.",
                "prix": 99.99,
                "quantite": 40,
                "image_url": "https://www.ninanina.fr/wp-content/uploads/2019/12/n3575-chaine-figaro-homme-acier-inoxydable-argent-50-cm-bijoux-colliers-hommes-en-ligne-ninanina.jpg"
            },
            {
                "id": "16",
                "titre": "Bague en or",
                "description": "Bague en or massif, dans un style à la fois moderne et contemporain.",
                "prix": 96.99,
                "quantite": 20,
                "image_url": "https://cdn-media.glamira.com/media/product/newgeneration/view/1/sku/8381feratibes/alloycolour/yellow.jpg"
            },
            {
                "id": "17",
                "titre": "Bague en argent",
                "description": "Bague en argent 925 pour homme.",
                "prix": 420.99,
                "quantite": 20,
                "image_url": "https://itsara.net/cdn/shop/products/bague-homme-en-argent-ethnique-n027p1_Itsara_bijoux_2048x.jpg?v=1737535078"
            },
            {
                "id": "18",
                "titre": "Collier en acier",
                "description": "Collier en acier inoxydable pour homme.",
                "prix": 134.99,
                "quantite": 40,
                "image_url": "https://www.ninanina.fr/wp-content/uploads/2019/12/n3575-chaine-figaro-homme-acier-inoxydable-argent-50-cm-bijoux-colliers-hommes-en-ligne-ninanina.jpg"
            },
            {
                "id": "19",
                "titre": "Bracelet en cuir",
                "description": "Bracelet en cuir véritable pour homme.",
                "prix": 127.99,
                "quantite": 50,
                "image_url": "https://www.lapetitecannoise.com/333-large_default/bracelet-homme-cuir-argent.jpg"
            },
            {
                "id": "20",
                "titre": "Montre élégante et rétro",
                "description": "Montre élégante, et rétro en cuir pour homme. ",
                "prix": 194.99,
                "quantite": 12,
                "image_url": "https://maison-fevre.fr/cdn/shop/products/bracelet-montre-retro-cuir-marron-homme-maison-fevre-fait-main_900x.jpg?v=1725021036"
            },
            {
                "id": "21",
                "titre": "Collier en acier",
                "description": "Collier en acier inoxydable pour homme.",
                "prix": 189.99,
                "quantite": 40,
                "image_url": "https://www.ninanina.fr/wp-content/uploads/2019/12/n3575-chaine-figaro-homme-acier-inoxydable-argent-50-cm-bijoux-colliers-hommes-en-ligne-ninanina.jpg"
            },
            {
                "id": "22",
                "titre": "Bague en or",
                "description": "Bague en or massif, dans un style à la fois moderne et contemporain.",
                "prix": 140.99,
                "quantite": 20,
                "image_url": "https://cdn-media.glamira.com/media/product/newgeneration/view/1/sku/8381feratibes/alloycolour/yellow.jpg"
            },
            {
                "id": "23",
                "titre": "Collier en argent massi",
                "description": "Collier en argent massif, dans un style moderne",
                "prix": 456.99,
                "quantite": 20,
                "image_url": "https://media.cdnws.com/_i/18487/12510/2963/10/collier-gourmette-ronde-7mm-argent-rhodie-1200p-l.jpeg"
            },
            {
                "id": "24",
                "titre": "Bague en argent",
                "description": "Bague en argent 925 pour homme.",
                "prix": 239.99,
                "quantite": 20,
                "image_url": "https://itsara.net/cdn/shop/products/bague-homme-en-argent-ethnique-n027p1_Itsara_bijoux_2048x.jpg?v=1737535078"
            },
            {
                "id": "25",
                "titre": "Collier en acier",
                "description": "Collier en acier inoxydable pour homme.",
                "prix": 169.99,
                "quantite": 40,
                "image_url": "https://www.ninanina.fr/wp-content/uploads/2019/12/n3575-chaine-figaro-homme-acier-inoxydable-argent-50-cm-bijoux-colliers-hommes-en-ligne-ninanina.jpg"
            },
            {
                "id": "26",
                "titre": "Bracelet en cuir",
                "description": "Bracelet en cuir véritable pour homme.",
                "prix": 229.99,
                "quantite": 50,
                "image_url": "https://www.lapetitecannoise.com/333-large_default/bracelet-homme-cuir-argent.jpg"
            },
            {
                "id": "27",
                "titre": "Montre élégante et rétro",
                "description": "Montre élégante, et rétro en cuir pour homme. ",
                "prix": 399.99,
                "quantite": 12,
                "image_url": "https://maison-fevre.fr/cdn/shop/products/bracelet-montre-retro-cuir-marron-homme-maison-fevre-fait-main_900x.jpg?v=1725021036"
            },
            {
                "id": "28",
                "titre": "Bague en argent",
                "description": "Bague en argent 925 pour homme.",
                "prix": 780.99,
                "quantite": 20,
                "image_url": "https://itsara.net/cdn/shop/products/bague-homme-en-argent-ethnique-n027p1_Itsara_bijoux_2048x.jpg?v=1737535078"
            },
            {
                "id": "29",
                "titre": "Collier en acier",
                "description": "Collier en acier inoxydable pour homme.",
                "prix": 494.99,
                "quantite": 40,
                "image_url": "https://www.ninanina.fr/wp-content/uploads/2019/12/n3575-chaine-figaro-homme-acier-inoxydable-argent-50-cm-bijoux-colliers-hommes-en-ligne-ninanina.jpg"
            },
            {
                "id": "30",
                "titre": "Bague en or",
                "description": "Bague en or massif, dans un style à la fois moderne et contemporain.",
                "prix": 129.99,
                "quantite": 20,
                "image_url": "https://cdn-media.glamira.com/media/product/newgeneration/view/1/sku/8381feratibes/alloycolour/yellow.jpg"
            },
            {
                "id": "31",
                "titre": "Bague en argent",
                "description": "Bague en argent 925 pour homme.",
                "prix": 179.99,
                "quantite": 20,
                "image_url": "https://itsara.net/cdn/shop/products/bague-homme-en-argent-ethnique-n027p1_Itsara_bijoux_2048x.jpg?v=1737535078"
            },
        ]
        db.products.insert_many(products)
        print("Données de test pour 'products' insérées.")

    if db.users.count_documents({}) == 0:
        users = [
            {
                "firstname": "John",
                "name": "Doe",
                "password": "password123",
                "email": "john.doe@example.com"
            },
            {
                "firstname": "Jane",
                "name": "Doe",
                "password": "pas88opfi3",
                "email": "jane.doe@example.com"
            },
            {
                "firstname": "Marcus",
                "name": "Lovis",
                "password": "9:W5fx!E83iCf)",
                "email": "marcus.lovis@example.com"
            },
        ]
        db.users.insert_many(users)
        print("Données de test pour 'users' insérées.")


initialize_database()