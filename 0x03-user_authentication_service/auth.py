#!/usr/bin/env python3
""" Athentication module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Hash password for storage
    """
    new_pwd = password.encode('utf-8')
    hashed_pwd = bcrypt.hashpw(new_pwd, bcrypt.gensalt())
    return hashed_pwd
