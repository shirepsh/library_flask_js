from project import db,app

#create the customers table
class Customers(db.Model):
    customer_id = db.Column(db.Integer, primary_key = True)
    customer_name = db.Column(db.String(15), nullable= False)
    city = db.Column(db.String(15), nullable= False)
    age = db.Column (db.Integer, nullable= False)
    # loan = db.relationship('Loans', backref='customers', lazy=True)


    # initialise 
    def __init__(self, customer_name, city, age):
        self.customer_name = customer_name
        self.city = city
        self.age = age
        
