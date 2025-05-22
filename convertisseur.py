import pandas as pd
import json

# Lire le fichier Excel
df = pd.read_excel('codes.xlsx')

# Vérifier les noms de colonnes
print("Colonnes trouvées dans Excel :", df.columns.tolist())

# Créer un dictionnaire avec les codes comme clés
data = {}

for _, row in df.iterrows():
    code = str(row['Code Postal']).strip()
    url = str(row['url']).strip()
    data[code] = url

# Écrire dans data.json
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("data.json créé avec succès !")
