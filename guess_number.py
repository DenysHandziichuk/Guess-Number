import sys
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QVBoxLayout, QPushButton, QWidget, QMessageBox
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 300, 200)
        self.setWindowTitle("Guess the number")

        widget = QWidget(self)
        self.setCentralWidget(widget)

        layout = QVBoxLayout()
        widget.setLayout(layout)

        self.label = QLabel("Let's guess the number", self)
        layout.addWidget(self.label)
        
        self.hints = 1
        self.hints_label = QLabel(f"You have {self.hints} hints left", self)
        layout.addWidget(self.hints_label)

        self.entry = QLineEdit(self)
        layout.addWidget(self.entry)

        self.button = QPushButton("Guess it", self)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.function)

        self.button = QPushButton("Hint", self)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.show_hints)


        self.reset_button = QPushButton("Reset" ,self)
        layout.addWidget(self.reset_button)
        self.reset_button.clicked.connect(self.reset)

        self.random_number = random.randint(1, 100)

    def function(self):
        self.enter = int(self.entry.text())
        try:
            if self.enter == self.random_number:
                messagebox = QMessageBox()
                messagebox.setText("Congratulations, You Won!")
                messagebox.exec()
            elif self.enter > self.random_number:
                messagebox = QMessageBox()
                messagebox.setText("Number is too big")
                messagebox.exec()
            elif self.enter < self.random_number:
                messagebox = QMessageBox()
                messagebox.setText("Number is too low")
                messagebox.exec()
            elif self.enter <= 100 or self.enter <= 0:
                messagebox = QMessageBox()
                messagebox.setText("Invalid entry, enter number from 1 to 100")
                messagebox.exec() 
        except ValueError:
            messagebox = QMessageBox()
            messagebox.setText("Invalid input, enter an integer")
            messagebox.exec()
        self.entry.clear()
    

    def show_hints(self):
        if self.hints > 0:
            self.hints -= 1
            self.hints_label.setText(f"You have {self.hints} hints left")
        
            if self.random_number > 50:
                messagebox = QMessageBox()
                messagebox.setText("Number is bigger than 50")
                messagebox.exec()
            elif self.random_number < 50:
                messagebox = QMessageBox()
                messagebox.setText("Number is lower than 50")
                messagebox.exec()            

        else:
            messagebox = QMessageBox()
            messagebox.setText("You don't have any hints ")
            messagebox.exec()

    def reset(self):
        self.random_number = random.randint(1, 100)
        self.hints = 1
        self.hints_label.setText(f"You have {self.hints} hints left")
        self.entry.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())