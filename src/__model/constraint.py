from dataclasses import dataclass

from ..problem import Problem


@dataclass
class Constraint:
    problem: Problem
