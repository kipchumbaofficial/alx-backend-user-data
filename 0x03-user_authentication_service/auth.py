#!/usr/bin/env python3
""" Athentication module
"""
from sqlalchemy.exc import InvalidRequestError
from db import DB
import bcrypt
from user import User


def _hash_password(password: str) -> bytes:
    """ Hash password for storage
    """
    new_pwd = password.encode('utf-8')
    hashed_pwd = bcrypt.hashpw(new_pwd, bcrypt.gensalt())
    return hashed_pwd


class Auth:
    """ Auth class to interact with the authentication database.
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers a new user
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f'User {email} already exists')
        except InvalidRequestError:
            hashed_pwd = _hash_password(password)
            new_user = self._db.add_user(email, hashed_pwd)
        return new_user
