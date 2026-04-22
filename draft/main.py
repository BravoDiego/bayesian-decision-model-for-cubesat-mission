# Lire le fichier input.txt
with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Traiter les lignes (enlever la dernière lettre de chaque ligne)
new_lines = []
for line in lines:
    line = line.rstrip("\n")  # enlever le saut de ligne
    if len(line) > 0:
        #line = "0" if "In-house" in line else "1"
        line.replace("\"", "")
         # enlever le dernier caractère
    new_lines.append(line+"\n")  # remettre le saut de ligne

# Écrire dans output.txt
with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Fichier traité avec succès !")
