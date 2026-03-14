"""
Service layer for sorting operations
Handles business logic and validation
Follows Single Responsibility and Dependency Inversion principles
"""

from typing import List, Dict, Any
from algorithms import SortFactory, SortAlgorithm


class SortRequest:
    """Represents a sort request"""
    
    def __init__(self, numbers: List[float], algorithm: str = "insertion"):
        """
        Initialize a sort request
        
        Args:
            numbers: List of numbers to sort
            algorithm: Name of the sorting algorithm
            
        Raises:
            ValueError: If input is invalid
        """
        if not isinstance(numbers, list):
            raise ValueError("Numbers must be a list")
        
        if not numbers:
            raise ValueError("Numbers list cannot be empty")
        
        try:
            self.numbers = [float(n) for n in numbers]
        except (ValueError, TypeError):
            raise ValueError("All numbers must be numeric")
        
        self.algorithm = algorithm


class SortResponse:
    """Represents a sort response"""
    
    def __init__(
        self,
        sorted_numbers: List[float],
        time_taken_ms: float,
        algorithm: str,
        success: bool = True,
        message: str = None
    ):
        """
        Initialize a sort response
        
        Args:
            sorted_numbers: The sorted numbers
            time_taken_ms: Execution time in milliseconds
            algorithm: Algorithm used
            success: Whether the operation was successful
            message: Optional message
        """
        self.sorted_numbers = sorted_numbers
        self.time_taken_ms = time_taken_ms
        self.algorithm = algorithm
        self.success = success
        self.message = message
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert response to dictionary"""
        return {
            "sorted_numbers": self.sorted_numbers,
            "time_taken_ms": self.time_taken_ms,
            "algorithm": self.algorithm,
            "success": self.success,
            "message": self.message
        }


class SortService:
    """
    Service for sorting operations
    Implements business logic and algorithm selection
    """
    
    def __init__(self):
        """Initialize sort service"""
        self.factory = SortFactory()
    
    def sort(self, request: SortRequest) -> SortResponse:
        """
        Perform sorting operation
        
        Args:
            request: SortRequest object
            
        Returns:
            SortResponse object
            
        Raises:
            ValueError: If algorithm is not supported
        """
        try:
            # Get the sorting algorithm
            algorithm: SortAlgorithm = self.factory.create(request.algorithm)
            
            # Execute sorting
            sorted_numbers, execution_time = algorithm.sort(request.numbers)
            
            # Create response
            return SortResponse(
                sorted_numbers=sorted_numbers,
                time_taken_ms=execution_time,
                algorithm=algorithm.get_name(),
                success=True
            )
        
        except ValueError as e:
            return SortResponse(
                sorted_numbers=[],
                time_taken_ms=0,
                algorithm=request.algorithm,
                success=False,
                message=str(e)
            )
        except Exception as e:
            return SortResponse(
                sorted_numbers=[],
                time_taken_ms=0,
                algorithm=request.algorithm,
                success=False,
                message=f"Unexpected error: {str(e)}"
            )
    
    def get_algorithm_info(self, algorithm_name: str) -> Dict[str, Any]:
        """
        Get information about a sorting algorithm
        
        Args:
            algorithm_name: Name of the algorithm
            
        Returns:
            Dictionary with algorithm information
        """
        try:
            algorithm = self.factory.create(algorithm_name)
            return {
                "id": algorithm_name,
                "name": algorithm.get_name(),
                "complexity": algorithm.get_complexity(),
                "available": True
            }
        except ValueError:
            return {"available": False}
    
    def get_available_algorithms(self) -> List[Dict[str, Any]]:
        """
        Get list of available algorithms with their info
        
        Returns:
            List of algorithm information dictionaries
        """
        algorithms = []
        for algo_name in self.factory.get_available_algorithms():
            info = self.get_algorithm_info(algo_name)
            # ensure each entry includes the route id (e.g., 'insertion', 'merge')
            info.setdefault('id', algo_name)
            algorithms.append(info)
        return algorithms
