from abc import ABCMeta, abstractmethod

from .__model.constraint import Constraint
from .__model.objective import Objective
from .__model.variable import Variable


class Params:
    pass


@dataclass
class Problem(metaclass=ABCMeta):
    params: Params

    @abstractmethod
    def make(self):
        pass
