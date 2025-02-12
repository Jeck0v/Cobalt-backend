class User:
    def __init__(self, firstname, name, password, email):
        self.firstname = firstname
        self.name = name
        self.password = password
        self.email = email

    def to_dict(self):
        """
        Convertit l'objet User en dictionnaire pour MongoDB.
        """
        return {
            "firstname": self.firstname,
            "name": self.name,
            "password": self.password,
            "email": self.email
        }