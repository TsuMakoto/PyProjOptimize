from dataclasses import InitVar, dataclass

from .problem import Params, Problem


@dataclass
class Base:
    problem: InitVar[Problem]

    def __post_init__(self, problem: Problem):
        self._set_indexes(problem.indexes)
        self._set_params(problem.params)
        self._set_appendix(problem)

    def _set_indexes(self, indexes):
        pass

    def _set_params(self, params: Params):
        self.params = params

    def _set_appendix(self, problem):
        pass
