# coding=utf-8
from typing import Tuple, Any, Generator

from aiogram_declarative.src import Router


class CoreJoint:
    """Basic class for a group of aiogram handler classes"""

    def __init__(self, **kwargs) -> None:
        for name, attribute in kwargs.items():
            setattr(self, name, attribute)
        if not getattr(self, "router", None):
            self.router = Router()

    def iter_attributes(self) -> Generator[Tuple[str, Any], None, None]:
        for name, attribute in self.__dict__.items():
            if not name.startswith("_"):
                yield name, attribute
        yield from self._iter_cls_attributes()

    @classmethod
    def _iter_cls_attributes(cls) -> Generator[Tuple[str, Any], None, None]:
        for name, attribute in cls.__dict__.items():
            yield name, attribute
