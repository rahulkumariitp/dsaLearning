"""
Insertion Sort Algorithm Implementation
"""

import time
from typing import List, Tuple
from base_sort import SortAlgorithm


class InsertionSort(SortAlgorithm):
    """Insertion Sort implementation"""
    
    def sort(self, numbers: List[float]) -> Tuple[List[float], float]:
        """
        Implements Insertion Sort algorithm
        Time Complexity: O(n²) average and worst case, O(n) best case
        Space Complexity: O(1)
        
        Args:
            numbers: List of numbers to sort
            
        Returns:
            Tuple of (sorted_numbers, execution_time_ms)
        """
        start_time = time.time()
        
        arr = numbers.copy()
        n = len(arr)
        
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        
        end_time = time.time()
        execution_time_ms = (end_time - start_time) * 1000
        
        return arr, execution_time_ms
    
    def get_name(self) -> str:
        """Get algorithm name"""
        return "Insertion Sort"
    
    def get_complexity(self) -> dict:
        """Get complexity information"""
        return {
            "time_best": "O(n)",
            "time_average": "O(n²)",
            "time_worst": "O(n²)",
            "space": "O(1)",
            "stable": True
        }
