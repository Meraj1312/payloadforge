from abc import ABC, abstractmethod
from typing import List


class BaseModule(ABC):
    """
    Base class for all vulnerability modules.
    Each module must implement the generate() method.
    """

    name: str = "base"

    @abstractmethod
    def generate(self, **kwargs) -> List[str]:
        """
        Generate and return a list of payload strings.
        """
        pass
