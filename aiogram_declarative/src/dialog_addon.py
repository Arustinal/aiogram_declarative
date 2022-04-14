# coding=utf-8
from typing import Any, Type

from aiogram import Router
from aiogram_dialog import Dialog, DialogRegistry  # type: ignore

from aiogram_declarative.abc import AbstractAddon


class DialogAddon(AbstractAddon):
    """Aiogram Dialog's support"""

    def __init__(self, dialog_registry: DialogRegistry) -> None:
        self.registry = dialog_registry

    @property
    def instance_type(self) -> Type[Dialog]:
        """This property should return a type of class, which instance should be executed with that addon."""
        return Dialog

    def register(self, router: Router, var_name: str, var_content: Any) -> None:
        """This method calls by Registry in a moment of construction whole bot structure."""
        self.registry.register(var_content, router=router)
