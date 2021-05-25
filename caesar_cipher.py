# Project:      Caesar Cipher Encrypter/Decrypter
# Author:       Ryan Mayes
# Date Started: 2021-5-25
# Date Edited:  2021-5-25



# Imports
import sys
from PyQt5.QtWidgets import QApplication, QWidget



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



# Defining the function for creating the window
def create_window():

    # Defining the application object and allowing it to be passed command line arguments
    app = QApplication(sys.argv)

    # Defining the window
    window = QWidget()

    # Setting the size of the window
    window.setGeometry(0, 0, 500, 300)

    # Setting the title of the window
    window.setWindowTitle("Todo and Reminders")

    # Bringing the window to the screen for the user
    window.show()

    # Running the GUI event loop
    sys.exit(app.exec_())



# Running the main function
if __name__ == "__main__":
    #create_window()

    result = encrypt("abc", -28)

    print(result)