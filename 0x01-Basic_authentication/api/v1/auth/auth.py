#!/usr/bin/env python3
""" The Auth class module
"""
from flask import request
from typing import TypeVar, List


class Auth:
    """ Auth class base class of all the authentications
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth:
        Returns: False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ authorization_header
        Returns: None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user
        Returns: None
        """
        return None
