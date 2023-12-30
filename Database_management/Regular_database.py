import sqlite3

conn = sqlite3.connect('regular_data.db', check_same_thread=False)
cursor = conn.cursor()

# Créer la table pour les images
cursor.execute('''CREATE TABLE IF NOT EXISTS images
                  (id INTEGER PRIMARY KEY,
                  image BLOB,
                  metadata TEXT)''')  # ou 'chemin TEXT' si vous stockez le chemin

# Créer la table pour les transcriptions
cursor.execute('''CREATE TABLE IF NOT EXISTS transcriptions
                  (id INTEGER PRIMARY KEY,
                  titre TEXT,
                  transcription TEXT,
                  date DATETIME,
                  autres_metadata TEXT)''')

# Ne pas oublier de commit et fermer la connexion
conn.commit()
conn.close()
