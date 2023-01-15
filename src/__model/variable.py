from dataclasses import dataclass

from ..problem import Problem


@dataclass
class Variable:
    problem: Problem
