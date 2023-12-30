import sqlite3
import os
import time
import logging
import pytesseract
from PIL import Image
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configuration de logging
logging.basicConfig(filename='/Users/dontizi/Documents/Rewind/app.log',
                    level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

# Chemins vers les dossiers principaux
chemin_images = '/Users/dontizi/Documents/Rewind/Screenshots'
chemin_transcriptions = '/Users/dontizi/Documents/Rewind/Transcription'

# Configuration de pytesseract
# Si nécessaire, spécifiez le chemin vers tesseract ici
# pytesseract.pytesseract.tesseract_cmd = '/path/to/tesseract'

def wait_for_file_to_finish(file_path):
    """Attendre que la taille du fichier ne change plus, ce qui indique la fin de l'écriture."""
    size = -1
    while size != os.path.getsize(file_path):
        size = os.path.getsize(file_path)
        time.sleep(1)  # Attendre 1 seconde avant de re-vérifier la taille

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Vérifier si c'est un dossier: traiter comme un nouveau dossier de date
        if event.is_directory:
            # Surveiller le nouveau dossier pour les fichiers
            observer.schedule(FileHandler(), event.src_path, recursive=False)
        else:
            self.handle_file(event.src_path)

    def handle_file(self, file_path):
        try:
            wait_for_file_to_finish(file_path)  # Attendre que l'écriture du fichier soit terminée
            conn = sqlite3.connect('regular_data.db', check_same_thread=False)
            cursor = conn.cursor()
            
            # Décider si le fichier est une image ou une transcription
            if chemin_images in file_path:
                # Traiter comme image
                with open(file_path, 'rb') as f:
                    img = f.read()
                    # Extraire le texte de l'image avec OCR
                    text = pytesseract.image_to_string(Image.open(f), lang='fra+eng')
                    # Insérer l'image et le texte extrait dans la base de données
                    cursor.execute("INSERT INTO images (image, metadata) VALUES (?, ?)", (img, text))
                    logging.info(f"Image et texte insérés avec succès : {file_path}")
                    print(f"Size of image data read: {len(img)} bytes")
                    
            elif chemin_transcriptions in file_path:
                # Traiter comme transcription
                with open(file_path, 'r') as f:
                    text = f.read()
                    cursor.execute("INSERT INTO transcriptions (transcription) VALUES (?)", (text,))
                    logging.info(f"Transcription insérée avec succès : {file_path}")
                    
            conn.commit()
        except Exception as e:
            logging.error(f"Erreur lors de l'insertion du fichier {file_path}: {e}")
        finally:
            conn.close()

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            MyHandler().handle_file(event.src_path)

# Observer pour les dossiers principaux (qui va détecter les nouveaux dossiers de date)
observer = Observer()
observer.schedule(MyHandler(), chemin_images, recursive=True)
observer.schedule(MyHandler(), chemin_transcriptions, recursive=True)
observer.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()
    logging.info("Surveillance des dossiers arrêtée.")
observer.join()
