from abc import ABC, abstractmethod
from typing import List
import random


class SortStrategy(ABC):
    @abstractmethod
    def sort(self, _list: List[int]):
        pass


class BubbleSort(SortStrategy):
    def sort(self, _list: List[int]):
        n = len(_list)
        for i in range(n):
            for j in range(0, n - i - 1):
                if _list[j] > _list[j + 1]:
                    _list[j], _list[j + 1] = _list[j + 1], _list[j]
        return _list


class InsertionSort(SortStrategy):
    def sort(self, _list: List[int]):
        for i in range(0, len(_list)):
            pivot = _list[i]
            j = i - 1
            while j >= 0 and pivot < _list[j]:
                _list[j + 1] = _list[j]
                j -= 1
            _list[j + 1] = pivot
        return _list


class MergeSort(SortStrategy):
    def sort(self, _list: List[int]):
        if len(_list) <= 1:
            return _list
        mid = len(_list) // 2
        left = _list[:mid]
        right = _list[mid:]
        left = self.sort(left)
        right = self.sort(right)
        return self.merge(left, right)

    def merge(self, left: list, rigth: list):
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(rigth):
            if left[i] < rigth[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(rigth[j])
                j += 1
        result.extend(left[i:])
        result.extend(rigth[j:])
        return result


class QuickSort(SortStrategy):
    def sort(self, _list: List[int]):
        if len(_list) <= 1:
            return _list
        pivot = _list[-1]
        lower = [x for x in _list[:-1] if x <= pivot]
        higher = [x for x in _list[:-1] if x > pivot]
        return self.sort(lower) + [pivot] + self.sort(higher)


class SortContext:
    def __init__(self, sort_strategy: SortStrategy = None) -> None:
        self._sort_strategy = sort_strategy

    @property
    def strategy(self):
        return self._sort_strategy

    @strategy.setter
    def strategy(self, sort_strategy: SortStrategy):
        self._sort_strategy = sort_strategy

    def handle_sort(self, _list: List[int]) -> List[int]:
        return self._sort_strategy.sort(_list)


context = SortContext(QuickSort())
context.strategy = BubbleSort()
_list = [random.randint(0, 100) for _ in range(15)]
print(f"Sort: {_list}")
sorted_list = context.handle_sort(_list)
print(f"Result: {sorted_list}")
