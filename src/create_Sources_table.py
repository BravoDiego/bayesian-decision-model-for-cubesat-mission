import csv

nom_fichier_csv = "bayesian-decision-model-for-cubesat-mission\\src\\extraction_satellites.csv"
nom_fichier_markdown = "sources_bibliographie.md"


lignes_markdown = [
    "| Satellite Name | Size | Primary Documentation / Source Link |",
    "| :--- | :--- | :--- |"
]


with open(nom_fichier_csv, mode="r", encoding="utf-8-sig") as fichier:
    lecteur = csv.DictReader(fichier)
    
    for ligne in lecteur:
        print(ligne)
        nom = ligne["Project"].strip()
        taille = ligne["Size"].strip()
        url_source = ligne["Source"].strip()
    
        if not url_source or url_source == "...":
            lien_md = "Documentation non disponible"
        else:
            lien_md = f"[Source Document / Article]({url_source})"
        
        lignes_markdown.append(f"| **{nom}** | {taille} | {lien_md} |")

texte_markdown_complet = "\n".join(lignes_markdown)

with open(nom_fichier_markdown, mode="w", encoding="utf-8") as fichier_out:
    fichier_out.write(texte_markdown_complet)
