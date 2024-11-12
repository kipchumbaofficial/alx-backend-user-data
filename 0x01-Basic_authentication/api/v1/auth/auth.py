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
        if not path or not excluded_paths:
            return True
        if not path.endswith("/"):
            path += "/"
        if path in excluded_paths:
            return False
        else:
            return True
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
