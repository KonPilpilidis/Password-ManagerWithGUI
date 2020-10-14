<a><img src="https://github.com/KonPilpilidis/Password-ManagerWithGUI/blob/main/logo.ico" height="150" title="PasswordManagerLogo" alt="PasswordManagerLogo"></a>

<!-- [![Konstantinos Pilpilidis](https://avatars1.githubusercontent.com/u/71609885?s=400&u=c8c17cdd60c197a1003b0ae128c86069952caa4e)](http://pilpilidis.de) -->

# Password Manager

> A password manager that generates and stores passwords


[![Generic badge](https://img.shields.io/badge/Finished-No-red.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Version-0.0-green.svg)](https://shields.io/)

---

## Table of Contents

- [Features](##features)
- [Usage](##usage)
- [FAQ](##faq)
- [Support](#support)

---

### Setup
Before starting the program, an initialization takes place. The user chooses a user alias and a 
master-password. This information is used to encode the passwords. If the user loses or forgets 
the master-password, the passwords cannot be encoded. Multiple users can use the programm.
>!!!! The master-password is not saved. Only the user can decode the password.!!!!
- If you want more syntax highlighting, format your code like this:


```shell
$ brew update
$ brew install fvcproductions
```

##Features
### Password generation
<ul>
<li> <em>Random Alphanumerical password</em>: The program generates a password of a user defined length after the user 
chooses which groups of ASCII characters to include (letters, numbers, punctuation symbols).
<li> <em> Diceware password</em>: The program generates a password containing a user defined number of words from a 
dictionnairy separated by a user defined delimiter.
</ul>

### Password hashing
The programm peppers and salts the password and hashes the password using a uniquely generated Fernet key
### Password storage
## Usage (Optional)
## Documentation (Optional)
## Tests (Optional)

- Going into more detail on code and technologies used
- I utilized this nifty <a href="https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet" target="_blank">Markdown Cheatsheet</a> for this sample `README`.


##FAQ

- **How do I do *specifically* so and so?**
    - No problem! Just do this.

---

## Support

Reach out to me at one of the following places!

- Website: <a href="http://pilpilidis.de" target="_blank">`pilpilidis.de`</a>
- E-mail: <a href="mailto:konstantinos.pilpilidis@pilpilidis.de" target="_blank">`konstantinos.pilpilidis@pilpilidis.de`</a>
- Twitter: <a href="http://twitter.com/PilpilidisK" target="_blank">`@PilpilidisK`</a>
---
Copyright 2020 © <a href="http://pilpilidis.de" target="_blank">Pilpilidis Konstantinos</a>.
