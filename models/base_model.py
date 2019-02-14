#!/usr/bin/python3
"""
    Module containing the ``BaseModel`` class.
"""
from datetime import datetime
import uuid

class BaseModel:
    """
        BaseModel Class.
    """

    def __init__(self):
        """ Initializing an instance of ``BaseModel``.
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
            Returns a string representation of ``BaseModel`` instance.
        """
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id,
            self.__dict__)

    def save(self):
        """
            Updates `updated_at`.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            Returns a dictionary containing instance dict, instance __class__,
            but also, created_at, updated_at in ISO format.
        """
        i_dict = {}
        for key, val in self.__dict__.items():
            i_dict[key] = val
        i_dict['__class__'] = self.__class__.__name__
        i_dict['created_at'] = self.created_at.isoformat()
        i_dict['updated_at'] = self.updated_at.isoformat()

        return i_dict