"""
Base Module Definition
Defines the required interface for all PayloadForge modules.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict, Any


class BaseModule(ABC):
    """
    All vulnerability modules must inherit from this class.
    """

    def __init__(self, **kwargs):
        """
        Store any configuration parameters passed from CLI.
        """
        self.config = kwargs

    @abstractmethod
    def generate(self) -> List[Dict[str, Any]]:
        """
        Generate payload data.

        Returns:
            List[Dict]: Structured payload objects.
        """
        pass
