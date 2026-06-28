import pandas as pd
import numpy as np


df = pd.read_csv("ESA_CNES - CubeSeat Dataset - data_V2.csv")

df['Coût Total (USD)'] = df['Coût Total (USD)'].astype(str).str.replace(',', '.')
df['Coût Total (USD)'] = pd.to_numeric(df['Coût Total (USD)'], errors='coerce')


def calculate_clean_complexity(row):
    #base par Type de Mission (Complexité de la charge utile)
    mission = str(row['Mission_Type']).strip()
    base_scores = {
        'Technology Demo': 1.0,
        'Communications': 1.3,
        'Earth Observation': 1.8,
        'Military/Defense': 2.7,
        'Science/Astronomy': 2.7
    }
    
    # Si le type est "Deep Space", on le traite comme une mission scientifique complexe
    if mission == 'Deep Space':
        score = 3.0
    else:
        score = base_scores.get(mission, 1.4) # 1.4 par défaut si inconnu
    
    org = str(row['Organization']).lower()
    mfg = str(row['Manufactured (AIVT) by']).lower()
    
    agencies = ['esa', 'nasa', 'jpl', 'darpa', 'dlr', 'cnes', 'air force', 'defence', 'defensa']
    academic = ['university', 'ecole', 'politecnico', 'college', 'instit', 'in-house']
    
    if any(agency in org or agency in mfg for agency in agencies):
        score += 0.5
    elif any(acad in org or acad in mfg for acad in academic):
        # On vérifie que ce n'est pas un projet universitaire mais clé en main chez un industriel
        if 'gomspace' not in mfg and 'clyde' not in mfg and 'nanoavionics' not in mfg:
            score -= 0.2
        
        
    return round(score, 2)


df['Complexity_Score'] = df.apply(calculate_clean_complexity, axis=1)

df_orbites = pd.read_csv("draft\ESA_CNES - CubeSeat Dataset - data.csv")
df_merged = pd.merge(df, df_orbites[['id', 'Orbit_Type']], on='id', how='outer')
print(df_merged[['Project', 'Coût Total (USD)', 'Complexity_Score']].head())
df_merged.to_csv("CubeSat_Dataset_Clean.csv", index=False)