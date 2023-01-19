from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


class Params:
    pass


@dataclass
class Problem(metaclass=ABCMeta):
    params: Params

    @abstractmethod
    def make(self):
        pass
