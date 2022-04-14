# coding=utf-8
from abc import ABC
from typing import Any

from aiogram import Router


class AbstractAddon(ABC):
    """Example of addon class"""

    @property
    def instance_type(self) -> Any:
        """This property should contain a type of variable, which should be registered with current addon"""
        raise NotImplementedError()

    def register(self, router: Router, var_name: str, var_content: Any) -> None:
        """This method should implement all logic around your addon code, registration/preparing/etc.
        For single-actions before and past the registration, use __init__ and __del__ methods"""
        raise NotImplementedError()
