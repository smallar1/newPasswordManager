from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
import pwinput


def generate_key():
    return Fernet.generate_key()


def encrypt_password(key, password):
    fern = Fernet(key)
    encrypted_password = fern.encrypt(password.encode())
    return encrypted_password


def decrypt_password(key, encrypted_password):
    fern = Fernet(key)
    password = fern.decrypt(encrypted_password.encode())
    return password.decode()


def hash_function(string):
    byte_string = string.encode()

    hash_obj = hashes.Hash(hashes.SHA256())
    hash_obj.update(byte_string)

    hashed_str = hash_obj.finalize()
    return hashed_str
