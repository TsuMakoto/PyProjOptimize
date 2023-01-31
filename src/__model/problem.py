from dataclasses import dataclass
from typing import Generic, TypeVar

from lib.pipeline import Params as PipelineParams
from lib.pipeline import Pipeline


@dataclass
class Params:
    data_info: PipelineParams


P = TypeVar("P", bound=Params)
T = TypeVar("T")


class Problem(Generic[P, T]):
    def __init__(self, params: P):
        self.params = params
        self.indexes = self._indexes(params)
        self._set_params(params)

    def _indexes(self, params: P) -> T:
        return Pipeline(params.data_info).do()

    def _set_params(self, params: P):
        pass
