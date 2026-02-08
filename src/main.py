import os
import sys
from dotenv import load_dotenv
from mikrotik_api import MikrotikCSS610

# 1. Chargement des secrets
load_dotenv()
IP = os.getenv("SWITCH_IP")
USER = os.getenv("SWITCH_USER")
PASSWORD = os.getenv("SWITCH_PASSWORD")

# 2. Création du contrôleur
mon_switch = MikrotikCSS610(IP, USER, PASSWORD)

# 3. Test de sécurité
print("--- Test de connexion ---")
status = mon_switch.test_connexion()
print(status)

# 4. Si la connexion est OK, on demande les VLANs
if "Succés !" in status:
    print("\n--- Récupération des VLANs ---")
    vlans = mon_switch.get_vlans()
    print(vlans)