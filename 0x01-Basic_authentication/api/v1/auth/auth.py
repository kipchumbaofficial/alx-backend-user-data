#!/usr/bin/env python3
"""auth module:
    Manages API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Manages API authentication
    """
    def require_auth(self, path: str,
                     excluded_paths: List[str]) -> bool:
        """require_auth:
            handles routes that require authentication
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path.endswith('/'):
            new_path = path
        else:
            new_path = path + '/'
        if new_path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """authorization_header:
            Handles authorization header
        """
        if request is None:
            return None
        header_value = request.header.get('Authorization')
        if header_value:
            return header_value
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user:
            User invoking the API
        """
        return None
