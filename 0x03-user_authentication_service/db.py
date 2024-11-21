#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Add user to the database
        """
        new_user = User(
                email=email,
                hashed_password=hashed_password
                )
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """ Find user by filtering with arbitrary keyword argument.
        """
        valid_keys = {column.name for column in User.__table__.columns}
        for key in kwargs:
            if key not in valid_keys:
                raise InvalidRequestError(f"Invalid filter key: {key}")

        # Perform the query using valid filters
        query = self._session.query(User).filter_by(**kwargs)
        user = query.first()

        if not user:
            raise NoResultFound(f"No user found for filters: {kwargs}")

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """ Update user data
        """
        user = self.find_user_by(id=user_id)
        for key in kwargs:
            if not hasattr(user, key):
                raise ValueError(f"Invalid values{kwargs.get(key)}")
            setattr(user, key, kwargs.get(key))

        self._session.commit()
        return None
