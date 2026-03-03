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

print("Entrer les 2 nombres à manipuler :")

nombre1 = input("Nombre 1 : ")
nombre2 = input("Nombre 2 : ")

if not nombre1.isnumeric() or not nombre2.isnumeric():
    print("Veuillez entrer des entiers valides.")
    raise SystemExit("Fin du programme.")
else:
    print("Les nombres entrés sont :", nombre1, "et", nombre2)
    nombre1 = int(nombre1)
    nombre2 = int(nombre2)

    print("Entrer l'opération à effectuer (addition, soustraction, multiplication, division) :")

    operation = input("Opération : ")

    if not operation in ["+", "-", "*", "/"]:
        raise SystemExit("Opération non valide. Fin du programme.")
    else:
        print("L'opération choisie est :", operation)
        match operation:
            case "+":
                resultat = nombre1 + nombre2
                print("Le résultat de l'addition est :", resultat)
            case "-":
                resultat = nombre1 - nombre2
                print("Le résultat de la soustraction est :", resultat)
            case "*":
                resultat = nombre1 * nombre2
                print("Le résultat de la multiplication est :", resultat)
            case "/":
                if nombre2 == 0:
                    raise SystemExit("Division par zéro impossible. Fin du programme.")
                else:
                    resultat = nombre1 / nombre2
                    print("Le résultat de la division est :", round(resultat, 2))

