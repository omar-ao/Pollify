#!/usr/bin/python3
"""
Initialize the models
"""


from models.engine.db_storage import DBStorage
storage = DBStorage()
storage.reload()
