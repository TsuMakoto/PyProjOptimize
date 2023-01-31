from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

from .base import Base
from .variable import Variable


@dataclass
class Objective(Base, metaclass=ABCMeta):
    variable: Variable
    is_valid: bool = True
    msg: str = ""

    @abstractmethod
    def configurate(self):
        pass

    def validate(self):
        pass
