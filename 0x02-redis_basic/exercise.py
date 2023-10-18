#!/usr/bin/env python3
"""Defines a module that creates a class cache"""


import redis
import uuid
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable[[
        bytes], Union[str, int, float]] = [
            lambda d:d]) -> Union[str, int, float, bytes]:
        """take a key string argument and an optional Callable
        that will convert the data back to the desired format"""
        data = self._redis.get(key)
        if data is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """parametrize Cache.get with string"""
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """parametrize Cache.get with int"""
        return self.get(key, fn=int)
