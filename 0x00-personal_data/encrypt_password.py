#!/usr/bin/env python3
"""
Password Encryption Module
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Encrypts/Hashes the password
    """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates if the password matches the hashed password.
    """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
