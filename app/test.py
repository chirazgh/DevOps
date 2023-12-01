# test.py
import unittest
from username_checker import check_username

class TestUsernameChecker(unittest.TestCase):
    """
    Test pour le programme de vérification du nom d'utilisateur
    """

    def test_existing_user(self):
        """
        Vérification d'un utilisateur existant dans la liste.
        """
        result = check_username("Chiraz", ["Chiraz", "Wafa", "Dorra", "Ali", "Ahmed"])
        self.assertTrue(result)  # Vérifiez que la fonction retourne True pour un utilisateur existant

    def test_non_existing_user(self):
        """
        Vérification d'un utilisateur non existant dans la liste.
        """
        result = check_username("John", ["Chiraz", "Wafa", "Dorra", "Ali", "Ahmed"])
        self.assertFalse(result)  # Vérifiez que la fonction retourne False pour un utilisateur non existant

    def test_empty_username(self):
        """
        Vérification d'un nom d'utilisateur vide.
        """
        result = check_username("", ["Chiraz", "Wafa", "Dorra", "Ali", "Ahmed"])
        self.assertFalse(result)  # Vérifiez que la fonction retourne False pour un nom d'utilisateur vide

if __name__ == "__main__":
    unittest.main()