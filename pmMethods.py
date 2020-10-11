from random import choice
from string import ascii_letters, digits, punctuation
import cryptography
from cryptography.fernet import Fernet
import os

keyFile = "key.key"
passwordFile = "archive.csv"
USER = "user"
MASTER = "pass"
SALT = "a"

def createPassword(length = 8,characters = True, numbers = True, symbols = True):
    """
    1. creates a random password
    2. saves the hashed password
    :param length: number of characters of password
    :param characters: a boolean for whether the password should contain characters
    :param numbers: a boolean for whether the password should contain digits
    :param symbols: a boolean for whether the password should contain symbols
    :return: str password
    """
    assert type(length) == int and length > 3 and length < 32, "The size of the password must be an integer number between 3 and 20"

    def generatePassword():
        """
        Generates a password of length = arg1
        returns str
        """
        user_password = ""
        for i in range(length):
            user_password += choice(ascii_letters * characters + digits * numbers + punctuation * symbols)
        return user_password, USER + SALT + user_password + choice(ascii_letters) + MASTER
    def generateKey():
        """
        Generates a unique encryption key with which to encrypt each password and writes it on a file.
        returns byte and int
        """
        def count_keys():
            """
            Counts the number of passwords generated and writes the id of the password which can be decrypted with each key.
            """
            if os.path.isfile('./' + keyFile) and os.access('./' + keyFile, os.R_OK):
                with open(keyFile, 'r') as f:
                    i = 0
                    for i, l in enumerate(f,):
                        pass
                return i
            else:
                return 1
        key = Fernet.generate_key()
        i=count_keys()
        with open(keyFile, 'a') as file:  # Open the file as wb to write bytes
            file.write(str(i)+" "+str(key.decode("utf-8"))+"\n")  # The key is type bytes still
        return key, i
    key, index = generateKey()
    password, hashable_password = generatePassword()
    hashable_password = hashable_password.encode()
    f = Fernet(key)
    encrypted = f.encrypt(hashable_password)
    with open(passwordFile,'a') as file:
        file.write(str(index )+ ',' + encrypted.decode('utf-8') + '\n')
    return password

def decrypt(hash):
    pass

print(createPassword())