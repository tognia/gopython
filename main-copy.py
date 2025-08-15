# print("Enter the first number:");
# number1 = input();
# print("Enter the second number:");
# number2 = input();
# result = 0;
# if not number1.isnumeric() or not number2.isnumeric():
#     raise SystemExit("Fin du programme");
# else:
#     number1 = int(number1);
#     number2 = int(number2);
    
#     print("Enter an operator (+, -, *, /):");
#     operator = input();
#     if not operator in ['+', '-', '*', '/']:
#         raise SystemExit("Fin du programme");
#     else:
#         if operator == '+':
#             result = number1 + number2;
#         elif operator == '-':
#             result = number1 - number2;
#         elif operator == '*':
#             result = number1 * number2;
#         elif operator == '/':
#             if number2 == 0:
#                 raise SystemExit("Division par zéro n'est pas autorisée");
#             result = round(number1 / number2, 2);

# print("Le résultat de", number1, operator, number2, "est:", result);
# print("Fin du programme");

# races_de_chien = ["golden retriever", "chihuahua", "terrier", "carlin"]
# for chien in races_de_chien:
#     print(chien);

# for x in range(4, 10):
#     print(x);
# capacite_maximale = 10;
# capacite_actuelle = 3;
# while capacite_actuelle < capacite_maximale:
#     print("Capacité actuelle:", capacite_actuelle);
#     capacite_actuelle += 1;

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# liste = [1, 2, 3, 4, 5]
# for i in liste:
#     if i == 3:
#         continue
#     print(i)

# print ("Veuillez entrer une liste de nombres séparés par des virgules :");
# nombres = input();
# print(nombres);
# nombres_liste = nombres.split(",");
# print("Liste de nombres :", nombres_liste);
# liste_entiers = [int(nombre) for nombre in nombres_liste if nombre.isdigit()]
# print("Liste d'entiers :", liste_entiers);
# somme = 0;
# for nombre in liste_entiers:
#     somme += nombre;
# print("La somme des entiers est :", somme);
# moyenne = somme / len(liste_entiers) if liste_entiers else 0 ;
# print("La moyenne des entiers est :", moyenne); 
# nombres_superieurs_a_moyenne = [nombre for nombre in liste_entiers if nombre > moyenne]
# print("Nombres supérieurs à la moyenne :", nombres_superieurs_a_moyenne);

# def afficher_messagage():
#     print("Bonjour, bienvenue dans le programme de calcul !");

# afficher_messagage();

# def afficher_nom_prenom(nom, prenom):
#     print("Nom :", nom);
#     print("Prénom :", prenom);  

# afficher_nom_prenom("Dupont", "Jean");

# def additioner (a,b):
#     return a, b, a + b;

# print("La somme de 5 et 3 est :", additioner(5, 3));

# def salaire_mensuel(salaire_annuel):
  
#    return salaire_annuel / 12;


# def salaire_hebdomadaire(salaire_mensuel):
#    return salaire_mensuel / 4;

# def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
#    return salaire_hebdomadaire / heures_travaillees;


# print("Veuillez entrer votre salaire annuel :");
# salaire_annuel = input();
# print("Veuillez entrer le nombre d'heures travaillées par semaine :");
# heures_travaillees = input();

# votre_salaire_horaire = salaire_horaire(salaire_hebdomadaire(salaire_mensuel(int(salaire_annuel))),int(heures_travaillees))

# print("Votre salaire horaire est :", round(votre_salaire_horaire, 2));

# while True:
#    try:
#       x= int(input("Veuillez entrer un nombre entier : "))
#       break
#    except ValueError:
#       print("Ce n'est pas un nombre entier valide. Veuillez réessayer.")
   