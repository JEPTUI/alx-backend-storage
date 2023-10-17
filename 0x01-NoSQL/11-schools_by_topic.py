#!/usr/bin/env python3
"""Defines a function that returns the list of school
having a specific topic"""


import pymongo


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    schools = list(mongo_collection.find({"topics": topic}))

    return schools
