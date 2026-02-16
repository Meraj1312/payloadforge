from typing import Dict, Type
from core.base import BaseModule


class ModuleRegistry:
    """
    Central registry for vulnerability modules.
    """

    _modules: Dict[str, Type[BaseModule]] = {}

    @classmethod
    def register(cls, module_class: Type[BaseModule]) -> None:
        cls._modules[module_class.name] = module_class

    @classmethod
    def get(cls, name: str) -> BaseModule:
        if name not in cls._modules:
            available = ", ".join(cls._modules.keys())
            raise ValueError(f"Module '{name}' not found. Available: {available}")
        return cls._modules[name]()

    @classmethod
    def list_modules(cls):
        return list(cls._modules.keys())
