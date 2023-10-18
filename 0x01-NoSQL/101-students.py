#!/usr/bin/env python3
"""
Defines function that returns all students sorted by average score
"""


import pymongo


def top_students(mongo_collection):
    """returns all students sorted by average score"""
    pipeline = [
        {
            "$unwind": "$scores"
        },
        {
            "$group": {
                "_id": "$_id",
                "name": {"$first": "$name"},
                "averageScore": {"$avg": "$scores.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]

    return list(mongo_collection.aggregate(pipeline))
