import pandas as pd
import numpy as np


df = pd.read_csv("bayesian-decision-model-for-cubesat-mission\ESA_CNES - CubeSeat Dataset - data_V2.csv")

df['Coût Total (USD)'] = df['Coût Total (USD)'].astype(str).str.replace(',', '.')
df['Coût Total (USD)'] = pd.to_numeric(df['Coût Total (USD)'], errors='coerce')


def calculate_clean_complexity(row):
    #base par Type de Mission (Complexité de la charge utile)
    mission = str(row['Mission_Type']).strip()
    score = 1.0
    mission_bonus = {
        "Technology Demo": 0.0,
        "Communications": 0.3,
        "Earth Observation": 0.5,
        "Military/Defense": 0.7,
        "Science/Astronomy": 1.0,
        "Deep Space": 2.0
    }
    for key, value in mission_bonus.items():
        if key in mission:
            score += value

    
    org = str(row['Organization']).lower()
    mfg = str(row['Manufactured (AIVT) by']).lower()
    
    agencies = ['esa', 'nasa', 'jpl', 'darpa', 'dlr', 'cnes', 'air force', 'defence', 'defensa']
    academic = ['university', 'ecole', 'politecnico', 'college', 'instit', 'in-house']
    
    if any(agency in org or agency in mfg for agency in agencies):
        if "Science/Astronomy" in mission:
            score += 0.7
        else:
            score += 0.5
    elif any(acad in org or acad in mfg for acad in academic):
        # On vérifie que ce n'est pas un projet universitaire mais clé en main chez un industriel
        if 'gomspace' not in mfg and 'clyde' not in mfg and 'nanoavionics' not in mfg:
            score -= 0.2
        
    return round(score, 2)


df['Complexity_Score'] = df.apply(calculate_clean_complexity, axis=1)

df_orbites = pd.read_csv("bayesian-decision-model-for-cubesat-mission\draft\ESA_CNES - CubeSeat Dataset - data.csv")
df_merged = pd.merge(df, df_orbites[['id', 'Orbit_Type']], on='id', how='outer')
print(df_merged[['Project', 'Coût Total (USD)', 'Complexity_Score']].head())
df_merged.to_csv("bayesian-decision-model-for-cubesat-mission\CubeSat_Dataset_Clean.csv", index=False)