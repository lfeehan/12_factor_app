from flask_mongoalchemy import MongoAlchemy
db = MongoAlchemy()

class Filter(db.Document):
    name = db.StringField()
    type = db.StringField()
    goal = db.StringField()
    value = db.IntField()


class User(db.Document):
    name = db.StringField()
    wallet = db.StringField()
    balance =  db.FloatField()
    filters = db.ListField(db.DocumentField(Filter))

    def __repr__(self):
        return '<User {0}>'.format(self.name)

    def serialize(self):
        """
        Custom method used within api to serialize database objects into
        JSON.
        """
        return {
            'name': self.name,
            'wallet': self.wallet,
            'balance': self.balance
        }
