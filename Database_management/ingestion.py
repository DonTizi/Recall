import sqlite3

# Chemin vers votre base de données SQLite
database_path = '../Rewind/regular_data.db' # Replace it with your DB Path

# Chemin et nom des fichiers où vous voulez enregistrer les textes
all_texts_output_path = 'all_texts.txt'
new_texts_output_path = 'new_texts.txt'  # Fichier pour les nouvelles entrées uniquement

# Connectez-vous à la base de données SQLite
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

# Assurez-vous que la colonne processed existe, sinon créez-la
cursor.execute("SELECT name FROM pragma_table_info('images') WHERE name='processed'")
if cursor.fetchone() is None:
    cursor.execute("ALTER TABLE images ADD COLUMN processed BOOLEAN DEFAULT 0")
    conn.commit()

# Récupérez tous les textes non traités de la table images
cursor.execute("SELECT id, metadata FROM images WHERE processed = 0")
new_texts = cursor.fetchall()

# Écrivez les nouveaux textes dans les fichiers, s'il y en a
if new_texts:
    with open(all_texts_output_path, 'a') as all_file, open(new_texts_output_path, 'w') as new_file:
        for id, text in new_texts:
            # Écrivez dans le fichier de tous les textes
            all_file.write(text + '\n')
            # Écrivez également dans le fichier des nouveautés
            new_file.write(text + '\n')
            # Marquez le texte comme traité
            cursor.execute("UPDATE images SET processed = 1 WHERE id = ?", (id,))

# Sauvegardez les modifications dans la base de données
conn.commit()

# Fermez la connexion à la base de données
conn.close()

print(f"Les nouveaux textes ont été ajoutés à {all_texts_output_path} et {new_texts_output_path}.")
