#!/usr/bin/python3
"""The base class of the Airbnb"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines all common attributes/methods
    for other classes
    """
    def __init__(self, *args, **kwargs):
        """Initializes class BaseModel
        args:
            args - not used
            kwargs - arguments for the constructor of a
                        BaseModel
        attributes:
            created_at - time an instance is created
            upddated_at - time an instance is updated
            id - universal unique identifier for
                    each instance created
        """
        tformat = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                        value, tformat)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def save(self):
        """Updates the public instance attribute
        'updated_at' with current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all key/
        values of '__dict__' of the instance
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["id"] = self.id
        my_dict["updated_at"] = self.updated_at.isoformat()

        return my_dict

    def __str__(self):
        """Returns a string of class name, id, and dictionary"""
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)
