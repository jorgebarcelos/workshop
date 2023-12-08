from model.models import *
from dao.daos import *

class ControllerCategory:
    def create_category(self, new_category):
        exist = False
        dao_category = DaoCategory.read()

        for i in dao_category:
            if i.category == new_category:
                exist = True
        
        if not exist:
            DaoCategory.save(new_category)
            print("Categoria criaada com sucesso!")
        else:
            print("A categoria em questão já existe")