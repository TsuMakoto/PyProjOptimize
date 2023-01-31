from dataclasses import dataclass

from .base import Base


@dataclass
class Variable(Base):
    def generate(self):
        pass
