#!/usr/bin/python3
"""module that defines a class to manage file storage for hbnb clone"""
import json

from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """manages storage of hbnb models in JSON format"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return a dictionary of instantiated objects in __objects.

        If a cls is specified, returns a dictionary of objects of that type.
        Otherwise, returns the __objects dictionary.
        """
        if cls is not None:
            if isinstance(cls, str):
                cls = eval(cls)
            return {
                key: value
                for key, value in self.__objects.items()
                if isinstance(value, cls)
            }
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()["__class__"] + "." + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as file:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, file)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as file:
                temp = json.load(file)
                for key, val in temp.items():
                    self.all()[key] = classes[val["__class__"]](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Deletes obj from the __objects list """
        if obj is not None and hasattr(obj, "id"):
            # construct the key based on the object class and id
            key = obj.__class__.__name__ + "." + obj.id

            # delete the object if it exists in the __objects list
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """ Calls reload() for deserializing JSON file to objects """
        self.reload()    
