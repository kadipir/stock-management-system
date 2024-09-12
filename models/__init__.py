#!/usr/bin/python3
"""
create a unique FileStorage instance for my application
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from os import getenv


storage = FileStorage()
storage.reload


