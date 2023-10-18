#!/usr/bin/env python3
"""Defines a module that creates a class cache"""


import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """stores a private instance"""
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument and returns a string"""
        key = str(uuid.uuid4())

        self._redis.set(key, data)

        return key
