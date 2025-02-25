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
        IA
        """
        requete = request.json.get('demande')

        descriptions = [doc["description"] for doc in db.products.find({}, {"description": 1})]

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
            resultat = "Voici lequel de nos bijoux correspondrait le mieux à votre demande : " + descriptions[BestMatch]
            return {'resultat': resultat}, 200
        else:
            return {'resultat': 'Malheureusement, les précisions actuelles ne sont pas suffisantes pour effectuer une recherche appropriée. Peux-tu me donner de nouvelles précisions ?'}, 404

def init_ia_routes(api):
    api.add_namespace(ia_ns)