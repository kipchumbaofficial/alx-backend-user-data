#!/usr/bin/env python3
""" Basic Auth Implementation
"""
import base64
from .auth import Auth
from models.user import User
from typing import TypeVar


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode_base64_authorization_header:
        Returns:
            Decode value of a Base64 string
        """
        if base64_authorization_header:
            if isinstance(base64_authorization_header, str):
                try:
                    # Try to decode the Base64 String
                    decoded_bytes = base64.b64decode(
                            base64_authorization_header
                            )

                    # Convert the decoded bytes to a UTF-8 string
                    utf8_string = decoded_bytes.decode('utf-8')

                    return utf8_string
                except (base64.binascii.Error,
                        ValueError, UnicodeDecodeError):
                    return None
        return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ extract_user_credentials:
        Returns:
            The user email and password from the Base64 decoded value
        """
        if decoded_base64_authorization_header:
            if isinstance(decoded_base64_authorization_header, str):
                if ':' in decoded_base64_authorization_header:
                    data = decoded_base64_authorization_header.split(':', 1)
                    email, password = data
                    return email, password
        return None, None

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ user_object_from_credentials:
        Returns
            The User instance based on his email and password
        """
        if user_email and isinstance(user_email, str):
            if user_pwd and isinstance(user_pwd, str):
                try:
                    users = User.search({'email': user_email})
                    for user in users:
                        if user.is_valid_password(user_pwd):
                            return user
                except Exception:
                    return None

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user:
        Returns:
            the User instance for a request
        """
        header = self.authorization_header(request)
        if not header:
            return None

        base64_encoded = self.extract_base64_authorization_header(header)
        if not base64_encoded:
            return None

        utf8 = self.decode_base64_authorization_header(base64_encoded)
        if not utf8:
            return None

        email, password = self.extract_user_credentials(utf8)
        if not email or not password:
            return None

        return self.user_object_from_credentials(email, password)
