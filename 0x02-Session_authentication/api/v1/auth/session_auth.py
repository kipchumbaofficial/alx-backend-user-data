#!/usr/bin/env python3
""" Session Auth Implementation
"""
from .auth import Auth
import uuid
from models.user import User


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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ user_id_for_session_id:
        Return:
            User ID based on Session ID
        """
        if session_id:
            if isinstance(session_id, str):
                return SessionAuth.user_id_by_session_id.get(session_id)
        return None

    def current_user(self, request=None):
        """ Retrieves a User instance based on cookie value:
        """
        session_id = self.session_cookie(request)
        if not session_id:
            return None

        user_id = self.user_id_for_session_id(session_id)

        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """ Deletes a session
        """
        if request:
            cookie = self.session_cookie(request)
            if cookie:
                if self.user_id_for_session_id(cookie):
                    del self.user_id_by_session_id[cookie]
                    return True
        return False
