from cryptography.fernet import Fernet

# Generate a secret key
secret_key = b'sgu198qcuXNDvLRCUdaZi7F75Al5wy85QMZHTuDmTxM='
cipher_suite = Fernet(secret_key)

def encrypt_data(value):
    encrypted_value = cipher_suite.encrypt(value.encode())
    return encrypted_value.decode()