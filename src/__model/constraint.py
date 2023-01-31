from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

from .variable import Variable


@dataclass
class Constraint(metaclass=ABCMeta):
    variable: Variable
    is_valid = True
    msg = ""

    @abstractmethod
    def append_all(self):
        pass

    def validate(self):
        pass
