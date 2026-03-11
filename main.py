# mon_tuple = (1, 2, 3, 4, 5)
# print("Le contenu du tuple est :", mon_tuple)
# print(mon_tuple[2])  # Affiche le troisième élément du tuple
# mon_tuple_bis = ("cinq", "six")
# mon_nouveau_tuple = mon_tuple + mon_tuple_bis
# print("Le nouveau tuple est :", mon_nouveau_tuple)
# print(5 in mon_nouveau_tuple)  # Vérifie si 5 est dans le nouveau tuple
# print(len(mon_nouveau_tuple))  # Affiche la longueur du nouveau tuple
# fruits = ["Pomme", "Banane", "Orange"]
# fruits.append("Kiwi")
# print("La liste des fruits est :", fruits)
# fruits.remove("Orange")
# print("La liste des fruits est :", fruits)
# fruits[1] = "ananas"
# print("La liste des fruits est :", fruits)
# print(len(fruits))
# fruits.sort()
# print("La liste des fruits triée est :", fruits)
# fruits.sort(key=str.lower)
# print("La liste des fruits triée en ordre décroissant est :", fruits)
# nouvelle_campagne = {
#     "responsable_de_campagne" : "Jeanne D'arc",
#     "nom_de_campagne" : "Campagne nous aimons les chiens",
#     "date_de_debut" : "2024-06-01",
#     "date_de_fin" : "2024-12-31",
#     "budget" : 50000,
#     "Influenceurs importants" : ["@influenceur1", "@influenceur2", "@influenceur3"]
# }
# print("Détails de la campagne :", nouvelle_campagne)
# print("Nom de la campagne", nouvelle_campagne["nom_de_campagne"])
# taux_de_conversion = {}
# taux_de_conversion["Facebook"] = 0.05
# taux_de_conversion["Instagram"] = 0.07
# print("Taux de conversion :", taux_de_conversion)# Manipulation de tuples
# taux_de_conversion = dict()
# taux_de_conversion['facebook'] = 3.4
# taux_de_conversion['instagram'] = 1.2
# print("Taux de conversion :", taux_de_conversion)
# print("Taux de conversion Facebook :", taux_de_conversion['facebook'])

# infos_labradoodle = {
#     "poids" : "13kg à 16kg",
#     "origine": "Etats-Unis",
# }

# print("Infos labradoodle :", infos_labradoodle)
# infos_labradoodle["nom scientifique"] = "Canis lupus familiaris"
# print("Infos labradoodle mises à jour :", infos_labradoodle)
# infos_labradoodle["poids"] = "14kg à 18kg"
# print("Infos labradoodle mises à jour :", infos_labradoodle)

# del infos_labradoodle["origine"]
# print("Infos labradoodle après suppression de l'origine :", infos_labradoodle)
# print(infos_labradoodle.keys())
# print(infos_labradoodle.values())
# print(infos_labradoodle.items())
# print(infos_labradoodle.get("poids"))
# print("poids" in infos_labradoodle)
# print("taille" in infos_labradoodle)
# print(infos_labradoodle.get("taille"))
# infos_labradoodle.pop("poids")
# print("Infos labradoodle après suppression du poids :", infos_labradoodle)
# infos_labradoodle.clear()
# print("Infos labradoodle après vidage du dictionnaire :", infos_labradoodle)

# fruits = {
#     "pomme": "rouge",
#     "banane": "jaune",
#     "orange" : "orange"
# }

# fruits["kiwi"] = "vert"
# print(fruits)
# couleur_banane = fruits["banane"]
# fruits["pomme"] = "vert"
# print(fruits)
# fruits.pop("banane")
# print(fruits)
# print(fruits.keys())
# print(fruits.values())

# print("Entrer les 2 nombres à manipuler :")

# nombre1 = input("Nombre 1 : ")
# nombre2 = input("Nombre 2 : ")

# if not nombre1.isnumeric() or not nombre2.isnumeric():
#     print("Veuillez entrer des entiers valides.")
#     raise SystemExit("Fin du programme.")
# else:
#     print("Les nombres entrés sont :", nombre1, "et", nombre2)
#     nombre1 = int(nombre1)
#     nombre2 = int(nombre2)

#     print("Entrer l'opération à effectuer (addition, soustraction, multiplication, division) :")

#     operation = input("Opération : ")

#     if not operation in ["+", "-", "*", "/"]:
#         raise SystemExit("Opération non valide. Fin du programme.")
#     else:
#         print("L'opération choisie est :", operation)
#         match operation:
#             case "+":
#                 resultat = nombre1 + nombre2
#                 print("Le résultat de l'addition est :", resultat)
#             case "-":
#                 resultat = nombre1 - nombre2
#                 print("Le résultat de la soustraction est :", resultat)
#             case "*":
#                 resultat = nombre1 * nombre2
#                 print("Le résultat de la multiplication est :", resultat)
#             case "/":
#                 if nombre2 == 0:
#                     raise SystemExit("Division par zéro impossible. Fin du programme.")
#                 else:
#                     resultat = nombre1 / nombre2
#                     print("Le résultat de la division est :", round(resultat, 2))

# races_de_chien = ["golden retriever", "chihuahua", "terrier", "carlin"]

# for chien in races_de_chien:
#     print(chien)
# for x in range(5):
#     print(x)
# for y in range(2, 10):
#     print(y)

# capacite_maximale = 10
# capacite_actuelle = 3

# while capacite_actuelle < capacite_maximale:
#     print("Capacité actuelle :", capacite_actuelle)
#     capacite_actuelle += 1

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# liste = [1, 2, 3, 4, 5]

# for nombre in liste:
#     if nombre == 3:
#         continue
#     print(nombre)

# print("Saisissez une liste de nombres séparés par des virgules :")

# saisie = input("Nombres : ")
# nombres = saisie.split(",")
# print("Liste des nombres :", nombres)
# liste_nombres = []
# for nombre in nombres:
#         liste_nombres.append(int(nombre))
# print("Liste des nombres valides :", liste_nombres)
# somme = sum(liste_nombres)
# print("La somme des nombres est :", somme)  

# moyenne = somme / len(liste_nombres)
# print("La moyenne des nombres est :", round(moyenne, 2))

# nombre_de_nombres_superieurs_a_moyenne = 0
# for nombre in liste_nombres:
#     if nombre > moyenne:
#         nombre_de_nombres_superieurs_a_moyenne += 1
# print("Nombre de nombres supérieurs à la moyenne :", nombre_de_nombres_superieurs_a_moyenne)

# def salaire_mensuel(salaire_annuel):
#         return salaire_annuel / 12

# def salaire_hebdomadaire(salaire_mensuel):
#         return salaire_mensuel / 4

# def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
#         return salaire_hebdomadaire / heures_travaillees

# print("Entrez votre salaire annuel :")
# salaire_annuel = float(input())
# salaire_mensuel = salaire_mensuel(salaire_annuel)
# salaire_hebdomadaire = salaire_hebdomadaire(salaire_mensuel)
# print("Entrez le nombre d'heures travaillées :")
# heures_travaillees = float(input())
# salaire_horaire = salaire_horaire(salaire_hebdomadaire, heures_travaillees)
# print(f"Votre salaire horaire est de : {salaire_horaire:.2f}")

# def print_welcome_message():
#     print("Bienvenue sur la mini-calculatrice !")
    
# def input_two_number():
#     num1 = float(input("Entrez le premier nombre : "))
#     num2 = float(input("Entrez le deuxième nombre : "))
#     return num1, num2

# def print_menu_and_get_choice():
#     print("=== MENU ===")
#     print("1. Addition")
#     print("2. Soustraction")
#     print("3. Multiplication")
#     print("4. Division")

#     user_choice = input("Entrez votre choix (1-4) : ")

#     while user_choice not in ["1", "2", "3", "4"]:

#         user_choice = input("Choix invalide. Entrez votre choix (1-4) : ")

#     return user_choice

# def sum(a, b):
#     return a + b

# def substraction(a, b):
#     return a - b

# def multiplication(a, b):
#     return a * b

# def division(a, b):
#     if b != 0:
#         return a / b
#     else:
#         print("Erreur : division par zéro")

# def run_calculation(user_choice):
#     num1, num2 = input_two_number()
#     match user_choice:
#         case '1':
#             result = sum(num1, num2)
#         case '2':
#             result = substraction(num1, num2)
#         case '3':
#             result = multiplication(num1, num2)
#         case '4':
#             result = division(num1, num2)
#         case _:
#             print("Choix invalide.")
#     return result

# if __name__ == '__main__':
#     print_welcome_message()
#     user_choice = print_menu_and_get_choice()
#     result = run_calculation(user_choice)
#     print(result)


from calculatornew.operations import sum, division
import requests
from bs4 import BeautifulSoup

# if __name__ == "__main__":
#     resultat = sum(20, 30)
#     resultat2 = division(30,2)
#     print(resultat, resultat2)
#     url = "https://www.gov.uk/search/news-and-communications"
#     page = requests.get(url)
#     html_code = page.text
#     print(page.content)

with open("index1.html", "r") as file:
    soup = BeautifulSoup(file.read(), "html.parser")
    print(soup.title.string)
    print(soup.find_all('a'))
    print(soup.find('a'))