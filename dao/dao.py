from models.models import *


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