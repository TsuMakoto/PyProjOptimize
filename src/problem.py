from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Problem(Generic[T], metaclass=ABCMeta):
    def __init__(self, params: T):
        self.params = params

    @abstractmethod
    def make(self):
        pass
