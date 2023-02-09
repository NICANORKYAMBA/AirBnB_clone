#!/usr/bin/python3
"""file storage class of Airbnb"""
import json
from models.base_model import BaseModel


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary '__objects'"""
        return self.__objects

    def new(self, obj):
        """Sets in '__objects' the obj with key
        '<obj class name>.id'"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes '__objects' to the JSON file
        (path:__file_path)"""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserializes the JSON file to '__objects'
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing.)"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value['__class__'])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def close(self):
        """Call reload method"""
        self.reload()
