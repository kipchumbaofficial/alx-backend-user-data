#!/usr/bin/env python3
""" Session Auth Implementation
"""
from .auth import Auth
import uuid


class SessionAuth(Auth):
    """ SessionAuth:
    Handle Session Authentication Logics
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ create_session
        Returns:
            Session ID for a user_id
        """
        if user_id:
            if isinstance(user_id, str):
                session_id = str(uuid.uuid4())
                SessionAuth.user_id_by_session_id[session_id] = user_id
                return session_id
        return None
