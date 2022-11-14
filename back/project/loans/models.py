from project import db,app

#create the loans table
class Loans(db.Model):
    loan_id = db.Column (db.Integer, primary_key = True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'))
    loan_date = db.Column(db.String(15), nullable= False)
    return_date = db.Column(db.String(15), nullable= True)

    # initialise
    def __init__(self, customer_id, book_id, loan_date, return_date): 
        self.customer_id = customer_id
        self.book_id = book_id
        self.loan_date = loan_date
        self.return_date = return_date
    