from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

from .model import Model


class Result(metaclass=ABCMeta):
    @abstractmethod
    def parse(self):
        pass


@dataclass
class Evaluator(metaclass=ABCMeta):
    result: Result

    @abstractmethod
    def evaluate(self):
        pass


class Solver(metaclass=ABCMeta):
    @abstractmethod
    def solve(self, model: Model) -> Result:
        pass

    @abstractmethod
    def evaluate(self, result: Result) -> Evaluator:
        pass
