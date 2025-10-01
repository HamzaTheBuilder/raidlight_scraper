import requests
import csv
import time
import random

def scrape_raidlight_api():
    """
    Scraping des produits Raidlight via l'API JSON
    Méthode plus fiable et moins bloquante que le HTML scraping
    """
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'fr-FR,fr;q=0.9,en;q=0.8',
        'Referer': 'https://raidlight.com/',
        'X-Requested-With': 'XMLHttpRequest'
    })
    
    products = []
    page = 1
    max_products = 100
    
    print(" Début du scraping Raidlight via API...")
    
    while len(products) < max_products and page <= 20:  # Limite de sécurité
        # Délai respectueux entre les requêtes
        delay = random.uniform(2, 4)
        print(f" Attente de {delay:.1f}s avant la page {page}...")
        time.sleep(delay)
        
        # Endpoint principal de l'API produits
        url = f"https://raidlight.com/products.json?page={page}"
        
        try:
            response = session.get(url, timeout=15)
            
            if response.status_code == 429:
                print("  Limite de taux atteinte. Attente de 30 secondes...")
                time.sleep(30)
                continue
                
            if response.status_code != 200:
                print(f" Erreur {response.status_code}. Passage à la page suivante...")
                page += 1
                continue
            
            data = response.json()
            
            # Extraction des produits depuis la réponse JSON
            products_list = data.get('products', [])
            
            if not products_list:
                print(" Fin des produits disponibles")
                break
            
            print(f" Page {page}: {len(products_list)} produits trouvés")
            
            for product in products_list:
                if len(products) >= max_products:
                    break
                
                # Nettoyage et formatage des données
                product_name = product.get('title', 'Nom non disponible').strip()
                
                # Gestion du prix
                variants = product.get('variants', [{}])
                price = "Non disponible"
                if variants and 'price' in variants[0]:
                    price_value = variants[0]['price']
                    if price_value:
                        price = f"{price_value} EUR"
                
                # Construction du lien produit
                handle = product.get('handle', '')
                product_link = f"https://raidlight.com/products/{handle}" if handle else "Lien non disponible"
                
                # Catégorie et type
                product_type = product.get('product_type', 'Non catégorisé')
                vendor = product.get('vendor', 'Raidlight')
                
                product_data = {
                    'name': product_name,
                    'price': price,
                    'link': product_link,
                    'category': product_type,
                    'vendor': vendor,
                    'available': product.get('available', False)
                }
                
                products.append(product_data)
                print(f" [{len(products)}] {product_name} - {price}")
            
            page += 1
            
        except requests.exceptions.RequestException as e:
            print(f" Erreur réseau: {e}")
            time.sleep(10)
        except ValueError as e:
            print(f" Erreur JSON: {e}")
            break
        except Exception as e:
            print(f" Erreur inattendue: {e}")
            break
    
    # Sauvegarde des résultats
    if products:
        filename = 'products.csv'
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['name', 'price', 'link', 'category', 'vendor', 'available']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(products)
        
        print(f"\n SUCCÈS: {len(products)} produits sauvegardés dans {filename}")
        
        # Statistiques
        categories = set(p['category'] for p in products)
        print(f"Catégories trouvées: {len(categories)}")
        print(f"Exemples de catégories: {list(categories)[:5]}")
        
    else:
        print("Aucun produit n'a été récupéré")

if __name__ == "__main__":
    scrape_raidlight_api()