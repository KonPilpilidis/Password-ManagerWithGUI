*******************************
|logo| Password Manager (GUI)
*******************************
.. |logo| image:: logo.ico
    :width: 80
    :align: middle

The Password Manager (GUI) is a python package that generates (and stores) passwords.

Installation
###############################
To install the package, you can use:
::

    pip install ...

Features
###############################
- Generate passwords:
    - random alphanumerical sequences
        - Each digit is chosen using the method *random.choice*.
        - The user can define which types of ASCII characters to include in the password:
            - digits,
            - letters,
            - punctuation.
    - diceware passwords:
        - The user can choose between an dictionary in:
            - English or
            - German
        - The user can choose to include:
            - no punctuation (*none*),
            - add punctuation between any two words (*user*) or
            - allow the program to add random punctuation at any point (*random*).
- Archive generated passwords or archive user-defined passwords: [#]_
    - retrieve passwords
    - update passwords in archive

.. [#] The passwords are encrypted using a Fernet key generated based on the username and password. The encryption uses AES in CBC mode with a 128-bit key; using PKCS7 padding. The username and password are not saved.

Contributing
###############################
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

License
###############################
`MIT <https://choosealicense.com/licenses/mit/>`_

Support
###############################
Reach out to me at one of the following places!

- Website: `pilpilidis.de <https://pilpilidis.de>`_
- E-mail: `konstantinos.pilpilidis@pilpilidis.de <mailto:konstantinos.pilpilidis@pilpilidis.de>`_
- Twitter: `@PilpilidisK <http://twitter.com/PilpilidisK>`_