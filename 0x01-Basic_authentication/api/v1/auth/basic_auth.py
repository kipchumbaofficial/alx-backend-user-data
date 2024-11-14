#!/usr/bin/env python3
""" Basic Auth Implementation
"""
import base64
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
