from flask import request
from flask_restx import Namespace, Resource, fields
from db.database import db
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.stats import pearsonr

ia_ns = Namespace('ia', description='Opérations liées à l\'utilisation de l\'IA')

ia_model = ia_ns.model('IA', {
    'demande': fields.String(required=True, description='Demande de l\'utilisateur')
})
@ia_ns.route('/search')
class IA(Resource):
    @ia_ns.expect(ia_model)
    def post(self):
        """
        IA pour la recommandation de produits
        """
        requete = request.json.get('demande')

        products = list(db.products.find({}, {"description": 1, "titre": 1, "id": 1}))
        descriptions = [doc["description"] for doc in products]
        titres = [doc["titre"] for doc in products]
        product_ids = [doc["id"] for doc in products]

        if not descriptions:
            return {'resultat': '<p>Aucun produit disponible pour le moment.</p>'}, 404

        ensemble = [requete] + descriptions

        vect = TfidfVectorizer()
        tfidf_analyse = vect.fit_transform(ensemble).toarray()

        demande_tfidf = tfidf_analyse[0]
        description_tfidf = tfidf_analyse[1:]
        Newcorrelation = 0

        BestMatch = None

        for id, doc in enumerate(description_tfidf):
            correlation = pearsonr(demande_tfidf, doc)
            if correlation[0] > Newcorrelation:
                Newcorrelation = correlation[0]
                BestMatch = id

        if BestMatch is not None:
            product_id = product_ids[BestMatch]
            product_titre = titres[BestMatch]

            product_link = f"/products/{product_id}"

            resultat = f'Here\'s which of our jewels would best suit your request: {product_link}Click here to view the product'
            title = f'{product_titre}'
            return {'resultat': resultat, 'title': title, product_link: product_link}, 200
        else:
            return {'resultat': '<p>Unfortunately, the current details are not sufficient to carry out a proper search. Can you give me some more details?</p>'}, 404
def init_ia_routes(api):
    api.add_namespace(ia_ns)