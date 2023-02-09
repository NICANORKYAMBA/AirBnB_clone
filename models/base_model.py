#!/usr/bin/python3
"""The base class of the Airbnb"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines all common attributes/methods
    for other classes
    """

    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

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
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
                if 'id' not in kwargs:
                    self.id = str(uuid.uuid4())
                if 'created_at' not in kwargs:
                    self.created_at = datetime.now()

                if 'created_at' in kwargs and 'updated_at' not in kwargs:
                    self.updated_at = self.created_at
                else:
                    self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

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
        models.storage.new(self)
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
