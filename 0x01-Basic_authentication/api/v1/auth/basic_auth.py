#!/usr/bin/env python3
""" Basic Auth Implementation
"""
from .auth import Auth


class BasicAuth(Auth):
    """ BasicAuth Class
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """extract_base64_authorization_header:
        Returns:
            Base64 part of the Authorization header of Basic Auth
        """
        if authorization_header:
            if isinstance(authorization_header, str):
                if authorization_header.startswith('Basic '):
                    return authorization_header.split(' ', 1)[1]
        return None
