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
    Init bdd
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
            },
            {
                "id": "7",
                "titre": "Brown Leather Bracelet",
                "description": "Brown leather bracelet for men.",
                "prix": 29.99,
                "quantite": 50,
                "image_url": "https://www.lapetitecannoise.com/333-large_default/bracelet-homme-cuir-argent.jpg",
                "categorie": "Bracelets"
            },
            {
                "id": "8",
                "titre": "Elegant and Retro Watch",
                "description": "Elegant and retro leather watch for men.",
                "prix": 199.99,
                "quantite": 12,
                "image_url": "https://maison-fevre.fr/cdn/shop/products/bracelet-montre-retro-cuir-marron-homme-maison-fevre-fait-main_900x.jpg?v=1725021036",
                "categorie": "Watches"
            },
            {
                "id": "9",
                "titre": "Silver Ring",
                "description": "925 silver ring for men.",
                "prix": 49.99,
                "quantite": 20,
                "image_url": "https://itsara.net/cdn/shop/products/bague-homme-en-argent-ethnique-n027p1_Itsara_bijoux_2048x.jpg?v=1737535078",
                "categorie": "Rings"
            },
            {
                "id": "10",
                "titre": "Stainless Steel Necklace",
                "description": "Stainless steel necklace for men.",
                "prix": 49.99,
                "quantite": 40,
                "image_url": "https://www.ninanina.fr/wp-content/uploads/2019/12/n3575-chaine-figaro-homme-acier-inoxydable-argent-50-cm-bijoux-colliers-hommes-en-ligne-ninanina.jpg",
                "categorie": "Necklaces"
            },
            {
                "id": "11",
                "titre": "Cobalt Pendant",
                "description": "Elegant Cobalt pendant for men.",
                "prix": 299.99,
                "quantite": 15,
                "image_url": "https://caratsutra.in/cdn/shop/products/IMG_20220216_213558.jpg?v=1654097796",
                "categorie": "Pendants"
            },
            {
                "id": "12",
                "titre": "Gold Hoop Earrings",
                "description": "Stylish gold hoop earrings for men.",
                "prix": 179.99,
                "quantite": 30,
                "image_url": "https://www.gld.com/cdn/shop/products/micro-double-row-huggie-earrings-in-yellow-gold-gld-men-3_375x375_crop_center@2x.jpg?v=1680691085%20x2,%20//www.gld.com/cdn/shop/products/micro-double-row-huggie-earrings-in-yellow-gold-gld-men-3_375x375_crop_center.jpg?v=1680691085%20x1",
                "categorie": "Earrings"
            },
            {
                "id": "13",
                "titre": "Gold Hoop Earrings",
                "description": "Stylish gold hoop earrings for men.",
                "prix": 179.99,
                "quantite": 30,
                "image_url": "https://www.gld.com/cdn/shop/products/micro-double-row-huggie-earrings-in-yellow-gold-gld-men-3_375x375_crop_center@2x.jpg?v=1680691085%20x2,%20//www.gld.com/cdn/shop/products/micro-double-row-huggie-earrings-in-yellow-gold-gld-men-3_375x375_crop_center.jpg?v=1680691085%20x1",
                "categorie": "Earrings"
            },
            {
                "id": "14",
                "titre": "Luxury Leather Bracelet",
                "description": "Brown leather bracelet for men.",
                "prix": 89.99,
                "quantite": 30,
                "image_url": "https://www.lapetitecannoise.com/333-large_default/bracelet-homme-cuir-argent.jpg",
                "categorie": "Bracelets"
            },
            {
                "id": "15",
                "titre": "Elegant and Retro Watch",
                "description": "Elegant and retro leather watch for men.",
                "prix": 69.99,
                "quantite": 12,
                "image_url": "https://maison-fevre.fr/cdn/shop/products/bracelet-montre-retro-cuir-marron-homme-maison-fevre-fait-main_900x.jpg?v=1725021036",
                "categorie": "Watches"
            },
            {
                "id": "16",
                "titre": "Silver Ring",
                "description": "925 silver ring for men.",
                "prix": 79.99,
                "quantite": 20,
                "image_url": "https://itsara.net/cdn/shop/products/bague-homme-en-argent-ethnique-n027p1_Itsara_bijoux_2048x.jpg?v=1737535078",
                "categorie": "Rings"
            },
            {
                "id": "17",
                "titre": "Stainless Steel Necklace",
                "description": "Stainless steel necklace for men.",
                "prix": 99.99,
                "quantite": 40,
                "image_url": "https://www.ninanina.fr/wp-content/uploads/2019/12/n3575-chaine-figaro-homme-acier-inoxydable-argent-50-cm-bijoux-colliers-hommes-en-ligne-ninanina.jpg",
                "categorie": "Necklaces"
            },
            {
                "id": "18",
                "titre": "Cobalt Pendant",
                "description": "Elegant Cobalt pendant for men.",
                "prix": 189.99,
                "quantite": 15,
                "image_url": "https://caratsutra.in/cdn/shop/products/IMG_20220216_213558.jpg?v=1654097796",
                "categorie": "Pendants"
            },
            {
                "id": "19",
                "titre": "Gold Hoop Earrings",
                "description": "Stylish gold hoop earrings for men.",
                "prix": 179.99,
                "quantite": 30,
                "image_url": "https://www.gld.com/cdn/shop/products/micro-double-row-huggie-earrings-in-yellow-gold-gld-men-3_375x375_crop_center@2x.jpg?v=1680691085%20x2,%20//www.gld.com/cdn/shop/products/micro-double-row-huggie-earrings-in-yellow-gold-gld-men-3_375x375_crop_center.jpg?v=1680691085%20x1",
                "categorie": "Earrings"
            },
            {
                "id": "20",
                "titre": "Stainless Steel Necklace",
                "description": "Stainless steel necklace for men.",
                "prix": 210.99,
                "quantite": 40,
                "image_url": "https://www.ninanina.fr/wp-content/uploads/2019/12/n3575-chaine-figaro-homme-acier-inoxydable-argent-50-cm-bijoux-colliers-hommes-en-ligne-ninanina.jpg",
                "categorie": "Necklaces"
            },
            {
                "id": "21",
                "titre": "Cobalt Pendant",
                "description": "Elegant Cobalt pendant for men.",
                "prix": 430.99,
                "quantite": 15,
                "image_url": "https://caratsutra.in/cdn/shop/products/IMG_20220216_213558.jpg?v=1654097796",
                "categorie": "Pendants"
            },
            {
                "id": "22",
                "titre": "Cobalt Pendant",
                "description": "Elegant Cobalt pendant for men.",
                "prix": 245.99,
                "quantite": 15,
                "image_url": "https://caratsutra.in/cdn/shop/products/IMG_20220216_213558.jpg?v=1654097796",
                "categorie": "Pendants"
            },
            {
                "id": "23",
                "titre": "Elegant and Retro Watch",
                "description": "Elegant and retro leather watch for men.",
                "prix": 185.99,
                "quantite": 12,
                "image_url": "https://maison-fevre.fr/cdn/shop/products/bracelet-montre-retro-cuir-marron-homme-maison-fevre-fait-main_900x.jpg?v=1725021036",
                "categorie": "Watches"
            },
            {
                "id": "24",
                "titre": "Elegant and Retro Watch",
                "description": "Elegant and retro leather watch for men.",
                "prix": 99.99,
                "quantite": 12,
                "image_url": "https://maison-fevre.fr/cdn/shop/products/bracelet-montre-retro-cuir-marron-homme-maison-fevre-fait-main_900x.jpg?v=1725021036",
                "categorie": "Watches"
            },
            {
                "id": "25",
                "titre": "Elegant and Retro Watch",
                "description": "Elegant and retro leather watch for men.",
                "prix": 299.99,
                "quantite": 12,
                "image_url": "https://maison-fevre.fr/cdn/shop/products/bracelet-montre-retro-cuir-marron-homme-maison-fevre-fait-main_900x.jpg?v=1725021036",
                "categorie": "Watches"
            },
            {
                "id": "24",
                "titre": "Elegant and Retro Watch",
                "description": "Elegant and retro leather watch for men.",
                "prix": 499.99,
                "quantite": 12,
                "image_url": "https://maison-fevre.fr/cdn/shop/products/bracelet-montre-retro-cuir-marron-homme-maison-fevre-fait-main_900x.jpg?v=1725021036",
                "categorie": "Watches"
            },
            {
                "id": "26",
                "titre": "Elegant and Retro Watch",
                "description": "Elegant and retro leather watch for men.",
                "prix": 599.99,
                "quantite": 12,
                "image_url": "https://maison-fevre.fr/cdn/shop/products/bracelet-montre-retro-cuir-marron-homme-maison-fevre-fait-main_900x.jpg?v=1725021036",
                "categorie": "Watches"
            },
            {
                "id": "27",
                "titre": "Silver Ring",
                "description": "925 silver ring for men.",
                "prix": 449.99,
                "quantite": 20,
                "image_url": "https://itsara.net/cdn/shop/products/bague-homme-en-argent-ethnique-n027p1_Itsara_bijoux_2048x.jpg?v=1737535078",
                "categorie": "Rings"
            },
            {
                "id": "28",
                "titre": "Silver Ring",
                "description": "925 silver ring for men.",
                "prix": 129.99,
                "quantite": 20,
                "image_url": "https://itsara.net/cdn/shop/products/bague-homme-en-argent-ethnique-n027p1_Itsara_bijoux_2048x.jpg?v=1737535078",
                "categorie": "Rings"
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