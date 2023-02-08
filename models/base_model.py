#!/usr/bin/python3
"""The base class of the Airbnb"""
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods
    for other classes
    """

    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self):
        """Initializes class BaseModel
        attributes:
            created_at - time an instance is created
            upddated_at - time an instance is updated
            id - universal unique identifier for
                each instance created
        """
        self.created_at = BaseModel.created_at
        self.id = BaseModel.id
        self.updated_at = BaseModel.updated_at

    def __str__(self):
        """Returns a string of class name, id, and dictionary
        """
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute
        'updated_at' with current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all key/
        values of '__dict__' of the instance
        """
        my_dict = dict(self.__dict__)
        my_dict['__class__'] = str(type(self).__name__)
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['id'] = self.id
        my_dict['updated_at'] = self.updated_at.isoformat()

        return my_dict
