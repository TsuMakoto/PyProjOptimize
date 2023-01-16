from dataclasses import dataclass

from .__model.constraint import Constraint
from .__model.objective import Objective
from .__model.variable import Variable
from .problem import Problem


@dataclass
class Model:
    problem: problem
    variable: Variable
    constraint: Constraint
    objective: Objective

    def make(self):
        self.variable.generate()
        self.fix()

        self.constraint.set_variable(self.variable)
        self.constraint.validate()
        if not self.constraint.is_valid:
            raise Exception(self.constraint.msg)
        self.constraint.append_all()

        self.objective.set_variable(self.variable)
        self.objective.validate()
        if not self.objective.is_valid:
            raise Exception(self.objective.msg)
        self.objective.configurate()
