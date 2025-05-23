import pandas as pd
import json
import os

# --- ÉTAPE 1 : Chargement du fichier Excel ---
excel_path = 'Codes.xlsx'  # Change ici si le fichier est dans un autre dossier

if not os.path.exists(excel_path):
    print(f"❌ Fichier introuvable : {excel_path}")
    exit()

try:
    df = pd.read_excel(excel_path, dtype={'Code Postal': str})
    print("✅ Fichier Excel chargé avec succès.")
except Exception as e:
    print("❌ Erreur lors de la lecture du fichier Excel :")
    print(e)
    exit()

# --- ÉTAPE 2 : Traitement des données et création du JSON ---
try:
    print("Colonnes détectées :", df.columns.tolist())

    data = {}
    for _, row in df.iterrows():
        code = row['Code Postal'].zfill(5).strip()
        url = str(row['url']).strip()
        data[code] = url

    # Écrire dans data.json
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("✅ data.json créé avec succès !")

except KeyError as e:
    print("❌ Nom de colonne incorrect. Vérifie bien qu'il y a une colonne 'Code Postal' et une 'url'")
    print(e)

except Exception as e:
    print("❌ Erreur inattendue pendant le traitement des données :")
    print(e)
