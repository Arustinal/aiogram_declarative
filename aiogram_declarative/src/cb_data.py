# coding=utf-8
from dataclasses import dataclass
from inspect import ismethod
from typing import Optional, Dict, Any, Tuple

from aiogram.dispatcher.event.handler import CallbackType


@dataclass
class CallbackData:
    """
    Describing class for callback
    """

    callback: CallbackType
    filters: Tuple[CallbackType, ...]
    bound_filters: Dict[str, Any]
    flags: Optional[Dict[str, Any]]
    stacklevel: int

    def is_callback_initiated(self) -> bool:
        """Is callback initiated as a method?"""
        if ismethod(self.callback):
            return True
        else:
            return False

    def update_callback(self, initiated_callback: CallbackType) -> None:
        """Replaces callback with an initiated version"""
        self.callback = initiated_callback
