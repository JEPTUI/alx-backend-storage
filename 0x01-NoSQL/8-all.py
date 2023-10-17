#!/usr/bin/env python3
"""Defines a function that lists all documents in a collection"""


import pymongo


def list_all(mongo_collection):
    """Returns lists of all documents or empty list
    if no document in the collection"""
    documents = list(mongo_collection.find({}))
    
    if not documents:
        return []

    return documents
