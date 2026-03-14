"""
Merge Sort Algorithm Implementation
"""

import time
from typing import List, Tuple
from base_sort import SortAlgorithm


class MergeSort(SortAlgorithm):
    """Merge Sort implementation"""
    
    def sort(self, numbers: List[float]) -> Tuple[List[float], float]:
        """
        Implements Merge Sort algorithm
        Time Complexity: O(n log n) best, average, and worst case
        Space Complexity: O(n)
        
        Args:
            numbers: List of numbers to sort
            
        Returns:
            Tuple of (sorted_numbers, execution_time_ms)
        """
        start_time = time.time()
        
        arr = numbers.copy()
        
        if len(arr) > 1:
            self._merge_sort_helper(arr, 0, len(arr) - 1)
        
        end_time = time.time()
        execution_time_ms = (end_time - start_time) * 1000
        
        return arr, execution_time_ms
    
    def _merge_sort_helper(self, arr: List[float], left: int, right: int) -> None:
        """
        Helper method to recursively sort array using merge sort
        
        Args:
            arr: Array to sort
            left: Left index
            right: Right index
        """
        if left < right:
            mid = (left + right) // 2
            
            # Recursively sort left half
            self._merge_sort_helper(arr, left, mid)
            
            # Recursively sort right half
            self._merge_sort_helper(arr, mid + 1, right)
            
            # Merge the sorted halves
            self._merge(arr, left, mid, right)
    
    def _merge(self, arr: List[float], left: int, mid: int, right: int) -> None:
        """
        Merge two sorted subarrays
        
        Args:
            arr: Array containing subarrays
            left: Left index
            mid: Middle index
            right: Right index
        """
        # Create copies of the left and right subarrays
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        # Merge the two subarrays back
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        # Copy remaining elements from left subarray
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        # Copy remaining elements from right subarray
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    
    def get_name(self) -> str:
        """Get algorithm name"""
        return "Merge Sort"
    
    def get_complexity(self) -> dict:
        """Get complexity information"""
        return {
            "time_best": "O(n log n)",
            "time_average": "O(n log n)",
            "time_worst": "O(n log n)",
            "space": "O(n)",
            "stable": True
        }
