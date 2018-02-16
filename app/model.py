from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), index = True)
    price = db.Column(db.Integer, index = True)
    cpufrequency = db.Column(db.Integer)
    cpu = db.Column(db.String(50))
    ram = db.Column(db.Integer)
    hdd = db.Column(db.Integer)
    imgpath = db.Column(db.String(200))

    def __repr__(self):
        return '<Product {}>'.format(self.name)