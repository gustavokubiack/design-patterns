from abc import ABC, abstractmethod


class SortStrategy(ABC):
    @abstractmethod
    def sort(self):
        pass


class BubbleSort(SortStrategy):
    def sort(self):
        ...
