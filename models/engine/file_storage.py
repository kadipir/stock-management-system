#!/usr/bin/python3


import json
import os 
from models.base_model import BaseModel


class FileStorage:
    """
    class that stores objects that can be reloaded when the program is launched again
    """
    _file_path = 'file.json'
    _objects = {}



    def new(self, obj):
        """
        adds objects into the empty dictionary __objects
        """
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name,obj.id)
        FileStorage._objects[key] = obj


    def all(self):
        """
        return the dictionary containing the objects
        """
        return FileStorage._objects


    
    def save(self):
        all_objs = FileStorage.__objects
        obj_dict = {}
        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()
        with open(FileStorage.__file_path, "w", encoding = "utf-8") as file:
            json.dump(obj_dict, file)



    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__fil_path, "r", encoding = "utf-8") as file:
                try:
                    obj_dict = json.load(file)
                    for key, values in obj_dict.items():
                        class_name, obj_id = key.split(".")
                        cls = eval(class_name)
                        instance = cls(**values)
                        FileStorage.__object[key] = instance
                except Exception:
                    pass
                    
