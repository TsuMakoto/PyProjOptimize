from dataclasses import dataclass

from ..problem import Problem


@dataclass
class Objective:
    problem: Problem
