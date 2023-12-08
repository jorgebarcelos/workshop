from model.models import *


class DaoCategory:
    @classmethod
    def save(cls, category):
        with open('category.txt', 'a') as file:
            file.writelines(category)
            file.writelines('\n')

    
    @classmethod
    def read(cls):
        with open('category.txt') as file:
            cls.category = file.readlines()
        cls.category = list(lambda x: x.replace('\n', ''), cls.category)
        
        category_list = []

        for i in cls.category:
            category_list.append(Category(i))
        return category_list
        

class DaoSale:
    @classmethod
    def save(cls, sale: Sale):
        with open('sale.txt', 'a') as file:
            file.writelines(
                sale.sold_item.name + '|' + \
                    sale.sold_item.price + '|' + \
                        sale.sold_item.category + '|' + \
                            sale.seller + '|' + \
                                sale.buyer + '|'+ \
                                    str(sale.quantity_sold) + '|' + \
                                        sale.date
            )
            file.writelines('\n')

    @classmethod
    def read(cls):
        with open('sale.txt', 'r') as file:
            cls.sale = file.readlines()

        cls.sale = list(map(lambda x: x.replace('\n', ''), cls.sale))
        cls.sale = list(map(lambda x: x.split('|'), cls.sale))

        sale_list = []
        
        for i in cls.sale:
            sale_list.append(Sale(Products(i[0], i[1], i[2], i[3], i[4], i[5], i[6])))
        return sale_list
    

class DaoStock:
    @classmethod
    def save(cls, product: Products, quantity):
        with open('stock.txt', 'a') as file:
            file.writelines(
                product.name + '|' + \
                    product.price + '|' + \
                        product.category + '|' + \
                            str(quantity)
            )
            file.writelines('\n')


    @classmethod
    def read(cls):
        with open('stock.txt', 'r') as file:
            cls.stock = file.readlines()

        cls.stock = list(map(lambda x: x.replace('\n', ''), cls.stock))
        cls.stock = list(map(lambda x: x.split('|'), cls.stock))

        stock_list = []
        
        if len(cls.stock) > 0:
            for i in cls.stock:
                stock_list.append(Stock(Products(i[0], i[1], i[2], i[3])))
            return stock_list


class DaoSupplier:
    @classmethod
    def save(cls, supplier: Supplier):
        with open('supplier.txt', 'a') as file:
            file.writelines(
                supplier.name + '|' + \
                    supplier.cnpj + '|' + \
                        supplier.phone + '|' + \
                            supplier.category
            )
            file.writelines('\n')


    @classmethod
    def read(cls):
        with open('supplier.txt', 'r') as file:
            cls.supplier = file.readlines()

        cls.supplier = list(map(lambda x: x.replace('\n', ''), cls.supplier))
        cls.supplier = list(map(lambda x: x.split('|'), cls.supplier))

        supplier_list = []
        

        for i in cls.supplier:
            supplier_list.append(Supplier(i[0], i[1], i[2], i[3]))
        return supplier_list
    

    class DaoPerson:
        @classmethod
        def save(cls, persons: Person):
            with open('clients.txt', 'a') as file:
                file.writelines(
                    persons.name + '|' + \
                        persons.phone + '|' + \
                            persons.cpf + '|' + \
                                persons.email + '|' + \
                                    persons.address
                )
                file.writelines('\n')


        @classmethod
        def read(cls):
            with open('clients.txt', 'r') as file:
                cls.clients = file.readlines()

            cls.clients = list(map(lambda x: x.replace('\n', ''), cls.clients))
            cls.clients = list(map(lambda x: x.split('|'), cls.clients))

            clients_list = []
            

            for i in cls.clients:
                clients_list.append(Person(i[0], i[1], i[2], i[3], i[4]))
            return clients_list
        

class DaoEmployee:
    @classmethod
    def save(cls, employee: Employee):
        with open('employee.txt', 'a') as file:
            file.writelines(
                employee.employee_id + '|' + \
                    employee.name + '|' + \
                        employee.phone + '|' + \
                            employee.cpf + '|' + \
                                employee.email + '|' + \
                                    employee.address
            )
            file.writelines('\n')


    @classmethod
    def read(cls):
        with open('employee.txt', 'r') as file:
            cls.employee = file.readlines()

        cls.employee = list(map(lambda x: x.replace('\n', ''), cls.employee))
        cls.employee = list(map(lambda x: x.split('|'), cls.employee))

        employee_list = []
        

        for i in cls.employee:
            employee_list.append(Employee(i[0], i[1], i[2], i[3], i[4], i[5]))
        return employee_list