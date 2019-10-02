import hashlib
import random
import string

secret_key = 'key'


def generate_random_string(length=10):
    """Generate a random string of fixed length. """
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def encrypt_password(password, salt):
    """encrypt user's password."""
    return hash_md5(password+salt+secret_key)


def is_right_password(input_password, salt, encrypted_password):
    """To determine the password input is right or not."""
    input_encrypt = encrypt_password(input_password, salt)
    return True if input_encrypt == encrypted_password else False


def hash_md5(s):
    """md5 some strings."""
    return hashlib.md5(s.encode()).hexdigest()
