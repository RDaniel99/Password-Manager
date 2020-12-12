# Password-Manager

## Instructions
### Installation
```
pip3 install cryptography
pip3 install sqlite3
```
### Execution
```
python passmanager.py <password_file> <method> <website> <user> <pass>
```
* password_file = file with the password (base64 safe)
* method = { -list / -add / -remove / -get }
* For list, no args are needed
* For add, all args are needed
* For remove, only website and user are needed
* For get, only website is needed

## Future
### 2.0 - RELEASED
#### TO-DO:
* catch exceptions
* beautify formatting of results / error messages

## Current version
### 1.1 - RELEASED
#### TO-DO:
* ~~added update for existing accounts~~
* ~~added password as sample instead of file~~

## Old versions
### 1.0 - RELEASED
#### TO-DO:
* ~~solve bugs~~
* ~~create instructions in README.md~~
* ~~documentation PEP-8~~

### 0.3 - RELEASED
#### TO-DO:
* ~~exceptions for different cases~~
* ~~encryption/decryption~~

### 0.2 - RELEASED
#### TO-DO:
* ~~rest api for database~~

### 0.1 - RELEASED
~~### TO-DO:~~
* ~~added setup for create storage table~~
* ~~added orchestrator to separate functionalities~~
