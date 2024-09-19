#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.stock import Stock
from os import getenv

storage = FileStorage()
storage.reload()
