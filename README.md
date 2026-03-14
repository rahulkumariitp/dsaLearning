# Dot_Net_Project - Comprehensive Full-Stack Sorting Application

A complete multi-component project demonstrating modern web development with React, Python Flask API, and .NET Web API.

## Project Components

### 1. **WebApp** - React TypeScript Frontend
A modular, reusable React application for sorting arrays with multiple backend options.

**Features:**
- Dropdown selection for backend (Python or .NET)
- Algorithm selection (Insertion Sort)
- Number input interface
- Real-time performance metrics display
- Statistics (array size, min/max values)

**Run Instructions:**
```bash
cd WebApp
npm install
npm run dev
```
Access at `http://localhost:5173`

### 2. **PythonSortApi** - Flask REST API
A Python Flask API providing sorting algorithms with CORS support.

**Features:**
- POST `/sort/insertion` - Insertion Sort endpoint
- GET `/health` - Health check
- CORS enabled for React frontend

**Run Instructions:**
```bash
cd PythonSortApi
pip install -r requirements.txt
python app.py
```
Access at `http://localhost:5000`

### 3. **DotNetSortApi** - ASP.NET Core Web API
A modern .NET Web API for sorting operations with dependency injection.

**Features:**
- POST `/api/sort/insertion` - Insertion Sort endpoint
- GET `/api/sort/health` - Health check
- CORS enabled for React frontend
- Full dependency injection and logging

**Run Instructions:**
```bash
cd DotNetSortApi
dotnet build
dotnet run
```
Access at `http://localhost:5001` (HTTPS) or `http://localhost:5000` (HTTP)

### 4. **ConsoleApp1** - Modern .NET Console Application
Example console app demonstrating modern .NET features (top-level statements, DI, configuration).

**Run Instructions:**
```bash
dotnet run --project ConsoleApp1
```

### 5. **PythonConsoleApp** - Python Console Examples

**Example 1 - Basic User Info:**
```bash
/Users/rahulkumar/Dot_Net_Project/.venv/bin/python PythonConsoleApp/main.py
```

**Example 2 - Insertion Sort Console:**
```bash
/Users/rahulkumar/Dot_Net_Project/.venv/bin/python PythonConsoleApp/insertion_sort.py
```

## Full-Stack Usage Example

### Step 1: Start the Python API
```bash
cd PythonSortApi
pip install -r requirements.txt
python app.py
```

### Step 2: Start the .NET API
```bash
cd DotNetSortApi
dotnet run
```

### Step 3: Start the React Frontend
```bash
cd WebApp
npm install
npm run dev
```

### Step 4: Use the Application
1. Open `http://localhost:5173` in your browser
2. Select either Python or .NET backend from dropdown
3. Enter numbers separated by spaces (e.g., `5 2 8 1 9`)
4. Click "Sort" button
5. View sorted results and execution time

---

## Starting & Stopping Apps Individually

### Start Individual Apps

**Python Flask API** (Port 5002):
```bash
cd /Users/rahulkumar/Dot_Net_Project/PythonSortApi
/Users/rahulkumar/Dot_Net_Project/.venv/bin/python app.py
```

**.NET Web API** (Port 5001):
```bash
cd /Users/rahulkumar/Dot_Net_Project/DotNetSortApi
dotnet run
```

**React Frontend** (Port 5173):
```bash
cd /Users/rahulkumar/Dot_Net_Project/WebApp
npm run dev
```

### Stop Individual Apps

**Stop Python API** (Port 5002):
```bash
lsof -ti:5002 | xargs kill -9
```

**Stop .NET API** (Port 5001):
```bash
lsof -ti:5001 | xargs kill -9
```

**Stop React Frontend** (Port 5173):
```bash
lsof -ti:5173 | xargs kill -9
```

**Stop All Apps**:
```bash
lsof -ti:5173 | xargs kill -9 2>/dev/null; lsof -ti:5001 | xargs kill -9 2>/dev/null; lsof -ti:5002 | xargs kill -9 2>/dev/null; echo "All services stopped"
```

### Quick Aliases (Optional)

Add these to your `.zshrc` or `.bash_profile` for faster access:

```bash
alias start-python-api="cd /Users/rahulkumar/Dot_Net_Project/PythonSortApi && /Users/rahulkumar/Dot_Net_Project/.venv/bin/python app.py"
alias start-dotnet-api="cd /Users/rahulkumar/Dot_Net_Project/DotNetSortApi && dotnet run"
alias start-react="cd /Users/rahulkumar/Dot_Net_Project/WebApp && npm run dev"
alias stop-python="lsof -ti:5002 | xargs kill -9 2>/dev/null && echo 'Python API stopped'"
alias stop-dotnet="lsof -ti:5001 | xargs kill -9 2>/dev/null && echo '.NET API stopped'"
alias stop-react="lsof -ti:5173 | xargs kill -9 2>/dev/null && echo 'React stopped'"
alias stop-all="lsof -ti:5173 | xargs kill -9 2>/dev/null; lsof -ti:5001 | xargs kill -9 2>/dev/null; lsof -ti:5002 | xargs kill -9 2>/dev/null; echo 'All services stopped'"
```

Then use:
```bash
start-python-api    # Start Python API
start-dotnet-api    # Start .NET API
start-react         # Start React
stop-python         # Stop Python API
stop-dotnet         # Stop .NET API
stop-react          # Stop React
stop-all            # Stop all services
```

### Quick Reference Table

| Service | Port | Start Command | Stop Command |
|---------|------|---------------|--------------|
| Python API | 5002 | `start-python-api` | `stop-python` |
| .NET API | 5001 | `start-dotnet-api` | `stop-dotnet` |
| React Frontend | 5173 | `start-react` | `stop-react` |
| All Services | 5001,5002,5173 | - | `stop-all` |

---

```
┌─────────────────────────────────────────────────────────────┐
│                   React Frontend (WebApp)                    │
│                     Port: 5173                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ SortForm Component │ SortResult Component           │    │
│  │ - Backend Selection │ - Sorted Array Display        │    │
│  │ - Algorithm Choice  │ - Execution Time              │    │
│  │ - Number Input      │ - Statistics                  │    │
│  └─────────────────────────────────────────────────────┘    │
└────────────┬──────────────────────────┬─────────────────────┘
             │                          │
             ▼                          ▼
    ┌────────────────────┐     ┌──────────────────────┐
    │ Python Flask API   │     │  .NET Web API        │
    │ Port: 5000         │     │  Port: 5001          │
    │ ─────────────────  │     │  ──────────────────  │
    │ /sort/insertion    │     │ /api/sort/insertion  │
    │ /health            │     │ /api/sort/health     │
    └────────────────────┘     └──────────────────────┘
```

## Modular Design Principles

### React Components
- **App.tsx** - Main orchestrator, handles API calls
- **SortForm.tsx** - Reusable form component for input
- **SortResult.tsx** - Reusable result display component
- **types.ts** - Centralized TypeScript interfaces

### .NET Backend
- **Controllers/** - HTTP request handlers
- **Services/** - Business logic and algorithms
- **Models/** - Request/Response DTOs

### Python Backend
- **app.py** - Flask application with endpoints
- **requirements.txt** - Dependency management

## Type Safety

### React
- TypeScript with strict mode
- Interfaces: `SortRequest`, `SortResponse`, `BackendConfig`

### .NET
- C# with nullable reference types
- Models: `SortRequest`, `SortResponse`

### Python
- Type hints for function parameters
- Docstrings for API endpoints

## Performance Metrics

Both APIs return execution time in milliseconds:
- Python: `time_taken_ms`
- .NET: `timeTakenMs`

This allows comparison between different backends for the same sorting operation.

## Extensibility

The modular architecture allows easy addition of:
- New sorting algorithms (Bubble Sort, Quick Sort, Merge Sort, etc.)
- New backends (Node.js Express, Java Spring Boot, etc.)
- Advanced statistics (comparisons, swaps, stability analysis)
- Benchmarking features

## Technology Stack

**Frontend:**
- React 18
- TypeScript
- Vite
- CSS 3

**Backend (Python):**
- Flask 3.0
- Flask-CORS
- Python 3.9+

**Backend (.NET):**
- ASP.NET Core 9.0
- C# 12.0

## Console Applications (Learning Examples)

These demonstrate modern language features:

### ConsoleApp1 (.NET)
- Top-level statements
- Dependency Injection
- Configuration management
- User input handling

### PythonConsoleApp
- Basic input/output
- Sorting algorithms
- Interactive loops

## Getting Started

1. **Clone/Download the project**
   ```bash
   cd /Users/rahulkumar/Dot_Net_Project
   ```

2. **Start all services (in separate terminals):**
   ```bash
   # Terminal 1: Python API
   cd PythonSortApi && python app.py
   
   # Terminal 2: .NET API
   cd DotNetSortApi && dotnet run
   
   # Terminal 3: React Frontend
   cd WebApp && npm run dev
   ```

3. **Open browser to `http://localhost:5173`**

## Documentation

- [WebApp README](./WebApp/README.md) - React frontend details
- [PythonSortApi README](./PythonSortApi/README.md) - Python API details
- [DotNetSortApi README](./DotNetSortApi/README.md) - .NET API details

## Summary

This project demonstrates:
- ✅ Modular component design (maximum reusability)
- ✅ Full-stack development (Frontend + 2 Backends)
- ✅ API integration patterns
- ✅ Cross-origin resource sharing (CORS)
- ✅ Performance measurement
- ✅ Modern language features (TypeScript, C#, Python type hints)
- ✅ Best practices in architecture and design patterns