"""
Base class for sorting algorithms
Defines the interface that all sorting algorithms must implement
"""

from abc import ABC, abstractmethod
from typing import List, Tuple


class SortAlgorithm(ABC):
    """Abstract base class for sorting algorithms"""
    
    @abstractmethod
    def sort(self, numbers: List[float]) -> Tuple[List[float], float]:
        """
        Sort numbers and return sorted array with execution time
        
        Args:
            numbers: List of numbers to sort
            
        Returns:
            Tuple of (sorted_numbers, execution_time_ms)
        """
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        """Get the name of the sorting algorithm"""
        pass
    
    @abstractmethod
    def get_complexity(self) -> dict:
        """Get time and space complexity information"""
        pass
