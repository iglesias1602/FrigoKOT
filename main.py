from datetime import datetime
from prettytable import PrettyTable


class Aliment:
    def __init__(self, nom, type_, date_peremption):
        self.__nom = nom
        self.__type_ = type_
        self.__date_peremption = date_peremption

    @property
    def nom(self):
        return self.__nom

    @property
    def type(self):
        return self.__type_

    @property
    def date_peremption(self):
        return self.__date_peremption


class Frigo:
    def __init__(self):
        self.__aliment_frigo = {}

    @property
    def aliment_frigo(self):
        return self.__aliment_frigo

    def ajouter_aliment(self, aliment):
        """Ajoute un aliment dans le frigo"""

        if aliment.nom not in self.aliment_frigo:
            self.__aliment_frigo[aliment.nom] = aliment

    def retirer_aliment(self, aliment):
        """Retire un aliment du frigo"""

        self.__aliment_frigo.pop(aliment.nom)

    def afficher_contenu(self):
        mon_tableau = PrettyTable(['Nom', 'Type du produit', 'Date de péremption'])
        for a in self.__aliment_frigo.values():
            mon_tableau.add_row((a.nom, a.type, a.date_peremption.strftime('%d/%m/%Y')))
        print(mon_tableau)


class Recette:
    def __init__(self, nom, description):
        self.__nom = nom
        self.__description = description

    @property
    def nom(self):
        return self.__nom

    @property
    def description(self):
        return self.__description


class Etudiant:
    def __init__(self, prenom, nom, age):
        self.__prenom = prenom
        self.__nom = nom
        self.__age = age
        self.__allergique_a = []

    @property
    def prenom(self):
        return self.__prenom

    @property
    def nom(self):
        return self.__nom

    @property
    def age(self):
        return self.__age

    @property
    def allergique_a(self):
        return self.__allergique_a

    def __eq__(self, other):
        """Overloading of the == operator for Etudiant"""
        if isinstance(other, Etudiant):
            return self.prenom == other.prenom and self.nom == other.nom
        else:
            raise TypeError

    def ajouter_allergene(self, allergene):
        """ajoute un allergène pour un étudiant donné"""

        if allergene not in self.__allergique_a:
            self.__allergique_a.append(allergene)

    def retirer_allergene(self, allergene):
        """retire un allergène pour un étudiant donné"""

        for i in self.__allergique_a:
            if i == allergene:
                self.__allergique_a.remove(allergene)


class Allergene:
    def __init__(self, nom):
        self.__nom = nom

    @property
    def nom(self):
        return self.__nom

    def __eq__(self, other):
        """Overloading of the == operator for Allergene"""

        if isinstance(other, Allergene):
            return self.nom == other.nom
        else:
            raise TypeError


class Repas:
    def __init__(self, date_repas, type_repas):
        self.__date_repas = date_repas
        self.__type_repas = type_repas
        self.__participants = []

    @property
    def date_repas(self):
        return self.__date_repas

    @property
    def type_repas(self):
        return self.__type_repas

    @property
    def participants(self):
        return self.__participants

    def ajouter_participant(self, participant):
        """ajoute un allergène pour un étudiant donné"""

        if participant not in self.__participants:
            self.__participants.append(participant)

    def retirer_participant(self, participant):
        """retire un allergène pour un étudiant donné"""

        self.__participants.remove(participant)