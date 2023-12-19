import pretty_errors
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
    

    def change_category(self, category_change, category_changed):
        dao_category = DaoCategory.read()

        category_list = list(filter(lambda x: x.category == category_change, dao_category))

        if len(category_list) > 0:
            data_category = list(filter(lambda x: x.category == category_changed))
            if len(data_category) == 0:
                data_category_changed = list(map(lambda x: Category(category_changed) if(x.category == category_change) else(x), dao_category))
                print("Categoria alterada com sucesso")
            else:
                print("A categoria que deseja alterar já existe")
        else:
            print("A categoria que deseja alterar não existe")
        
        with open("category.txt", "w") as file:
            for i in data_category_changed:
                file.writelines(i.category)
                file.writelines("\n")


    def show_category(self):
        categories = DaoCategory.read()

        if len(categories) == 0:
            print("Categoria vazia")
        else:
            for i in categories:
                print(f'Categoria: {i.category}')

