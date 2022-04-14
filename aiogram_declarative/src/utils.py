# coding=utf-8
from typing import Callable
from inspect import getfullargspec


def resolve_kwargs(func: Callable, whole_kwargs: dict) -> dict:
    if "self" in whole_kwargs.keys():
        raise ValueError("Don't use \"self\" parameter in kwargs")
    return {k: v for k, v in whole_kwargs.items() if k in getfullargspec(func)[0]}
