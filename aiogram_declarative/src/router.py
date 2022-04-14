# coding=utf-8
from typing import List, Iterable

from aiogram import Router as _Router

from aiogram_declarative.src import TelegramEventObserver


class Router(_Router):
    """Custom implementation of aiogram Router"""

    def __init__(self, *args, **kwargs) -> None:
        if hasattr(self, "name") and not kwargs.get("name", None):
            kwargs["name"] = self.name
        super().__init__(*args, **kwargs)
        self._remap_method()

    def _remap_method(self) -> None:
        for alias in self._get_observers_aliases():
            observer = TelegramEventObserver(alias, self)
            setattr(self, alias, observer)
            self.observers[alias] = observer

    @staticmethod
    def _get_observers_aliases() -> List[str]:
        return [
            "message",
            "edited_message",
            "channel_post",
            "edited_channel_post",
            "inline_query",
            "chosen_inline_result",
            "callback_query",
            "shipping_query",
            "pre_checkout_query",
            "poll",
            "poll_answer",
            "my_chat_member",
            "chat_member",
            "chat_join_request",
            "error",
        ]

    def _iter_observers(self) -> Iterable[TelegramEventObserver]:
        for alias in self._get_observers_aliases():
            yield getattr(self, alias)

    def init_callbacks(self, ex_cls, cls) -> None:
        """
        Replace handlers with initiated versions
        """
        for observer in self._iter_observers():
            for func, cb_data in observer.pre_handlers.items():
                for name, attribute in cls.__dict__.items():
                    if func is attribute:
                        cb_data.update_callback(getattr(ex_cls, name))
                        break

    def register_handlers(self) -> None:
        for observer in self._iter_observers():
            observer.register_handlers()
