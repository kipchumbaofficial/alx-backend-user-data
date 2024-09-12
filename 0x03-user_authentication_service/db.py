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
        """Creates an new user in db
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Finds user by given keyword arguments
        """
        try:
            query = self._session.query(User)
            valid_columns = set([column.name
                                for column in User.__table__.columns])

            for key, value in kwargs.items():
                if key not in valid_columns:
                    raise InvalidRequestError("Invalid filter key")
                query = query.filter(getattr(User, key) == value)
            user = query.one()
            return user
        except NoResultFound as e:
            raise
        except InvalidRequestError as ire:
            raise

    def update_user(self, user_id: int, **kwargs) -> None:
        """Updates user
        """
        user = self.find_user_by(id=user_id)
        valid_columns = set([column.name
                            for column in User.__table__.columns])
        for key, value in kwargs.items():
            if key not in valid_columns:
                raise ValueError("Argument doesn't match any attribute")
            user.key = value
        self._session.commit()
