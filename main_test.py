from tabulate import tabulate
import pandas


class Fridge(object):
    """Creates food list objects
    for user to add it manually"""

    product_in_fridge = []

    def __init__(self, product=None, type_food=None, exp_date=None):
        self.product = product
        self.type_food = type_food
        self.exp_date = exp_date

    def add_item(self, product, type_food, exp_date):
        """Add product to the fridge."""
        if self.product in self.product_in_fridge:
            print(product + " is already in the fridge.\n")
        elif len(product) == 0:
            print('Error. Fill all the fields')

        else:
            self.product_in_fridge.append({'Product': product, 'Type': type_food, 'dateExp': exp_date})
            #print(f'\n{product} added.\n')


"""
if __name__ == "__main__":

    #gui.main()

    #my_frigo = Fridge("Frigo1")


    headers = ['Nom', 'Type du produit', 'Date de péremption']

    run = True

    print("Tapez 'stop' à tout moment pour arrêter le programme et afficher la liste des produits")

    while run:
        insert = input("Ajouter le produit\n")
        if insert == 'stop':
            break
        insert_type = input("Ajouter le type du produit\n")
        if insert_type == 'stop':
            break
        insert_exp_date = input("Ajouter la date de péremption en format dd/mm/yyyy \n")
        if insert_exp_date == 'stop':
            break
        if len(insert_exp_date) != 10:
            insert_exp_date = input("Veuillez introduire la date dans le format dd/mm/yyyy \n")


    my_frigo.add_item(insert, insert_type, insert_exp_date)

    info = my_frigo.product_in_fridge
    # print(info)


    df = pandas.DataFrame(info)

    if len(my_frigo.product_in_fridge) == 0:
        print(tabulate(df, headers=headers, tablefmt='double_grid'))
        print('Votre frigo est vide')
    else:
        print(tabulate(df, headers='keys', tablefmt='double_grid'))

    print(input('\nPress ENTER to exit'))
"""
