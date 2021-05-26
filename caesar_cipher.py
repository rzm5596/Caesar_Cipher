# Project:      Caesar Cipher Encrypter/Decrypter
# Author:       Ryan Mayes
# Date Started: 2021-5-25
# Date Edited:  2021-5-26



# Imports
import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QLineEdit, QTextEdit, QWidget, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon


# Defining the encrypt function
def encrypt(message, shift):

    # If the shift is negative, then turn it positive
    if(shift < 0):
        temp = int(shift / 26)
        shift = shift + (temp + 1) * 26

    # Getting the shift of the function 
    shift = shift % 26

    # Creating a string for the new encrypted message
    new_message = ""

    # Going through each element in the message to encrypt it
    for i in message:

        # Checking for if it is apart of the alphabet
        if (i.isalpha()) == True:

            # Adding the shift
            shifted_i = ord(i) + shift

            # Since it is apart of the alphabet, first check whether it is a capital letter or not
            if (ord(i) < 91):

                # In this case it is a capital, so the limit is 65-90

                # Making sure the number isn't above the limit
                if(shifted_i > 90):

                    # Fixing it if it was above the limit
                    shifted_i = shifted_i - 26

            else:
                # In this case it is a lowercase, so the limit is 97-122

                # Making sure the number isn't above the limit
                if(shifted_i > 122):

                    # Fixing it if it was above the limit
                    shifted_i = shifted_i - 26

            # Adding the encrypted character to the new message
            new_message += chr(shifted_i)

        # If not, just keep it the same
        else:
            new_message += i

    # Returning the encrypted message
    return new_message



# Defining the encrypt function
def decrypt(message, shift):

    # If the shift is negative, then turn it positive
    if(shift < 0):
        temp = int(shift / 26)
        shift = shift + (temp + 1) * 26

    # Getting the shift of the function 
    shift = shift % 26

    # Creating a string for the new encrypted message
    new_message = ""

    # Going through each element in the message to encrypt it
    for i in message:

        # Checking for if it is apart of the alphabet
        if (i.isalpha()) == True:

            # Adding the shift
            shifted_i = ord(i) - shift

            # Since it is apart of the alphabet, first check whether it is a capital letter or not
            if (ord(i) < 91):

                # In this case it is a capital, so the limit is 65-90

                # Making sure the number isn't below the limit
                if(shifted_i < 65):

                    # Fixing it if it was below the limit
                    shifted_i = shifted_i + 26

            else:

                # In this case it is a lowercase, so the limit is 97-122

                # Making sure the number isn't below the limit
                if(shifted_i < 97):

                    # Fixing it if it was below the limit
                    shifted_i = shifted_i + 26

            # Adding the encrypted character to the new message
            new_message += chr(shifted_i)

        # If not, just keep it the same
        else:
            new_message += i

    # Returning the encrypted message
    return new_message



# Creating a class for creating a window
class Test(QWidget):

    # Defining the init for this class
    def __init__(self):

        super().__init__()  # Calling the init for the super class
        self.initUI()       # Calling the UI init function



    # Defining an init for the UI
    def initUI(self):

        # Creating a label and text box for the key
        self.shift = QLabel('Shift')
        self.shiftEdit = QLineEdit()

        # Creating a button and text box for the encryption
        self.encryptButton = QPushButton('Encrypt', self)
        self.encryptEdit = QTextEdit()
        self.encryptButton.clicked.connect(self.encryptClicked) # Connecting the button to a function when clicked

        # Creating a button and text box for the decryption
        self.decryptButton = QPushButton('Decrypt', self)
        self.decryptEdit = QTextEdit()    
        self.decryptButton.clicked.connect(self.decryptClicked) # Connecting the button to a function when clicked

        # Setting up the grid layout
        grid = QGridLayout()
        grid.setSpacing(10)     

        # Setting the widgets on the grid
        grid.addWidget(self.shift, 1, 0)
        grid.addWidget(self.shiftEdit, 1, 1)

        grid.addWidget(self.encryptButton, 2, 0)
        grid.addWidget(self.encryptEdit, 2, 1, 4, 1)

        grid.addWidget(self.decryptButton, 5, 0)
        grid.addWidget(self.decryptEdit, 5, 1, 7, 1)

        # Setting the layout to the grid
        self.setLayout(grid)
        
        self.resize(720, 480)                   # Resizing the window
        self.center()                           # Centering the window
        self.setWindowTitle("Caesar Cipher")    # Setting the title of the window
        self.setWindowIcon(QIcon('web.png'))    # Setting the window icon

        self.show() # Bringing the window to the screen for the user



    # Defining what happens when the window is closed
    def closeEvent(self, event):

        # Prompting a message box when the program is exited
        reply = QMessageBox.question(self, 
                                    'Quit?', # Titlebar message
                                     "Are you sure you want to quit?", # Dialog message
                                     QMessageBox.Yes | QMessageBox.No, # Buttons appearing in the dialog
                                     QMessageBox.No) # Default selected button

        # Checking the reply
        if reply == QMessageBox.Yes:
            event.accept() # If yes, the application quits successfully
        else:
            event.ignore() # If no, the application does not quit



    # Defining a function for when the encrypt button is clicked
    def encryptClicked(self):

        key = int(self.shiftEdit.text())            # Getting the key
        message = self.encryptEdit.toPlainText()    # Getting the message
        self.encryptEdit.setPlainText(message)      # Repopulating the message in the text box
        cipherText = encrypt(message, key)          # Encrypting the message
        self.decryptEdit.setPlainText(cipherText)   # Showing the cipher text



    # Defining a function for when the encrypt button is clicked
    def decryptClicked(self):
        
        key = int(self.shiftEdit.text())            # Getting the key
        cipherText = self.decryptEdit.toPlainText() # Getting the cipher text
        self.decryptEdit.setPlainText(cipherText)   # Repopulating the cipher text in the text box
        message = decrypt(cipherText, key)          # Decrypting the cipher text
        self.encryptEdit.setPlainText(message)      # Showing the message


    # Defining a function for centering the window on the screen
    def center(self):

        qr = self.frameGeometry()                           # Creating a rectangle with the window's geometry
        cp = QDesktopWidget().availableGeometry().center()  # Figuring out the center point of the monitor
        qr.moveCenter(cp)                                   # Moving the center of the rectangle to the center of the monitor
        self.move(qr.topLeft())                             # Moving the window to the top left of the rectangle


# Defining the function for creating the window
def create_window():

    # Defining the application object and allowing it to be passed command line arguments
    app = QApplication(sys.argv)

    # Defining the window
    window = Test()

    # Running the GUI event loop
    sys.exit(app.exec_())



# Running the main function
if __name__ == "__main__":

    create_window()
