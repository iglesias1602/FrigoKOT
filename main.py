from prettytable import PrettyTable


class Fridge(object):

    """Creates food list objects
    for user to add it manually"""

    product_in_fridge = {}

    def __init__(self, food_name=None):
        self.food_name = food_name

    def add_item(self, product, type_food, exp_date):
        """Add product to the fridge."""
        if not product in self.product_in_fridge:
            self.product_in_fridge[product] = type_food, exp_date
            print(f'\n{product} added.\n')
        else:
            print(product + " is already in the fridge.\n")


my_frigo = Fridge("Frigo1")
myTable = PrettyTable(['Nom', 'Type du produit', 'Date de péremption'])

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


food_list = list(my_frigo.product_in_fridge.items())

for product in food_list:
    myTable.add_row((product[0], product[1][0], product[1][1]))

print(myTable)

if len(my_frigo.product_in_fridge) == 0:
    print('Votre frigo est vide')

print(input('\nPress ENTER to exit'))