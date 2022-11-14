from project import db,app

#create the books table
class Books(db.Model):
    book_id = db.Column(db.Integer, primary_key = True)
    book_name = db.Column(db.String(15), nullable= False)
    author = db.Column(db.String(15), nullable= False)
    year_published = db.Column (db.Integer, nullable= False)
    book_type = db.Column(db.Integer,nullable= False) 
    # loan= db.relationship('Loans', backref ='books', lazy=True)

    # initialise 
    def __init__(self, book_name, author, year_published, book_type):
        self.book_name = book_name
        self.author = author
        self.year_published = year_published
        self.book_type = book_type

