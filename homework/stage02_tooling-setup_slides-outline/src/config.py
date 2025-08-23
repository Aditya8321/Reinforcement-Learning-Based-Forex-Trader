# src/config.py
import os
from dotenv import load_dotenv

def load_env():
    """
    Load variables from .env into the environment.
    """
    load_dotenv()

def get_key(key_name):
    """
    Retrieve a value for the given environment variable name.
    Returns None if the key does not exist.
    """
    return os.getenv(key_name)
