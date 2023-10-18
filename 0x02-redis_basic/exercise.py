#!/usr/bin/env python3
"""Defines a module that creates a class cache"""


import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """decorator that takes a single method Callable argument
    and returns a Callable"""
    key = method.__qualname__

    @wraps(method)
    def wrapped_method(self, *args, **kwargs):
        """wrapper method"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapped_method


def call_history(method: Callable) -> Callable:
    """Appends inputs and outputs to create input
    and output list keys, respectively."""

    @wraps(method)
    def wrapped_method(self, *args, **kwargs):
        """Wrapper method for the decorated function"""
        method_name = method.__qualname__
        input_list_key = f"{method_name}:inputs"
        output_list_key = f"{method_name}:outputs"

        self._redis.rpush(input_list_key, str(args))

        output = method(self, *args, **kwargs)
        self._redis.rpush(output_list_key, str(output))
        return output

    return wrapped_method


class Cache:
    def __init__(self):
        """stores a private instance"""
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()
        self.call_count = {}

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[
        Callable] = None) -> Union[str, int, float, bytes]:
        """take a key string argument and an optional Callable
        that will convert the data back to the desired format"""
        data_value = self._redis.get(key)
        if data_value is not None:
            return fn(data_value)
        return data_value

    def get_str(self, key: str) -> str:
        """parametrize Cache.get with string"""
        data_value = self._redis.get(key)
        return data_value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """parametrize Cache.get with int"""
        data_value = self._redis.get(key)
        try:
            data_value = int(value.decode("utf-8"))
        except Exception:
            data_value = 0
        return data_value
