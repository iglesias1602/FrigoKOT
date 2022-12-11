from datetime import datetime
from prettytable import PrettyTable
from main import *

if __name__ == "__main__":
    frigo = Frigo()
    while True:
        action = input("Tapez a pour ajouter, s pour supprimer\n")
        if action == 'a':
            aliment_nom = input("Ajoutez un aliment\n")
            if aliment_nom == 'stop':
                break
            aliment_type = input("Ajoutez le type de l'aliment\n")
            aliment_date = None
            while aliment_date is None:
                try:
                    date_str = input("Ajoutez la date de péremption en format dd/mm/yyyy \n")
                    aliment_date = datetime.strptime(date_str, '%d/%m/%Y')
                except ValueError:
                    print("Mauvais format de date")
            aliment = Aliment(aliment_nom, aliment_type, aliment_date)
            frigo.ajouter_aliment(aliment)
        else:
            aliment_nom = input("Supprimez un aliment\n")
            if aliment_nom == 'stop':
                break
            aliment = Aliment(aliment_nom, None, None)
            frigo.retirer_aliment(aliment)

        frigo.afficher_contenu()

