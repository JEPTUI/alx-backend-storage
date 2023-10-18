#!/usr/bin/env python3
"""
Defines function that inserts a new document in a collection based on kwargs
"""


import pymongo


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs
    and returns the new _id"""
    new_doc = mongo_collection.insert_one(kwargs)

    return new_doc.inserted_id
