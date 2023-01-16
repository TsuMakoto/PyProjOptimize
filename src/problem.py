from abc import ABCMeta, abstractmethod


class Problem(metaclass=ABCMeta):
    @abstractmethod
    def make(self):
        pass
