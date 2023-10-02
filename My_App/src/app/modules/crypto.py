from flet.security import encrypt, decrypt
from modules.FacadeBD import *

def encript_password(password):
    secret_key = "P4SSW0RD!"
    return encrypt(password, secret_key)

def verify_password(email, password):
    secret_key = "P4SSW0RD!"
    results = get_user(email)
    bd_email, bd_password = results[0]
    print(encrypt(password, secret_key))
    print(bd_password)
    if (encrypt(password, secret_key) == bd_password):
        return True
    else:
        return False