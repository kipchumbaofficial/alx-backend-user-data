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
