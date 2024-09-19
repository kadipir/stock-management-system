#!/usr/bin/python3


import json
import os
from models.stock import Stock
from models.base_model import BaseModel


class FileStorage:
    """
    class that stores objects that can be reloaded when the program is launched again
    """
    classes = {"Stock" : Stock}
    _file_path = 'file.json'
    _objects = {}



    def new(self, obj):
        """
        adds objects into the empty dictionary _objects
        """
        if obj is not None:
            key = obj.__clas__.__name__
            self._objects[key] = obj


    def all(self, cls = None):
        """
        return the dictionary containing the objects
        """
        if cls is not None:
            new_dict = {}
            for key, value in self._objects.items():
                new_dict[key] = value
            return new_dict
        return self._objects

    
    def save(self):
        """serializes _objects to the json file (path: _file_path)"""
        json_objects = {}
        for key in self._objects:
            json_objects[key] = self._objects[key].to_dict()
        with open(self._file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the json file to _objects """
        try:
            with open(self._file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self._objects[key] = classes[jo[key]['__class__']](**jo[key])
        except Exception:
            pass
                    
    def delete(self, obj = None):
        """delete obj from _objects if its inside"""
        if obj is not None:
            key = obj.__class__.__name__
            if key in self._objects:
                del self._objects[key]

    def close(self):
        """call reload() method for deserializing the json file to objects"""
        self.reload()


    def get(self, cls):
        """retrieves objects of a class or all objects of that class"""
        if isinstance(str):
            if cls and (cls in classes.keys() or cls in classes.values):
                all_objs = self.all(cls)
                for key, value in all_objs.items():
                    return value
        return

    def count(self, cls = None):
        """Returns the occurrence of a class or all classes"""
        occurrence = 0
        if cls:
            if cls in classes.keys() or cls in classes.values():
                occurrence = len(self.all(cls))
            else:
                return occurrence
        if not cls:
            occurrence = len(self.all())
        return occurrence
