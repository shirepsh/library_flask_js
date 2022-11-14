import datetime
from flask import render_template, request, redirect, Blueprint
from project import db
from project.customers.models import Customers
from project.loans.models import Loans
from project.books.models import Books

"""
in this file we are defining the loans blue print setting & wrote all the end points that related to loans
"""

loans = Blueprint('loans', __name__, template_folder='templates')

#function to use at add loan
def max_loan(book, loan_date):
    delta_type1 = datetime.timedelta(days= 10)
    delta_type2 = datetime.timedelta(days=5)
    delta_type3 = datetime.timedelta(days= 2)

    if book.book_type == 1: 
        return loan_date + delta_type1
    if book.book_type == 2: 
        return loan_date + delta_type2
    if book.book_type == 3: 
        return loan_date + delta_type3

# def book_avilable(book_id, loans):
#     for loan in loans:
#         if loan.book_id == int(book_id):
#             return False
#     return True

#display loans 
#serach loan by book id!!!
@loans.route('/loans/' , methods = ['GET'])
@loans.route('/loans/<book_id>')
def all_loans(book_id= -1):
    loans_res = []
    if int(book_id) == -1: 
        for loan in Loans.query.all():
            loans_res.append({"loan_id":loan.loan_id, "customer_id":loan.customer_id, "book_id":loan.book_id, "loan_date":loan.loan_date, "return_date":loan.return_date})
        return loans_res

    loan = Loans.query.filter_by(book_id=book_id)
    if loan:
        loans_res.append({"loan_id":loan.loan_id, "customer_id":loan.customer_id, "book_id":loan.book_id, "loan_date":loan.loan_date, "return_date":loan.return_date})
        return loans_res
    
#loan a book (add loan) 
@loans.route("/add_loan/", methods=['POST', 'GET'])
def add_loan():
    customer_id = request.json["customer_id"]
    book_id = request.json["book_id"]
    loan_date = datetime.date.today()
    res =Books.query.get(int(book_id))
    return_date = max_loan(res, loan_date)

    new_loan = Loans(customer_id, book_id, loan_date, return_date)
    db.session.add(new_loan)
    db.session.commit()

    return 'loan added' 

# #return book (update the returned value) 
# @loans.route("/return_book/<ind>", methods=['PUT', 'GET'])
# def upd_returned(ind=-1):
#     if int(ind) > -1:
#         loan=Loans.query.get(int(ind))
#         loan.returned = True
#         db.session.commit()
#     return render_template("return_book(loan).html", loan=loan)
            
# #late loans
# @loans.route("/late_loans/", methods=['GET']) 
# def display_late_loans():
#     late_loans = []
#     late_time = []
#     active_loans = Loans.query.filter_by(returned= False)
#     for loan in active_loans:
#         if loan.return_date < datetime.date.today():
#             late_loans.append(loan)
#             late_time.append((datetime.date.today()-loan.return_date).days)
#     return render_template ("late_loans.html", late_loans=late_loans, late_time= late_time)

#delete loan
@loans.route("/delete_loan/<ind>", methods=['DELETE' , 'GET'])
def del_loan(ind=-1):
    loan=Loans.query.get(int(ind))
    if loan:
            db.session.delete(loan)
            db.session.commit()
            return 'loan del'
