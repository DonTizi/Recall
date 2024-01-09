import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QScrollArea, QProgressBar
from PyQt5.QtCore import Qt
from subprocess import Popen, PIPE
from pynput import keyboard

class AskWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.resize(895, 485)  # Set the window size to 535x765

    def initUI(self):
        self.setWindowTitle('Ask and Run')
        layout = QVBoxLayout()

        self.question_input = QLineEdit(self)
        self.question_input.setPlaceholderText('Please ask your question here')
        layout.addWidget(self.question_input)

        self.run_button = QPushButton('Ask your question', self)
        self.run_button.clicked.connect(self.run_script)
        layout.addWidget(self.run_button)

        # Loading animation setup
        self.progress = QProgressBar(self)
        self.progress.setMaximum(0)  # Indeterminate mode
        self.progress.setMinimum(0)
        self.progress.hide()  # Hide progress bar initially
        layout.addWidget(self.progress)

        # Scrollable area for the result label
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.result_label = QLabel('Réponse apparaîtra ici...', self)
        self.result_label.setWordWrap(True)
        self.scroll_area.setWidget(self.result_label)
        layout.addWidget(self.scroll_area)

        self.setLayout(layout)

    def run_script(self):
        # Show loading animation and execute the script
        self.progress.show()
        question = self.question_input.text()
        process = Popen(['python', 'indexing.py', question], stdout=PIPE, stderr=PIPE, text=True)
        stdout, stderr = process.communicate()

        # Update the UI with the script result or error
        if process.returncode == 0:
            self.result_label.setText(stdout.strip())
        else:
            self.result_label.setText(f'Erreur : {stderr}')

        self.result_label.adjustSize()  # Adjust the label size to fit new content
        self.progress.hide()  # Hide the loading animation


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AskWindow()
    ex.show()



    sys.exit(app.exec_())
