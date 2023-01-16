from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

from ..problem import Problem


@dataclass
class Variable(metaclass=ABCMeta):
    problem: Problem

    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def fix(self):
        pass
