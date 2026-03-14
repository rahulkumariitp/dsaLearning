"""
Quick Sort Algorithm Implementation
"""

import time
from typing import List, Tuple
from base_sort import SortAlgorithm


class QuickSort(SortAlgorithm):
    """Quick Sort implementation"""

    def sort(self, numbers: List[float]) -> Tuple[List[float], float]:
        """
        Implements Quick Sort algorithm
        Average Time Complexity: O(n log n), Worst: O(n^2)
        Space Complexity: O(log n) on average

        Args:
            numbers: List of numbers to sort

        Returns:
            Tuple of (sorted_numbers, execution_time_ms)
        """
        start_time = time.time()

        arr = numbers.copy()
        self._quick_sort_helper(arr, 0, len(arr) - 1)

        end_time = time.time()
        execution_time_ms = (end_time - start_time) * 1000

        return arr, execution_time_ms

    def _quick_sort_helper(self, arr: List[float], low: int, high: int) -> None:
        if low < high:
            p = self._partition(arr, low, high)
            self._quick_sort_helper(arr, low, p - 1)
            self._quick_sort_helper(arr, p + 1, high)

    def _partition(self, arr: List[float], low: int, high: int) -> int:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def get_name(self) -> str:
        return "Quick Sort"

    def get_complexity(self) -> dict:
        return {
            "time_best": "O(n log n)",
            "time_average": "O(n log n)",
            "time_worst": "O(n^2)",
            "space": "O(log n)",
            "stable": False
        }
