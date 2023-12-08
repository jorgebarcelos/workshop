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

    
    def delete_category(self, remove_category):
        dao_category = DaoCategory.read()
        category = list(filter(lambda x: x.category == remove_category, dao_category))

        if len(category) <= 0:
            print("A categoria não existe")
        else:
            for i in range(len(dao_category)):
                if dao_category[i] == remove_category:
                    del dao_category[i]
                    break

            print("Categoria removida com sucesso!")

            with open('category.txt', 'w') as file:
                for i in dao_category:
                    file.writelines(i.category)
                    file.writelines('\n')