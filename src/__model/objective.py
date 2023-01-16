from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

from ..problem import Problem
from .variable import Variable


@dataclass
class Objective(metaclass=ABCMeta):
    problem: Problem
    is_valid: bool = True
    msg: str = ""

    @abstractmethod
    def configurate(self):
        pass

    @abstractmethod
    def validate(self):
        pass

    def set_variable(self, variable: Variable):
        self.variable = variable
