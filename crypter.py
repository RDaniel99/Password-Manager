from cryptography.fernet import Fernet


# decrypt password using master_password as key
def decrypt(password, master_password):
    f = Fernet(master_password)
    password = password.encode()
    decrypted_password = f.decrypt(password)
    decrypted_password = decrypted_password.decode()
    return decrypted_password


# encrypt password using master_password as key
def encrypt(password, master_password):
    f = Fernet(master_password)
    password = password.encode()
    encrypted_password = f.encrypt(password)
    encrypted_password = encrypted_password.decode()
    return encrypted_password
