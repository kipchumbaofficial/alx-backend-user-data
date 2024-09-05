#!/usr/bin/env python3
'''basic_auth module:
    Manages Basic Auth
'''
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """BasicAuth:
        Basic Authentication logic
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        """Returns the value after the authentication scheme
        """
        if not authorization_header:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic'):
            return None
        details = None
        if len(authorization_header.split(" ", 1)) == 2:
            details = authorization_header.split(" ", 1)[1]
        return details

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """Returns decoded authorization headeer
        """
        if not base64_authorization_header:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded = decoded_bytes.decode('utf-8')
            return decoded
        except Exception as e:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """Extracts user credential from decoded header"""
        if not decoded_base64_authorization_header:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        credentials = decoded_base64_authorization_header.split(':', 1)
        return credentials[0], credentials[1]
