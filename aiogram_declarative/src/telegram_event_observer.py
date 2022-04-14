# coding=utf-8
"""
Custom version of TelegramEventObserver
"""
from typing import Optional, Dict, Any, Callable, List

from aiogram import Router as _Router
from aiogram.dispatcher.event.handler import CallbackType, FilterType
from aiogram.dispatcher.event.telegram import (
    TelegramEventObserver as _TelegramEventObserver,
)

from aiogram_declarative.src import CallbackData


class TelegramEventObserver(_TelegramEventObserver):
    """Custom implementation of TelegramEventObserver"""

    def __init__(self, event_type: str, router: _Router) -> None:
        super().__init__(router, event_type)
        self.event_type = event_type
        self.pre_handlers: Dict[CallbackType, CallbackData] = {}
        self.filters_storage: List[FilterType] = []
        self.bound_filters_storage: Dict[str, Any] = {}

    def __call__(
        self,
        *args: FilterType,
        flags: Optional[Dict[str, Any]] = None,
        **bound_filters: Any
    ) -> Callable[[CallbackType], CallbackType]:
        if not bound_filters:
            bound_filters = {}

        def _wrapper(callback: CallbackType) -> CallbackType:
            self.pre_handlers[callback] = CallbackData(
                callback, args=args, flags=flags, bound_filters=bound_filters
            )
            return callback

        return _wrapper

    def register_handlers(self) -> None:
        """This method simply registers initiated callback methods via standard aiogram procedure"""
        for index, cb_data in self.pre_handlers.items():
            if not cb_data.is_callback_initiated():
                raise ValueError("Callback has been not initiated")
            self.register(
                cb_data.callback,
                flags=cb_data.flags,
                *cb_data.args,
                **cb_data.bound_filters
            )
