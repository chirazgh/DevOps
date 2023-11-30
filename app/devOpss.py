# Programme de vérification du nom d'utilisateur

# Liste de noms d'utilisateurs
noms_utilisateurs = ["Chiraz", "Wafa", "Dorra", "Ali", "Ahmed"]

# Demander à l'utilisateur d'entrer son nom
nom_utilisateur = input("Entrez votre nom : ")

# Vérifier si le nom d'utilisateur est dans la liste
if nom_utilisateur in noms_utilisateurs:
    print(f"Bienvenue, {nom_utilisateur} ! Vous êtes un utilisateur enregistré.")
else:
    print(f"Désolée, {nom_utilisateur}. Vous n'êtes pas dans la liste des utilisateurs enregistrés.")