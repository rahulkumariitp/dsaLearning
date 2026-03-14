# Python Sorting API

A Flask-based REST API for sorting algorithms with performance metrics, following SOLID principles.

## Architecture & Project Structure

The API follows SOLID principles with clear separation of concerns:

```
PythonSortApi/
├── config.py          # Configuration management
├── algorithms.py      # Sorting algorithm implementations (Strategy pattern)
├── services.py        # Business logic layer (Service pattern)
├── routes.py          # API endpoints (Blueprint pattern)
├── app_factory.py     # Application factory (Factory pattern)
├── app.py             # Entry point (minimal)
├── requirements.txt   # Dependencies
└── README.md          # This file
```

## SOLID Principles Implementation

### Single Responsibility Principle (SRP)
- **config.py**: Only handles configuration
- **algorithms.py**: Only implements sorting algorithms
- **services.py**: Only handles business logic
- **routes.py**: Only defines API endpoints
- **app_factory.py**: Only creates and configures the app

### Open/Closed Principle (OCP)
- `SortAlgorithm` abstract base class allows new algorithms without modifying existing code
- `SortFactory` enables adding new algorithms via registration

### Liskov Substitution Principle (LSP)
- All sorting algorithms implement `SortAlgorithm` interface
- Can be used interchangeably through factory

### Interface Segregation Principle (ISP)
- Each module has focused, minimal interfaces
- Services only expose needed methods

### Dependency Inversion Principle (DIP)
- Routes depend on abstract `SortService`, not concrete implementations
- Algorithms depend on abstract `SortAlgorithm` base class

## Features

- **Insertion Sort** endpoint at `/sort/insertion`
- **Algorithm Info** endpoints
- **CORS enabled** for cross-origin requests
- **Performance metrics** - returns execution time in milliseconds
- **Input validation** - ensures proper data format
- **Extensible design** - easy to add new algorithms
- **Health check** endpoint at `/sort/health`

## Installation

1. Navigate to the PythonSortApi directory:
   ```bash
   cd PythonSortApi
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the API

Start the Flask development server:
```bash
python app.py
```

The API will be available at `http://localhost:5002`

## API Endpoints

### POST /sort/insertion

Sorts an array of numbers using the Insertion Sort algorithm.

**Request:**
```json
{
  "numbers": [5, 2, 8, 1, 9]
}
```

**Response:**
```json
{
  "sorted_numbers": [1, 2, 5, 8, 9],
  "time_taken_ms": 0.1234,
  "algorithm": "Insertion Sort",
  "success": true
}
```

### GET /sort/algorithms

Get list of available sorting algorithms with complexity information.

**Response:**
```json
{
  "algorithms": [
    {
      "name": "Insertion Sort",
      "complexity": {
        "time_best": "O(n)",
        "time_average": "O(n²)",
        "time_worst": "O(n²)",
        "space": "O(1)",
        "stable": true
      },
      "available": true
    }
  ]
}
```

### GET /sort/algorithm/<algorithm_name>

Get information about a specific algorithm.

**Response:**
```json
{
  "name": "Insertion Sort",
  "complexity": {
    "time_best": "O(n)",
    "time_average": "O(n²)",
    "time_worst": "O(n²)",
    "space": "O(1)",
    "stable": true
  },
  "available": true
}
```

### GET /sort/health

Health check endpoint.

**Response:**
```json
{
  "status": "healthy"
}
```

## Configuration

Configuration is managed through environment variables in `config.py`:

```python
FLASK_ENV     # Development or production
DEBUG         # Debug mode (True/False)
HOST          # Server host (default: 0.0.0.0)
PORT          # Server port (default: 5002)
CORS_ORIGINS  # CORS origins (default: *)
```

Set environment variables:
```bash
export PORT=5000
export DEBUG=False
export FLASK_ENV=production
python app.py
```

## Adding New Sorting Algorithms

1. Create a new class inheriting from `SortAlgorithm` in `algorithms.py`:

```python
class QuickSort(SortAlgorithm):
    def sort(self, numbers: List[float]) -> Tuple[List[float], float]:
        # Implementation
        pass
    
    def get_name(self) -> str:
        return "Quick Sort"
    
    def get_complexity(self) -> dict:
        return {
            "time_best": "O(n log n)",
            "time_average": "O(n log n)",
            "time_worst": "O(n²)",
            "space": "O(log n)",
            "stable": False
        }
```

2. Register it in `SortFactory`:

```python
from algorithms import SortFactory, QuickSort

SortFactory.register("quicksort", QuickSort)
```

3. Create endpoint in `routes.py`:

```python
@sort_bp.route("/quicksort", methods=["POST"])
def sort_quicksort():
    # Similar to sort_insertion
    pass
```

## Testing

Run tests to verify the API:

```bash
# Health check
curl http://localhost:5002/sort/health

# Sort numbers
curl -X POST http://localhost:5002/sort/insertion \
  -H "Content-Type: application/json" \
  -d '{"numbers": [5, 2, 8, 1, 9]}'

# Get algorithms
curl http://localhost:5002/sort/algorithms
```

## Design Patterns Used

1. **Factory Pattern**: `SortFactory` for creating algorithm instances
2. **Strategy Pattern**: `SortAlgorithm` interface for pluggable algorithms
3. **Service Pattern**: `SortService` for business logic
4. **Blueprint Pattern**: Flask blueprints for modular routing
5. **Configuration Pattern**: Centralized config management
6. **DTO Pattern**: Request/Response classes for data transfer

## Error Handling

The API provides meaningful error responses:

```json
{
  "success": false,
  "message": "Error description"
}
```

Status codes:
- `200`: Successful sort operation
- `400`: Invalid request (bad data)
- `404`: Algorithm not found
- `500`: Server error

