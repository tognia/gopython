
# import requests;
from bs4 import BeautifulSoup;

from calculator.operations import sum, subtraction, multiplication, division;

if (__name__ == "__main__"):
    result = sum(5, 3);
    print("The result of the sum is:", result);
    result = subtraction(5, 3);
    print("The result of the subtraction is:", result);
    result = multiplication(5, 3);
    print("The result of the multiplication is:", result);
    result = division(5, 3);
    print("The result of the division is:", result);

    with open("index.html", "r") as file:
        soup = BeautifulSoup(file, "html.parser");
    title = soup.title.string;
    h1Titre = soup.find("h1", id="titre");
    produits = soup.find_all("li", class_="product");
    print("Title of the HTML document:", title );
    print("H1 Title of the HTML document:", h1Titre.string if h1Titre else "Not found");
    print("List of products:");

# Dictionnaire pour stocker les produits
# all_products = dict()

# # Extraction des noms et des prix des produits dans la liste
# products = soup.find_all("li")
# for product in products:
#     name = product.find("h2").string
#     price_str = product.find("p", class_="price").string
#     # On sépare la chaine avec " " en liste de mots
#     price_list = price_str.split(" ")
#     # On récupère le prix (= deuxième mot)
#     all_products[name] = {"prix": price_list[1]}
    
#     # Extraction de la description du produit
#     # La description eest le dernier élément de la liste des paragraphes
#     description = product.find_all("p")[-1].string
#     all_products[name]["description"] = description

# # Affichage des informations extraites
# print("Produits:", all_products)

# # Transformation des prix en dollars
# for name in all_products.keys():
#     price_str = all_products[name]["prix"]
#     # Supprimer le symbole €
#     price = price_str.strip("€")
#     # Convertir en float
#     price = float(price)
#     dollar_price = price * 1.2
#     all_products[name]["prix_dollar"] = f"{dollar_price}$"

# Affichage avec les prix en dollars
# print("Tous les produits:", all_products)
list_produits = []
for produit in produits:
    nom = produit.find("h2").string if produit.find("h2") else "Not found"
    prix = produit.find("p", class_="price").string if produit.find("p", class_="price") else "Not found"
    
    # Nettoyer le prix pour ne garder qu'un nombre
    if prix and prix != "Not found":
        # Retirer le mot 'prix' et ':'
        parts = prix.split(":")
        if len(parts) > 1:
            prix = parts[1].strip()
        else:
            prix = parts[0].strip()
        
        # Retirer le symbole euro et autres caractères non numériques
        prix_numerique = ''.join(filter(str.isdigit, prix))
        
        # Convertir en dollar si on a un prix numérique valide
        if prix_numerique:
            prix_euro = int(prix_numerique)
            prix_dollar = prix_euro * 1.2
            prix = f"{prix_dollar:.0f}$"  # Format avec symbole dollar
        else:
            prix = "Not found"
    else:
        prix = "Not found"
    
    description = produit.find("p", class_="description").string if produit.find("p", class_="description") else "Not found"
    list_produits.append({"nom": nom, "prix": prix, "description": description})

for p in list_produits:
    print(f" - {p['nom']}: {p['prix']}, {p['description']}")

    # response = requests.get("https://google.com");
    # print("Response content:", response.content);






