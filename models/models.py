from datetime import datetime

class Category:
    def __init__(self, category ):
        self.category = category


class Products:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category


class Stock:
    def __init__(self, product: Products, quantity):
        self.product = product
        self.quantity = quantity


class Sale:
    def __init__(self, sold_item: Products, seller, buyer, quantity_sold, date = datetime.now()):
        self.sold_item = sold_item
        self.seller = seller
        self.buyer = buyer
        self.quantity_sold = quantity_sold
        self.date = date


class Supplier:
    def __init__(self, name, cnpj, phone, category):
        self.name = name
        self.cnpj = cnpj
        self.phone = phone
        self.category = category


class Person:
    def __init__(self, name, phone, cpf, email, address):
        self.name = name
        self.phone = phone
        self.cpf = cpf
        self.email = email
        self.address = address


class Employee(Person):
    def __init__(self, employee_id, name, phone, cpf, email, address):
        self.employee_id = employee_id
        super(Employee, self).__init__(name, phone, cpf, email, address)

