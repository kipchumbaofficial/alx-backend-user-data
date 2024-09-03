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
        return False

    def authorization_header(self, request=None) -> str:
        """authorization_header:
            Handles authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user:
            User invoking the API
        """
        return None
