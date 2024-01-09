import os
import subprocess
import threading
import time

# Scripts à exécuter
scripts = {
    "image_record": "./Rewind/record/record_photo.py",
    "pipeline": "./Rewind/Database_management/pipeline_db.py",
    "ingestion": "./Rewind/Database_management/ingestion.py",
    "adding_vectore": "./Rewind/Vectore/adding_vectore.py"
}

# Exécution des scripts d'enregistrement audio, d'image et du pipeline
for script in ["image_record", "pipeline"]:
    threading.Thread(target=subprocess.call, args=(['python', os.path.join(os.getcwd(), scripts[script])],)).start()

# Fonction pour exécuter l'ingestion et l'ajout de vecteurs toutes les 2 minutes
def pipeline():
    while True:
        # Exécution du script d'ingestion
        subprocess.call(['python', os.path.join(os.getcwd(), scripts["ingestion"])])

        # Exécution du script d'ajout de vecteurs
        subprocess.call(['python', os.path.join(os.getcwd(), scripts["adding_vectore"])])

        # Attente de 2 minutes
        time.sleep(120)

# Démarrage du pipeline
threading.Thread(target=pipeline).start()
