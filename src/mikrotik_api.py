import requests
from requests.auth import HTTPDigestAuth

class MikrotikCSS610:
    """
    Classe pour piloter le switch MikroTik CSS610 (SwOS Lite).
    """

    def __init__(self, ip, username, password):
        # On construit l'adresse de base pour les requêtes
        self.base_url = f"http://{ip}"
        # On prépare l'authentification
        self.auth = HTTPDigestAuth(username, password)

    def test_connexion(self):
        """
        Vérifie simplement si on peut accéder au switch.
        Sert à valider l'IP et le Mot de passe.
        """
        try:
            # On essaie d'accéder à la page d'accueil (index.html)
            url = f"{self.base_url}/index.html"
            reponse = requests.get(url, auth=self.auth, timeout=5)

            if reponse.status_code == 200:
                return "Connexion établie !"
            elif reponse.status_code == 401:
                return "Mauvais utilisateur ou mot de passe."
            else:
                return f"Erreur : Code HTTP {reponse.status_code}"
        
        except requests.exceptions.Timeout:
            return "Erreur : Le switch ne répond pas (Vérifie l'IP ou le câble)."
        except Exception as e:
            return f"Erreur critique : {e}"

    def get_vlans(self):
        """
        Récupère la configuration des VLANs (fichier vlans.b).
        """
        try:
            url = f"{self.base_url}/vlans.b"
            reponse = requests.get(url, auth=self.auth, timeout=5)
            
            if reponse.status_code == 200:
                return reponse.text  # Renvoie le contenu brut
            else:
                return f"Erreur lors de la récupération des VLANs (Code {reponse.status_code})"
        except Exception as e:
            return f"Erreur de connexion : {e}"