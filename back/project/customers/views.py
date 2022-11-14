import os
from flask import render_template, request, redirect, Blueprint
from project import db
from project.customers.models import Customers
from project.loans.models import Loans

"""
in this file we are defining the customers blue print setting & wrote all the end points that related to customers
"""

customers = Blueprint('customers', __name__, template_folder='templates')

#display customers:
@customers.route('/customers/', methods = ['GET'])
@customers.route('/customers/<id>')
def all_customers(id = -1):
    customers_res = []
    if int(id) == -1:
        for cust in Customers.query.all():
            customers_res.append({"customer_id":cust.customer_id, "customer_name":cust.customer_name, "city":cust.city, "age":cust.age})
        return customers_res
    if int(id) > -1: 
        cust = Customers.query.get(int(id))
        customers_res.append({"customer_id":cust.customer_id, "customer_name":cust.customer_name, "city":cust.city, "age":cust.age})
        return customers_res

# #search customer
# @customers.route('/search_customer', methods = ['POST'])
# def search_customer():
#     name = request.form['name']
#     customer = Customers.query.filter(Customers.customer_name == name or Customers.customer_name == name.lower()).first()
#     if customer is None: 
#         return redirect('/customers/')
#     return redirect(f'/customers/{customer.customer_id}')

#add Customer 
@customers.route("/add_customer/", methods=['POST', 'GET'])
def add_customer():
        customer_name = request.json["customer_name"]
        city = request.json["city"]
        age = request.json["age"]

        newCustomer= Customers(customer_name, city, age)
        db.session.add (newCustomer)
        db.session.commit()
        return 'customer added'

#delete customer
@customers.route("/delete_customer/<ind>", methods=['DELETE', 'GET'])
def del_customer(ind=-1):
        customer=Customers.query.get(int(ind))
        if customer:
            db.session.delete(customer)
            db.session.commit()
        return 'customer del'


#if customer has a loan cant del
#  loans = Loans.query.filter_by(returned= False)
#             for loan in loans:
#                 if loan.customer_id == customer.customer_id:
#                     return render_template ('all_customers.html', customers = Customers.query.all(), active_loan=True)