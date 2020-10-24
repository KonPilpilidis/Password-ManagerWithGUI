# Cryptography packages
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Auxiliary packages
from random import choice,sample
from string import ascii_letters, digits, punctuation
import csv
from configparser import ConfigParser

# File System
STORAGE = "archive.csv"

class Manager(object):
    """
    The object contains the general functions necessary for the manager to work.
    """
    Users = 0
    def __init__(self):
        """
        Initializes the Manager object for a user:
        1. Creates the necessary files
        2. Generates the master key
        """
        Manager.Users += 1
        key = Fernet.generate_key()
        keyfile = f"./resources/key{Manager.Users}.key"
        configfile = f"./resources/config{Manager.Users}.ini"
        salt = ''
        for i in range(8):
            salt += str(choice(ascii_letters + digits + punctuation))
        with open(self.keyfile, "wb") as file:
            file.write(key)
        config_object = ConfigParser()
        config_object["globals"] = {"id":Manager.Users,
                                    "salt": salt,
                                    "key": keyfile,
                                    "config":configfile,
                                    "storage":0}
        with open(configfile, 'w') as file:
            file.write(configfile)
    def _getSalt(self):
        """
        Retrieves the salt used to generate the encryption key for the password.
        :return: str
        """
        config = ConfigParser()
        config.read('config.ini')
        return config['globals']['salt']
    def _getMasterKey():
        """
        Retrieves the master encryption key from the current directory named `key.key`
        :return: bytes
        """
        config = ConfigParser()
        config.read('config.ini')
        return open("key.key", "rb").read()
    def _setKey(self,username,masterpassword):
        """
        The method returns an en-/decryption key which is generated based on the username and the password after adding the
        salt.
        :param masterpassword: str for the masterpassword
        :return: bytes
        """
        salt = self._getSalt()
        masterkey = self._getMasterKey()
        passphrase = username + salt + masterpassword  # This is input in the form of a string
        passphrase = passphrase.encode()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=masterkey,
            iterations=100000,
            backend=default_backend()
        )
        return base64.urlsafe_b64encode(kdf.derive(passphrase))  # Can only use kdf once
    def login(self,username,masterpassword):




    def encrypt(self,passphrase, username, masterpassword):
        """
        The method encrypts a password. (Not necessarily created with the classes methods)
        :param passphrase: Message to encrypt
        :param username: str The user name with which the program will encrypt the passwords
        :param masterpassword: The password with which the program will encrypt the passwords
        :return: bytes
        """
        if type(passphrase) == bytes:
            toEncode = passphrase
        else:
            toEncode = passphrase.encode()
        cipher = Fernet(self._setKey(username, masterpassword))
        return cipher.encrypt(toEncode)
    def decrypt(self,toDecode, username, masterpassword):
        """
        The method encrypts a password. (Not necessarily created with the classes methods)
        :param toDecode: Message to decrypt (bytes or str)
        :param username: str The user name with which the program will encrypt the passwords
        :param masterpassword: The password with which the program will encrypt the passwords
        :return: bytes
        """
        cipher = Fernet(Manager.getKey(username, masterpassword))
        return cipher.decrypt(toDecode)
    def checkCredentials(self,username,password):

    def newEntry(self,**kwargs):
        config = ConfigParser()
        new_value = config['globals']['storage'] + 1
        config.set("globals", "storage", new_value)

    def save(self):
        pass
    def load(self):
        pass
    def changePass(self):
        pass
    # def save(self,password_obj):
    #     self.Stored += 1
    #     with open(STORAGE, 'a') as file:
    #         file.write(str(self.Stored) + ',' + bpass.decode('utf-8') + '\n')
class Password(object):
    """
    The object contains the functions to generate, encrypt and decrypt the password.
    """
    def __init__(self,method="random",**kwargs):
        """
        Creates a random password
        :param method: The type of password to produce
                    1. random: random alphanumerical password
                    2. diceware: a diceware password
        :param length: int number of characters or words
        **kwargs: For method = "diceware"
            words- Int number of words in the password
            lang - The language of the dictionary ('EN','DE')
            delimiters - The method with which to set the delimiters:
                "none": ' ' for all delimiters,
                "user": a user defined list of delimiters,
                "random": a random list of delimiters
            delimiter_list - list with length -1 characters (overrides delimiters)
        For method = "random"
            characters - Whether characters should be used in the password (True , False)
            digits - Whether digits should be used in the password (True , False)
            punctuation - Whether punctuation marks should be used in the password (True , False)
            char_length - how many characters to use in the password (overrides characters argument)          | If the sum of these
            digi_length - how many digits to use in the password (overrides digits argument)                  | elements differs from the length argument,
            punc_length - how many punctuation marks to use in the password (overrides punctuation argument)  | the length is adjusted.
            total_length- the total number of characters
        :return: str
        """
        self.method = method
        self.kwargs = kwargs
        if self.method == "diceware":
            self.phrase = self._generateDiceware()
        else:
            self.phrase = self._generateRandom()
    def _generateDiceware(self):
        """
        generates a diceware password
        :return: str
        """
        def readInDictionnairy():
            """
            The method read into memory the diceware dictionairy
            """
            if self.kwargs['lang'] == 'DE':
                reader = csv.reader(open("./resources/dicewaredict_DE.csv", 'r'), delimiter="\t")
            else:
                reader = csv.reader(open("./resources/dicewaredict_EN.csv", 'r'), delimiter="\t")
            dict_list = {}
            for line in reader:
                dict_list[line[0]] = line[1]
            return dict_list
        def diceRoll():
            """
            The method rolls a number of dice to select a word.
            """
            set = [str(i) for i in range(1,7)]
            roll = ""
            for i in range(5):
                roll += choice(set)
            return roll
        def check_parameters():
            """
            The method controls the arguments passed and brings them in a usable form for the parent function.
            :return: None
            """
            try:
                if type(int(self.kwargs["words"])) != int and self.kwargs["words"] < 3:
                    print("The number of words defined was either invalid or too small. The program defaulted to a 5-word password")
                    self.kwargs["words"] = 5
            except:
                self.kwargs["words"] = 5
            try:
                if self.kwargs['lang'] not in ("EN", "DE"):
                    print("The chosen language is not available. The program defaulted to an english dictionairy.")
                    self.kwargs['lang'] = "EN"
            except:
                self.kwargs['lang'] = "EN"
            try:
                if self.kwargs['delimiters'] not in ("none", "user", "random"):
                    print(
                        "The method you provided was not one of the valid methods for setting delimiters in a diceware password. The program defaulted to a password without delimiters.")
                    self.kwargs['delimiters'] = "none"
            except:
                try:
                    if len(self.kwargs['delimiter_list']) == self.kwargs["words"] - 1:
                        self.kwargs['delimiters'] = 'user'
                    else:
                        print("The provided list is either too small or too big. The program defaulted to setting the delimiters randomly.")
                        self.kwargs['delimiters'] = "random"
                except:
                    self.kwargs['delimiters'] = 'none'
        def setDelimiters():
            """
            The program returns a list of delimiters of length - 1
            :return: list
            """
            if self.kwargs['delimiters'] == "none":
                return [' '] * (self.kwargs["words"])
            elif self.kwargs['delimiters'] == "user":
                return self.kwargs['delimiter_list']
            else:
                delimiter_list = []
                for i in range(self.kwargs["words"]):
                    delimiter_list.append(choice(punctuation))
                return delimiter_list
        check_parameters()
        dictionary = readInDictionnairy()
        password = ""
        delimiters = setDelimiters()
        for i in range(self.kwargs["words"]-1):
            password += dictionary[diceRoll()] + delimiters[i]
        password += dictionary[diceRoll()]
        return password
    def _generateRandom(self):
        """
        Generates an alphanumerical password
        returns str
        """
        def setParamLength(param):
            if param == "character":
                return "char_length"
            elif param == "digit":
                return "digi_length"
            elif param == "punctuation":
                return "punc_length"
            else:
                return None
        def checkParameters():
            """
            The method checks the functions arguments and brings them in a usable for the parent method form
            :return: None
            """
            def checker(param):
                """
                The method tests whether a named argument was passed and it is valid and passes a valid argument if not.
                :param param: the element to check
                :return: None
                """
                param_len = setParamLength(param)
                try:
                    if self.kwargs[param] == True:
                        try:
                            if type(int(self.kwargs[param_len])) != int and self.kwargs[param_len] < 1:
                                print(f"The argument {param_len} is invalid. The program added 1 {param}s")
                                self.kwargs[param_len] = 1
                            else:
                                self.kwargs[param_len] = int(self.kwargs[param_len])
                        except:
                            self.kwargs[param_len] = 1
                    else:
                        try:
                            if type(int(self.kwargs[param_len])) != int and self.kwargs[param_len] < 1:
                                print(f"The argument {param_len} is invalid. The program excluded {param}s.")
                                self.kwargs[param_len] = 1
                                self.kwargs[param] = True
                        except:
                            self.kwargs[param_len] = 1
                            self.kwargs[param] = True
                except:
                    try:
                        if type(int(self.kwargs[param_len])) != int and self.kwargs[param_len] < 1:
                            print(f"The argument {param_len} is invalid. The program added 1 {param}s")
                            self.kwargs[param_len] = 1
                        else:
                            self.kwargs[param_len] = int(self.kwargs[param_len])
                            self.kwargs[param] = True
                    except:
                        self.kwargs[param_len] = 0
                        self.kwargs[param] = True
            for element in ['character','digit','punctuation']:
                checker(element)
            try:
                if self.kwargs["total_length"] < self.kwargs["digi_length"] + self.kwargs["punc_length"] + self.kwargs["char_length"]:
                    print("The designated total length is smaller that the sum of the required elements. The designated length was adjusted upwards.")
                    self.kwargs["total_length"] = self.kwargs["digi_length"] + self.kwargs["punc_length"] + self.kwargs["char_length"]
                    return 0
                elif self.kwargs["total_length"] > self.kwargs["digi_length"] + self.kwargs["punc_length"] + self.kwargs["char_length"]:
                    return self.kwargs["total_length"] - self.kwargs["digi_length"] - self.kwargs["punc_length"] - self.kwargs["char_length"]
            except:
                if self.kwargs["digi_length"] + self.kwargs["punc_length"] + self.kwargs["char_length"] < 4:
                    self.kwargs["total_length"] = 16
                    return 16
                else:
                    self.kwargs["total_length"] = self.kwargs["digi_length"] + self.kwargs["punc_length"] + self.kwargs["char_length"]
                return 0
        def compileCharacters(addOn):
            elements = []
            for param in ['char_length','digi_length','punc_length']:
                if self.kwargs[param] != 0:
                    for element in range(self.kwargs[param]):
                        if param == 'char_length':
                            elements.append(str(choice(ascii_letters )))
                        elif param == "digi_length":
                            elements.append(str(choice(digits)))
                        else:
                            elements.append(str(choice(punctuation)))
            for elem in range(addOn):
                elements.append(str(choice(ascii_letters * self.kwargs['character'] + digits * self.kwargs['digit'] + punctuation * self.kwargs['punctuation'])))
            return elements
        bag = compileCharacters(checkParameters())
        characters = sample(bag,self.kwargs["total_length"])
        password = ""
        return password.join(characters)
    def getPassword(self):
        """
        The method returns the password.
        :return: str
        """
        return self.phrase
