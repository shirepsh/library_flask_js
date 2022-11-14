from flask import Blueprint, redirect, render_template, request

from project import db
from project.books.models import Books
from project.loans.models import Loans

"""
in this file we are defining the books blue print setting & wrote all the end points that related to books
"""
books = Blueprint('books', __name__, template_folder='templates', static_folder='static')

#display books:
@books.route('/books/', methods = ['GET'])
@books.route('/books/<id>')
def all_books(id = -1):
    book_res =[]
    if int(id) == -1:
        for book in Books.query.all():
            book_res.append({"book_id":book.book_id, "book_name":book.book_name, "author":book.author, "year_published":book.year_published, "book_type":book.book_type})
        return book_res
    if int(id) > -1: 
        book = Books.query.get(int(id))
        book_res.append({"book_id":book.book_id, "book_name":book.book_name, "author":book.author, "year_published":book.year_published, "book_type":book.book_type})
        return book_res

# #search for a book
# @books.route('/search_book', methods = ['POST'])
# def search_book():
#     name = request.form['name']
#     book = Books.query.filter(Books.book_name == name or Books.book_name == name.lower()).first()
#     if book is None: 
#         return redirect('/books/')
#     return redirect(f'/books/{book.book_id}')

#add book 
@books.route("/add_book/", methods=['POST', 'GET'])
def add_book():
        book_name = request.json["book_name"]
        author = request.json["author"]
        year_published = request.json["year_published"]
        book_type = request.json["book_type"]
    

        newBook= Books(book_name, author, year_published, book_type)
        db.session.add (newBook)
        db.session.commit()
        return 'book added'

#delete book
@books.route("/delete_book/<ind>", methods=['DELETE', 'GET'])
def del_book(ind=-1):
        book=Books.query.get(int(ind))
        if book:
            db.session.delete(book)
            db.session.commit()
        return 'del'

#if book is on loan cant del
   # loans = Loans.query.filter_by(returned= False)
            # for loan in loans:
            #     if loan.book_id == book.book_id:
            #         return 'cant del'