#!/usr/bin/env python3
""" The Auth class module
"""
from flask import request
from typing import TypeVar, List
from os import getenv


SESSION_NAME = getenv('SESSION_NAME')


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
        if request:
            if 'Authorization' in request.headers:
                return request.headers.get('Authorization')
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user
        Returns: None
        """
        return None

    def session_cookie(self, request=None):
        """ session_cookie:
        Returns:
            A cookie value from a request
        """
        if request:
            return request.cookies.get(SESSION_NAME)
        return None
