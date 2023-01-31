from dataclasses import dataclass

from .__model.constraint import Constraint
from .__model.objective import Objective
from .__model.problem import Problem
from .__model.variable import Variable


@dataclass
class Model:
    problem: Problem
    variable: Variable
    constraint: Constraint
    objective: Objective

    def make(self):
        self.constraint.validate()
        if not self.constraint.is_valid:
            raise Exception(self.constraint.msg)
        self.constraint.append_all()

        self.objective.validate()
        if not self.objective.is_valid:
            raise Exception(self.objective.msg)
        self.objective.configurate()
