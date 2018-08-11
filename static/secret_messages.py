import os
import random
import sys


class Affine():
    """Affine cipher"""

    def __init__(self):
        self.message = input("What is your message >").upper()
        self.numbered_letter = {number: letter for letter, number in zip([
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z' and ' '],
            range(0, 26))}
        self.affine_encrypt_numbers = []
        self.word_numbers = []
        self.crypt = ''
        self.crypted_words = []
        self.decrypt_message = ''
        self.decrypted_message = []

    def encrypt(self):
        """Affine encrypter"""
        print("\n")
        print("You chose Affine Encrypter")
        print("\n")
        print("Here is your Encryption")
        print("\n")
        for letters in self.message:
            for key, value in self.numbered_letter.items():
                if value == letters:
                    self.affine_encrypt_numbers.append(((5 * key) + 2) % 26)

        for numbers in self.affine_encrypt_numbers:
            for key, value in self.numbered_letter.items():
                if numbers == key:
                    self.crypt += "".join(value)
        print(self.crypt)
        print("\n")

    def decrypt(self):
        """Affine decrypter"""
        print("\n")
        print("You chose Affine Decrypter")
        print("\n")
        print("Here is your Decryption")
        print("\n")
        for letter in self.message:
            for key, value in self.numbered_letter.items():
                if letter == value:
                    self.word_numbers.append((((key + 24) * 21) % 26))

        for numbers in self.word_numbers:
            for key, value in self.numbered_letter.items():
                if numbers == key:
                    self.decrypt_message += ''.join(value)
        print(self.decrypt_message)
        print("\n")


class Keyword():
    """Keyword cipher"""

    def __init__(self):
        self.message = input("What is your message >").upper()
        self.affine_encrypt_numbers = []
        self.word_numbers = []
        self.keyword_crypt = {
            letter: keyword for keyword, letter in
            zip("KRYPTOSABCDEFGHIJLMNQUVWXZ ",
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
                }
        self.crypt = ''
        self.crypted_words = []
        self.decrypt_message = ''
        self.decrypted_message = []

    def encrypt(self):
        """Keyword encrypter"""
        print("\n")
        print("You chose Keyword Encrypter")
        print("\n")
        print("Here is your Encryption")
        print("\n")
        for letter in self.message:
            for key, value in self.keyword_crypt.items():
                if value == letter:
                    self.crypt += "".join(key)
        print(self.crypt)
        print("\n")

    def decrypt(self):
        """Keyword decrypter"""
        print("\n")
        print("You chose Keyword Decrypter")
        print("\n")
        print("Here is your Decryption")
        print("\n")
        for letter in self.message:
            for key, value in self.keyword_crypt.items():
                if key == letter:
                    self.decrypt_message += ''.join(value)
        print(self.decrypt_message)
        print("\n")


class ADFGX():
    """ADFGX cipher"""

    def __init__(self):
        self.message = input("What is your message >").upper()
        self.crypt = ''
        self.crypted_words = []
        self.combine = []
        self.letters = "ADFGX "
        for letter in self.letters:
            self.combine.append("A" + letter)
            self.combine.append("D" + letter)
            self.combine.append("F" + letter)
            self.combine.append("G" + letter)
            self.combine.append("X" + letter)
            continue
            self.combine.append(" " + " ")
        self.adfgx_numbered_letter = {
            two_letters: number for two_letters, number in
            zip(self.combine, [
                'A', 'B', 'C', 'D', 'E', 'F',
                'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z', ' '])}
        self.n = 2
        self.message_split = [self.message[i:i+self.n] for i in
                              range(0, len(self.message), self.n)]
        self.decrypt_message = ''
        self.decrypted_message = []

    def encrypt(self):
        """ADFGX encrypter"""
        print("\n")
        print("You chose ADFGX Encrypter")
        print("\n")
        print("Here is your Encryption")
        print("\n")
        for letters in self.message:
            for key, value in self.adfgx_numbered_letter.items():
                if letters == value:
                    self.crypt += ''.join(key)
        print(self.crypt)
        print("\n")

    def decrypt(self):
        """ADFGX decrypter"""
        print("\n")
        print("You chose ADFGX Decrypter")
        print("\n")
        print("Here is your Decryption")
        print("\n")
        for letters in self.message_split:
            for key, value in self.adfgx_numbered_letter.items():
                if letters == key:
                    self.decrypt_message += ''.join(value)
        print(self.decrypt_message)
        print("\n")


def help():
    """help menu for the whole program"""
    print("What do you need help with?")
    print("\n")
    print("Help Menu")
    print("\n")
    print("     0. To learn about the program")
    print("     1. To learn about Affine Ciphers")
    print("     2. To learn about Keyword Cipher")
    print("     3. To learn about  ADFGX Cipher")
    print("     4. To go back to Main Menu")
    print("\n")
    print("     Enter the number you'd like to use? ")
    print("\n")


def encrypt_menu():
    """encrypt menu for the whole program"""
    print("Encrypt Menu:")
    print("\n")
    print("     1. To Encrypt with Affine Ciphers")
    print("     2. To Encrypt with Keyword Cipher")
    print("     3. To Encrypt with ADFGX Cipher")
    print("     4. To go back to Main Menu")
    print("\n")
    print("     Enter the number you'd like to use? ")
    print("\n")


def decrypt_menu():
    """decrypt menu for the whole program"""
    print("Decrypt Menu:")
    print("\n")
    print("     1. To Decrypt with Affine Cipher")
    print("     2. To Decrypt with Keyword Cipher")
    print("     3. To Decrypt with ADFGX Cipher")
    print("     4. To go back to Main Menu")
    print("\n")
    print("     Enter the number you'd like to use? ")
    print("\n")


def menu():
    """menu for the whole program"""
    print("Welcome to Secret Message")
    print("\n")
    print("  Secret Message Menu")
    print("\n")
    print("     0. Help")
    print("     1. Encrypt")
    print("     2. Decrypt")
    print("\n")
    print("    'Q' to quit ")
    print("\n")
    print("Enter the number for what you'd like")
    print("\n")


def goodbye_menu():
    clear()
    print("Goodbye! Hope you enjoyed this program!")
    print("\n")
    print("Please use again!")
    print("\n" * 5)
"""End of all Menus"""


def about():
    clear()
    print("   This program was created to encrypt and decrypt messages with")
    print("\n")
    print("three different ciphers: Affine, Keyword, and ADFGX. You would")
    print("\n")
    print("first want to encrypt a message. Then you should use that same ")
    print("\n")
    print("cipher to decrypt it. You also learn about each cipher by going")
    print("\n")
    print("back into the help menu. Press enter to head back to help menu")
    print("\n")


def keyword_info():
    clear()
    print(
        "A keyword cipher is a form of monoalphabetic \n"
        "substitution. A keyword is used as the key, and \n"
        "it determines the letter matchings of the cipher \n"
        "alphabet to the plain alphabet. Repeats of letters\n"
        " in the word are removed, then the cipher alphabet is \n"
        "generated with the keyword matching to A,B,C etc. until \n"
        "the keyword is used up, whereupon the rest of the ciphertext\n"
        "letters are used in alphabetical order, excluding those already\n"
        "used in the key."
         )
    print("\n")
    print("Plaintext:   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")
    print("Encrypted:   K R Y P T O S A B C D E F G H I J L M N Q U V W X Z")
    print("\n")


def affine_info():
    clear()
    print(
        "The affine cipher is a type of monoalphabetic \n"
        "substitution cipher, wherein each letter in an \n"
        "alphabet is mapped to its numeric equivalent,\n "
        "encrypted using a simple mathematical function,\n "
        "and converted back to a letter."
         )
    print("\n")
    print(
        "Each letter is enciphered with the function\n"
        " (ax + b) mod 26, where b is the magnitude\n"
        " of the shift."
         )
    print("\n")


def adfgx_info():
    clear()
    print(
        "The ADFGX cipher was created using a 5 x 5 polyburus. \n"
        "   A     D    F    G    X    \n"
        " A| a  | n  | c  | l  | p  | \n"
        " D| d  | o  | f  | z  | k  | \n"
        " F| q  | h  | v  | s  | w  | \n"
        " G| g  |i/j | r  | l  | p  | \n"
        " X| m  | b  | e  | t  | y  | \n"
        )
    print("Example: the message 'This is War'")
    print("\n")
    print("Would translate to:")
    print("\n")
    print("XGFDGDGGD GDGGD FXAAFG")
    print("\n")
"""End info for all ciphers and program"""


def error_message():
    clear()
    print(input(
        "You must enter 1 for 'Affine', 2 for 'Keyword' or 3 for 'ADFGX'"
        ))


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
"""Start of the script"""
if __name__ == "__main__":
    clear()
    main_input = input("Press 'Enter' to begin. ")
    while main_input != "Q":
        clear()
        menu()
        main_input = input("").upper()
        if main_input == '0':
            while main_input != '4':
                clear()
                help()
                main_input = input("")

                if main_input == '0':
                    about()
                    print(input("Press enter to head back to the help menu"))
                    clear()
                    help()

                if main_input == '1':
                    affine_info()
                    print(input("Press enter to head back to the help menu"))
                    clear()
                    help()

                if main_input == '2':
                    keyword_info()
                    print(input("Press enter to head back to the help menu"))
                    clear()
                    help()

                if main_input == '3':
                    adfgx_info()
                    print(input("Press enter to head back to the help menu"))
                    clear()
                    help()
            else:
                continue

        elif main_input == '1':
            while main_input != '4':
                clear()
                encrypt_menu()
                main_input = input("")
                if main_input == '1':
                    clear()
                    one = Affine().encrypt()
                    print(input("Press Enter"))
                elif main_input == '2':
                    clear()
                    two = Keyword().encrypt()
                    print(input("Press Enter"))
                elif main_input == '3':
                    clear()
                    three = ADFGX().encrypt()
                    print(input("Press Enter"))
                elif main_input == '4':
                    break
                else:
                    error_message()
            else:
                continue

        elif main_input == '2':
            while main_input != '4':
                clear()
                decrypt_menu()
                main_input = input("")
                if main_input == '1':
                    clear()
                    four = Affine().decrypt()
                    print(input("Press Enter"))
                elif main_input == '2':
                    clear()
                    five = Keyword().decrypt()
                    print(input("Press Enter"))
                elif main_input == '3':
                    clear()
                    six = ADFGX().decrypt()
                    print(input("Press Enter"))
                elif main_input == '4':
                    break
                elif main_input == '0':
                    help()
                else:
                    error_message()
            else:
                continue
        elif main_input == 'Q':
            clear()
            goodbye_menu()
            break
        else:
            clear()
            print(input("You must pick 1 to 'Encrypt' or 2 to 'Decrypt' "))
            continue
    else:
        goodbye_menu()
        clear()
