# Raidlight Scraper

Ce projet est un **scraper Python** pour récupérer les produits du site [Raidlight](https://raidlight.com) via leur API JSON. Il génère un fichier CSV avec les informations principales des produits.

---

## Fonctionnalités

- Scraping des produits via l'API JSON (méthode plus fiable que le scraping HTML)
- Gestion des limites de requêtes et délais aléatoires pour éviter le blocage
- Extraction des informations principales :
  - Nom du produit
  - Prix
  - Lien vers le produit
  - Catégorie
  - Fournisseur
  - Disponibilité
- Sauvegarde des résultats dans un fichier `products.csv`
- Limitation à 100 produits par défaut pour éviter les requêtes trop lourdes

---

## Installation

1. Cloner le dépôt :

git clone https://github.com/HamzaTheBuilder/raidlight_scraper.git
cd raidlight_scraper

Créer un environnement virtuel (optionnel mais recommandé) :
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows



Installer les dépendances :

pip install -r requirements.txt

Utilisation
Pour lancer le scraper :

python3 raidlight_scraper.py

Le fichier products.csv sera généré à la racine du projet avec les données des produits récupérés.

Configuration

Nombre maximum de produits : modifier la variable max_products dans le script
Limite de pages : modifier la variable page <= 20 dans le script
Délai entre les requêtes : ajuster la variable delay = random.uniform(2, 4)


Contribution
Les contributions sont les bienvenues !

Fork le projet
Crée une branche (git checkout -b feature/ma-fonctionnalite)
Commit tes modifications (git commit -m 'Ajout d'une fonctionnalité')
Push la branche (git push origin feature/ma-fonctionnalite)
Ouvre une Pull Request


Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus d'informations.
RéessayerClaude n'a pas encore la capacité d'exécuter le code qu'il génère.
