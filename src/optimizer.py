from dataclasses import dataclass

from lib.utils.operators.pipe import PipeOperator

from .model import Model
from .solver import Solver


@dataclass
class Optimizer:
    model: Model
    solver: Solver

    def optimize(self):
        return PipeOperator(self.model) * \
            self.solver.solve >> \
            self.solver.evaluate
