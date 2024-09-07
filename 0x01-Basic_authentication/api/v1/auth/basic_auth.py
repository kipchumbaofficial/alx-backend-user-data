#!/usr/bin/env python3
'''basic_auth module:
    Manages Basic Auth
'''
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


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

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """Gets user object
        """
        if not user_email or not isinstance(user_email, str):
            return None
        if not user_pwd or not isinstance(user_pwd, str):
            return None

        user_list = User.search({'email': user_email})
        if not user_list:
            return None
        user = user_list[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves Current user"""
        authorization = self.authorization_header(request)
        base64_auth = self.extract_base64_authorization_header(authorization)
        decoded_header = self.decode_base64_authorization_header(base64_auth)
        user_email, user_pwd = self.extract_user_credentials(decoded_header)

        user = self.user_object_from_credentials(user_email, user_pwd)
        return user
