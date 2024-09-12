#!/usr/bin/env python3
"""Hash a password
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Returns:
        A salted hash of the input password
    """
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_pwd
