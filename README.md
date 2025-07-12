# Chess_broker
# ♟ Chess Broker

🇫🇷**Chess Broker** est un outil open-source en Python qui permet de récupérer des informations publiques sur un compte Chess.com à l’aide de l’API officielle publique de la plateforme.

🇬🇧 OSINT tool for chess account.
---

## 🔍 Fonctionnalités

- Récupération de données publiques via l'API Chess.com :
  - Nom d'utilisateur
  - Pays
  - Avatar
  - Date d’inscription
  - Statut (premium, etc.)
  - Vérification
  - Dernière connexion
  - Plateforme de streaming (si renseignée)
  - Nombre de followers
  - Informations publiques de récupération de mot de passe (si disponibles)

---

## ⚖ Légalité & Éthique

✅ Utilise ce script uniquement pour :

des fins éducatives 🧠

du test en interne 🔒

ou avec autorisation (pentest OSINT autorisé par cible) ✅

❌ Aucune tentative d'accès non autorisé, de contournement ou de piratage n'est effectuée.  
📄 Je ne suis pas responsable de l’usage que vous ferez de ce script.

---

## Note
Le script prend le premier et dernier caractère du nom du mail exemple : 
promiris123@gmail.com = `p***3@g***l.com` (ceci est un faux mail a l'heure ou j'écris cela) 
---

## 🛠 Dépendances

- Python 3.10+ recommandé
- [art](https://pypi.org/project/art/) — pour un affichage stylisé en ASCII
- [requests](https://pypi.org/project/requests/) — pour les requêtes HTTP

### Installation

```bash
# Installer l'outil
git clone https://github.com/linuxuser-hash/Chess_broker.git
cd Chess_broker
pip install -r requierments.txt --break-system-packages


# Créer un environnement virtuel (recommandé)
python3 -m venv venv
source venv/bin/activate
