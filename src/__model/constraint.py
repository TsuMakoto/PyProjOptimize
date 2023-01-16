from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

from ..problem import Problem
from .variable import Variable


@dataclass
class Constraint(metaclass=ABCMeta):
    problem: Problem
    is_valid: bool = True
    msg: str = ""

    @abstractmethod
    def append_all(self):
        pass

    @abstractmethod
    def validate(self):
        pass

    def set_variable(self, variable: Variable):
        self.variable = variable
