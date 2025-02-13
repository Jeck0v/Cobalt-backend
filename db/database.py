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
    Initialise la base de données en créant les collections nécessaires si elles n'existent pas déjà.
    """
    # Liste des collections nécessaires
    required_collections = ['users', 'products', 'orders']
    existing_collections = db.list_collection_names()
    for collection in required_collections:
        if collection not in existing_collections:
            db.create_collection(collection)
            print(f"Collection '{collection}' créée.")
        else:
            print(f"Collection '{collection}' existe déjà.")


# Appeler la fonction d'initialisation lors de l'importation du module
initialize_database()