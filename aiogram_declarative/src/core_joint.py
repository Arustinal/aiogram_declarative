# coding=utf-8
from typing import Any
from typing import Generator
from typing import Tuple

from aiogram_declarative.src import Router


def nothing(*args, **kwargs):
    pass


class MetaJoint(type):
    def __new__(mcs, name, bases, class_dict):
        if len(bases) > 1:
            raise ValueError("Joint can't inherit from more than one class")
        if bases:
            parent = bases[-1]
            if past_router := getattr(parent, "router", None):
                if past_router is class_dict.get("router", None):
                    class_dict["router"] = Router(name=name)
            if "__init__" in class_dict:
                raise ValueError("Don't use __init__ directly. Use \"init hook()\" instead with same usage")

            class_obj = super().__new__(mcs, name, bases, class_dict)
            if past_init_hook := getattr(parent, "init_hook", None):
                if current_init_hook := getattr(class_obj, "init_hook", None):
                    if past_init_hook is current_init_hook:
                        setattr(class_obj, "init_hook", nothing)
        else:
            class_obj = super().__new__(mcs, name, bases, class_dict)
        return class_obj


class CoreJoint(metaclass=MetaJoint):
    """Basic class for a group of aiogram structure classes"""

    def __init__(self, **kwargs) -> None:
        pass

    def iter_attributes(self) -> Generator[Tuple[str, Any], None, None]:
        for name, attribute in self.__dict__.items():
            if not name.startswith("_"):
                yield name, attribute
        yield from self._iter_cls_attributes()

    @classmethod
    def _iter_cls_attributes(cls) -> Generator[Tuple[str, Any], None, None]:
        for name, attribute in cls.__dict__.items():
            yield name, attribute
