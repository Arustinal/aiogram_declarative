# coding=utf-8
"""This is the main registry."""
from typing import Union, Tuple, Dict, Any, Type, Generator

from aiogram import Dispatcher, Router as _Router

from aiogram_declarative.abc import AbstractAddon
from aiogram_declarative.src import CoreJoint
from aiogram_declarative.src.utils import resolve_kwargs


class Registry:
    """
    This class implements logic of finding all handler classes, and executes setup procedures on them.
    """

    def __init__(
            self,
            router: Union[Dispatcher, _Router],
            addons: Tuple[AbstractAddon, ...] = tuple(),
            core_cls=CoreJoint,
            **kwargs: Any
    ) -> None:
        self._core_cls = core_cls
        self.router = router
        self.addons = addons
        self._cls_storage: Dict[Type[Any], Any] = {}
        self.kwargs = kwargs

    def _get_ex_by_cls(self, cls) -> Any:
        self._cls_storage[cls] = self._cls_storage.get(cls) or cls()
        return self._cls_storage[cls]

    def _iter_classes(self, cls) -> Any:
        if cls is not self._core_cls:
            yield cls
        for subclass in cls.__subclasses__():
            yield from self._iter_classes(subclass)

    def _iter_instances_by_cls(self, cls) -> Any:
        if cls is not self._core_cls:
            yield self._get_ex_by_cls(cls)
        for subclass in cls.__subclasses__():
            yield from self._iter_instances_by_cls(subclass)

    def _iter_cls_with_instance(self) -> Generator[Tuple[Any, Any], None, None]:
        for cls, instance in zip(
                self._iter_classes(self._core_cls),
                self._iter_instances_by_cls(self._core_cls),
        ):
            yield cls, instance

    def _tie_routers(self) -> None:
        for cls, instance in self._iter_cls_with_instance():
            instance.router.init_callbacks(instance, cls)
            parent_class = cls.mro()[1]
            parent_instance = self._get_ex_by_cls(parent_class)
            parent_instance.router.include_router(instance.router)

    def _register_handler_functions(self) -> None:
        for instance in self._iter_instances_by_cls(self._core_cls):
            instance.router.register_handlers()

    def _tie_filters(self) -> None:
        for instance in self._iter_instances_by_cls(self._core_cls):
            instance.router.register_filters()

    def _tie_addons(self) -> None:
        addons_by_types = {addon.instance_type: addon for addon in self.addons}
        for instance in self._iter_instances_by_cls(self._core_cls):
            for name, attribute in instance.iter_attributes():
                if addon_handler := addons_by_types.get(type(attribute)):
                    addon_handler.register(
                        instance.router, var_name=name, var_content=attribute
                    )

    def _run_init_hook(self) -> None:
        for instance in self._iter_instances_by_cls(self._core_cls):
            instance.init_hook(**resolve_kwargs(instance.init_hook, self.kwargs))

    def _del_cls_storage(self) -> None:
        if hasattr(self, "_cls_storage"):
            delattr(self, "_cls_storage")

    def construct(self, del_storage=True) -> None:
        """Build up"""
        if not hasattr(self, "_cls_storage"):
            raise ValueError("Module already initiated")
        self._core_cls.router = self.router  # replace router with dispatcher in optimization purposes
        self._get_ex_by_cls(self._core_cls)
        self._run_init_hook()
        self._tie_routers()
        self._register_handler_functions()
        self._tie_addons()
        if del_storage:
            self._del_cls_storage()
