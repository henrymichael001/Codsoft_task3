import sys
import random
import string
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QRadioButton
from PyQt5.QtCore import Qt

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(400, 300)

        main_layout = QVBoxLayout()

        length_layout = QHBoxLayout()

        length_label = QLabel('Password Length:')
        length_layout.addWidget(length_label)

        self.length_line_edit = QLineEdit()
        self.length_line_edit.setPlaceholderText('Enter password length')
        self.length_line_edit.setStyleSheet("border-radius: 10px; padding: 5px;")
        length_layout.addWidget(self.length_line_edit)

        main_layout.addLayout(length_layout)

        radio_layout = QHBoxLayout()
        radio_layout.addStretch(1)  

        self.easy_radio = QRadioButton('Easy')
        self.medium_radio = QRadioButton('Medium')
        self.hard_radio = QRadioButton('Hard')
        radio_layout.addWidget(self.easy_radio)
        radio_layout.addStretch(1)  
        radio_layout.addWidget(self.medium_radio)
        radio_layout.addStretch(1)
        radio_layout.addWidget(self.hard_radio)
        radio_layout.addStretch(1)  

        self.medium_radio.setChecked(True)

        main_layout.addLayout(radio_layout)

        self.label = QLabel('Generated Password:')
        self.label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.label)

        main_layout.addSpacing(20)

        self.password_line_edit = QLineEdit()
        self.password_line_edit.setReadOnly(True)
        self.password_line_edit.setStyleSheet("""
            QLineEdit {
                font-weight: bold;
                text-transform: uppercase;
                margin-top: 20px;  # Increase top margin for visual separation
                border-radius: 15px;  # Curved edges
                padding: 15px;  # Increase padding for a larger display
                font-size: 18px;  # Increase font size for better visibility
                text-align: center;  # Center align text
            }
        """)
        main_layout.addWidget(self.password_line_edit)

        self.button = QPushButton('Generate Password')
        self.button.clicked.connect(self.generate_password)
        self.button.setStyleSheet("""
            QPushButton {
                color: white;
                font-weight: bold;
                background-color: red;
                border-radius: 25px;  # Curved edges
                padding: 15px 30px;  # Increase padding for a larger button
                font-size: 18px;  # Increase font size for better visibility
            }
            QPushButton:pressed {
                background-color: #cc0000;
            }
        """)
        button_layout = QHBoxLayout()  
        button_layout.addStretch(1)
        button_layout.addWidget(self.button)
        button_layout.addStretch(1)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def generate_password(self):

        length = int(self.length_line_edit.text()) if self.length_line_edit.text().isdigit() else 12

        easy_chars = string.ascii_lowercase
        medium_chars = string.ascii_letters + string.digits
        hard_chars = string.ascii_letters + string.digits + string.punctuation

        if self.easy_radio.isChecked():
            characters = easy_chars
        elif self.medium_radio.isChecked():
            characters = medium_chars
        else:
            characters = hard_chars

        password = ''.join(random.choice(characters) for i in range(length))
        self.password_line_edit.setText(password)

def main():
    app = QApplication(sys.argv)
    generator = PasswordGenerator()
    generator.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
