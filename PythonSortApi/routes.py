"""
API routes module
Defines all API endpoints
Follows Single Responsibility principle
"""

from flask import Blueprint, request, jsonify
from services import SortService, SortRequest

# Create blueprint for sort routes
sort_bp = Blueprint("sort", __name__, url_prefix="/sort")

# Initialize service
sort_service = SortService()


@sort_bp.route("/insertion", methods=["POST"])
def sort_insertion():
    """
    POST /sort/insertion
    Sorts numbers using Insertion Sort algorithm
    
    Request body:
    {
        "numbers": [float, float, ...]
    }
    
    Response:
    {
        "sorted_numbers": [float, float, ...],
        "time_taken_ms": float,
        "algorithm": str,
        "success": bool,
        "message": str (optional)
    }
    """
    try:
        # Parse request
        data = request.get_json()
        
        if not data:
            return jsonify({
                "success": False,
                "message": "Request body must be JSON"
            }), 400
        
        # Create request object
        sort_request = SortRequest(
            numbers=data.get("numbers", []),
            algorithm="insertion"
        )
        
        # Execute sort
        response = sort_service.sort(sort_request)
        
        # Return response
        return jsonify(response.to_dict()), 200 if response.success else 400
    
    except ValueError as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 400
    
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Server error: {str(e)}"
        }), 500


@sort_bp.route("/algorithms", methods=["GET"])
def get_algorithms():
    """
    GET /sort/algorithms
    Get list of available sorting algorithms
    
    Response:
    {
        "algorithms": [
            {
                "name": str,
                "complexity": {
                    "time_best": str,
                    "time_average": str,
                    "time_worst": str,
                    "space": str,
                    "stable": bool
                }
            }
        ]
    }
    """
    algorithms = sort_service.get_available_algorithms()
    return jsonify({"algorithms": algorithms}), 200


@sort_bp.route("/algorithm/<algorithm_name>", methods=["GET"])
def get_algorithm_info(algorithm_name: str):
    """
    GET /sort/algorithm/<algorithm_name>
    Get information about a specific algorithm
    
    Response:
    {
        "name": str,
        "complexity": {...},
        "available": bool
    }
    """
    info = sort_service.get_algorithm_info(algorithm_name)
    
    if not info["available"]:
        return jsonify({
            "success": False,
            "message": f"Algorithm '{algorithm_name}' not found"
        }), 404
    
    return jsonify(info), 200


@sort_bp.route("/health", methods=["GET"])
def health():
    """
    GET /sort/health
    Health check endpoint
    
    Response:
    {
        "status": "healthy"
    }
    """
    return jsonify({"status": "healthy"}), 200
