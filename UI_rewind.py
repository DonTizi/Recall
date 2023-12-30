import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QScrollArea
from PyQt5.QtCore import Qt
from subprocess import Popen, PIPE

class AskWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.resize(600, 400)  # Largeur = 600, Hauteur = 400


    def initUI(self):
        self.setWindowTitle('Ask and Run')
        layout = QVBoxLayout()

        self.question_input = QLineEdit(self)
        self.question_input.setPlaceholderText('Posez votre question ici...')
        layout.addWidget(self.question_input)

        self.run_button = QPushButton('Poser la question', self)
        self.run_button.clicked.connect(self.run_script)
        layout.addWidget(self.run_button)

        # Créer une zone de défilement pour le label de la réponse
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        
        self.result_label = QLabel('Réponse apparaîtra ici...', self)
        self.result_label.setWordWrap(True)  # Permettre au texte de s'enrouler
        
        # Ajouter le label à la zone de défilement
        self.scroll_area.setWidget(self.result_label)
        layout.addWidget(self.scroll_area)

        self.setLayout(layout)

    def run_script(self):
        question = self.question_input.text()
        process = Popen(['python', 'indexing.py', question], stdout=PIPE, stderr=PIPE, text=True)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            self.result_label.setText(stdout.strip())
        else:
            self.result_label.setText(f'Erreur : {stderr}')
        self.result_label.adjustSize()  # Ajuster la taille du label au nouveau contenu

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AskWindow()
    ex.show()
    sys.exit(app.exec_())
