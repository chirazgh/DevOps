# username_checker.py

def check_username(username, existing_usernames):
    """
    Vérifie si le nom d'utilisateur est dans la liste des utilisateurs existants.
    """
    return username in existing_usernames

if __name__ == "__main__":
    # Liste de noms d'utilisateurs
    noms_utilisateurs = ["Chiraz", "Wafa", "Dorra", "Ali", "Ahmed"]

    # Demander à l'utilisateur d'entrer son nom
    nom_utilisateur = input("Entrez votre nom : ")

    # Utiliser la fonction check_username pour vérifier si le nom d'utilisateur est dans la liste
    if check_username(nom_utilisateur, noms_utilisateurs):
        print(f"Bienvenue, {nom_utilisateur} ! Vous êtes un utilisateur enregistré.")
    else:
        print(f"Désolée, {nom_utilisateur}. Vous n'êtes pas dans la liste des utilisateurs enregistrés.")
