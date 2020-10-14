from random import choice
from string import ascii_letters, digits, punctuation
import cryptography
from cryptography.fernet import Fernet
import csv
import os
from configparser import ConfigParser

keyFile = "key.key"
passwordFile = "archive.csv"
USER = "user"
MASTER = "pass"
SALT = "a"

class Backend(object):
    # Configure the program for the user


    # Get the configparser object
    config_object = ConfigParser()

    # Assume we need 2 sections in the config file, let's call them USERINFO and SERVERCONFIG
    config_object["USERINFO"] = {
        "admin": "Chankey Pathak",
        "loginid": "chankeypathak",
        "password": "tutswiki"
    }

    config_object["SERVERCONFIG"] = {
        "host": "tutswiki.com",
        "port": "8080",
        "ipaddr": "8.8.8.8"
    }

    # Write the above sections to config.ini file
    with open('config.ini', 'w') as conf:
        config_object.write(conf)

        with open('key.key' , 'w') as fp:
            pass
        with open('archive.csv' , 'w') as fp:
            pass
        with open('config.conf' , 'w') as fp:
            pass

class Password(object):    
    @staticmethod
    def create(lengthChar = 8,lengthWord=4,characters = True, numbers = True, symbols = True,method = "random",delimiter=" "):
        """
        1. creates a random password
        2. saves the hashed password
        :param length: number of characters of password
        :param characters: a boolean for whether the password should contain characters
        :param numbers: a boolean for whether the password should contain digits
        :param symbols: a boolean for whether the password should contain symbols
        :return: str password
        """
        assert type(lengthChar) == int and lengthChar > 3 and lengthChar < 31, "The size of the password must be an integer number between 4 and 30"
        assert type(lengthWord) == int and lengthWord > 3 and lengthChar < 11, "The number of words in the password must be an integer number between 4 and 10"
        assert method in ('random','diceware'),"The chosen method is not available"
        def generateDiceware():
            def readInDictionnairy():
                """
                The method read into memory the diceware dictionairy
                """
                reader = csv.reader(open("dicewaredict.csv",'r'),delimiter="\t")
                dict_list = {}
                for line in reader:
                    dict_list[line[0]] = line[1]
                return dict_list
            def diceRoll():
                """
                The method rolls a number of dice to select a word.
                """
                set = ["1","2","3","4","5","6"]
                roll = ""
                for i in range(5):
                    roll += choice(set)
                return roll
            dictionnairy = readInDictionnairy()
            password = ""
            for i in range(lengthWord):
                password += dictionnairy[diceRoll()] + delimiter
            return password
        def generateRandom():
            """
            Generates a password of length = arg1
            returns str
            """
            password = ""
            for i in range(lengthChar):
                password += choice(ascii_letters * characters + digits * numbers + punctuation * symbols)
            return password
        if method == "random":
            return generateRandom()
        else:
            return generateDiceware()
    
    @staticmethod
    def encryptForSave(password):
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
                        for i, l in enumerate(f,2):
                            pass
                    return i
                else:
                    return 1
            key = Fernet.generate_key()
            i=count_keys()
            with open(keyFile, 'a') as file:  # Open the file as wb to write bytes
                file.write(str(i)+" "+str(key.decode("utf-8"))+"\n")  # The key is type bytes still
            return key, i
        def saltPepperPass():
            with open("config.conf",'r'):

            distorted = USER + SALT + password + choice(ascii_letters) + MASTER
            return distorted.encode()
        key, index = generateKey()
        cipher = Fernet(key)
        hashed_password = cipher.encrypt(saltPepperPass())
        with open(passwordFile,'a') as file:
            file.write(str(index )+ ',' + hashed_password.decode('utf-8') + '\n')
        print(hashed_password)
    
    def decrypt(hash):
        pass
print(Password.encryptForSave(Password.create(method="diceware")))