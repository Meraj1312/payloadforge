"""
Module Registry
Responsible for loading and instantiating modules dynamically.
"""

from __future__ import annotations
import importlib
from typing import Type

from .base import BaseModule


class ModuleRegistry:
    """
    Handles dynamic module loading.
    """

    MODULE_PATH = "payloadforge.modules"

    @classmethod
    def load(cls, module_name: str) -> Type[BaseModule]:
        """
        Load a module class dynamically.

        Args:
            module_name (str): Name of module folder (e.g., 'sqli', 'cmdi', 'xss')

        Returns:
            BaseModule subclass
        """
        try:
            module_path = f"{cls.MODULE_PATH}.{module_name}.{module_name}_module"
            module = importlib.import_module(module_path)

            class_name = f"{module_name.capitalize()}Module"

            module_class = getattr(module, class_name)

            if not issubclass(module_class, BaseModule):
                raise TypeError(f"{class_name} must inherit from BaseModule")

            return module_class

        except ModuleNotFoundError:
            raise ValueError(f"Module '{module_name}' not found.")
        except AttributeError:
            raise ValueError(f"Module class '{class_name}' not found in {module_name}_module.py.")
