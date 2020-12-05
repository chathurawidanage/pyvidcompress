from abc import abstractmethod


from abc import ABC, abstractmethod
from __future__ import annotations


class Tdv(ABC):

    @abstractmethod
    def persist(self):
        pass

    @staticmethod
    def load(file_path) -> Tdv:
        pass
