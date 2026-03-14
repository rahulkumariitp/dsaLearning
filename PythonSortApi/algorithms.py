"""
Sorting algorithms module
Factory for creating and managing sorting algorithm instances
"""

from typing import List
from base_sort import SortAlgorithm
from insertion_sort import InsertionSort
from merge_sort import MergeSort
from quick_sort import QuickSort


class SortFactory:
    """Factory for creating sorting algorithm instances"""
    
    _algorithms = {
        "insertion": InsertionSort,
        "merge": MergeSort,
        "quick": QuickSort
    }
    
    @classmethod
    def create(cls, algorithm_name: str) -> SortAlgorithm:
        """
        Create a sorting algorithm instance
        
        Args:
            algorithm_name: Name of the algorithm
            
        Returns:
            Instance of the requested algorithm
            
        Raises:
            ValueError: If algorithm is not supported
        """
        algorithm_class = cls._algorithms.get(algorithm_name.lower())
        if not algorithm_class:
            raise ValueError(
                f"Algorithm '{algorithm_name}' not supported. "
                f"Available: {list(cls._algorithms.keys())}"
            )
        return algorithm_class()
    
    @classmethod
    def get_available_algorithms(cls) -> List[str]:
        """Get list of available algorithms"""
        return list(cls._algorithms.keys())
    
    @classmethod
    def register(cls, name: str, algorithm_class: type) -> None:
        """
        Register a new sorting algorithm
        
        Args:
            name: Algorithm name
            algorithm_class: Algorithm class
        """
        cls._algorithms[name.lower()] = algorithm_class
