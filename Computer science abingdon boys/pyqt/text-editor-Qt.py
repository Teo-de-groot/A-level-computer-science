import sys
import PyQt6.QtWidgets as qtw
from PyQt6.QtGui import QFont, QFontDatabase


class Mainwindow(qtw.QMainWindow):
   def __init__(self, app):
       super().__init__()
       self.app = app
       self.setWindowTitle("Everybody is Kungfu text editing")


       layout = qtw.QVBoxLayout()


       self.textedit = qtw.QTextEdit()
       layout.addWidget(self.textedit)


       buttons = qtw.QHBoxLayout()


       self.open_button = qtw.QPushButton("Open")
       self.open_button.clicked.connect(self.open)


       self.save_button = qtw.QPushButton("Save")
       self.save_button.clicked.connect(self.save)


       self.quit_button = qtw.QPushButton("Quit")
       self.quit_button.clicked.connect(self.cancel)
       self.silly()


       buttons.addStretch()
       buttons.addWidget(self.open_button)
       buttons.addWidget(self.save_button)
       buttons.addWidget(self.quit_button)
       buttons.addStretch()


       layout.addLayout(buttons)


       widget = qtw.QWidget()
       widget.setLayout(layout)
       self.setCentralWidget(widget)

   def silly(self):
        available_fonts = QFontDatabase.families()

        preferred_fonts = [
            "Wingdings",        
            "Zapf Dingbats",    
            "Symbol",           
        ]
        for font_name in preferred_fonts:
            if font_name in available_fonts:
                font = QFont(font_name, 16)
                self.textedit.setFont(font)
                return

   def cancel(self):
       self.app.quit()


   def open(self):
       filename, _ = qtw.QFileDialog.getOpenFileName(
           self, "Open File", "", "Text Files (*.txt *.html)"
       )
       if filename:
           with open(filename, "r", encoding="utf-8") as file:
               self.textedit.setPlainText(file.read())


   def save(self):
       filename, _ = qtw.QFileDialog.getSaveFileName(
           self, "Save File", "", "Text Files (*.txt *.html)"
       )

       if filename:
           with open(filename, "w", encoding="utf-8") as file:
               file.write(self.textedit.toPlainText())


app = qtw.QApplication(sys.argv)
window = Mainwindow(app)
window.show()
app.exec()



