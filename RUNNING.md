# Running the Sorting Apps (DotNet + Python + Web)

This guide shows how to run each app from this workspace and how to test endpoints.

## 1) .NET Sorting API (DotNetSortApi)

### Prerequisites
- .NET 9 SDK installed
- Optional: `dotnet` command in PATH

### Run
```cli
cd /Users/rahulkumar/Dot_Net_Project/DotNetSortApi
# if port already in use, specify a free port with --urls
dotnet run --urls http://localhost:5050
```

### Verify
```cli
curl -i -X GET http://localhost:5050/api/sort/health
```

### API endpoints
- `POST http://localhost:5050/api/sort/insertion`
- `POST http://localhost:5050/api/sort/merge`
- `POST http://localhost:5050/api/sort/quick`

Request body for sorting endpoints:
```json
{
  "numbers": [5, 3, 1, 4, 2]
}
```

## 2) Python Sorting API (PythonSortApi)

### Prerequisites
- Python 3.9+ installed
- `pip` installed

### Install dependencies
```cli
cd /Users/rahulkumar/Dot_Net_Project/PythonSortApi
python3 -m pip install -r requirements.txt
```

### Run
```cli
cd /Users/rahulkumar/Dot_Net_Project/PythonSortApi
python3 app.py
```

### Verify
```cli
curl -i -X GET http://127.0.0.1:5002/sort/health
```

### Python API endpoints
- `GET http://127.0.0.1:5002/sort/health`
- `POST http://127.0.0.1:5002/sort/insertion`
- `GET http://127.0.0.1:5002/sort/algorithms`
- `GET http://127.0.0.1:5002/sort/algorithm/<name>`

Example request body for `POST /sort/insertion`:
```json
{
  "numbers": [5, 1, 9, 3]
}
```

## 3) WebApp (React + Vite)

### Prerequisites
- Node.js + npm installed

### Install and run
```cli
cd /Users/rahulkumar/Dot_Net_Project/WebApp
npm install
npm run dev
```

### Verify
Open the printed local URL (usually `http://localhost:5173`) in browser.

## 4) Run from VS Code (recommended)
1. Open Command Palette (⌘+Shift+P) -> `Tasks: Run Task`.
2. Choose `Run .NET API`, `Run Python API`, or `Run WebApp`.
3. To run all together, choose `Run All Services`.

## 5) Run from script
Run all three services from one terminal:
```cli
cd /Users/rahulkumar/Dot_Net_Project
./run-all.sh
```

## 6) Stop services (cleanup)
In terminal, run:
```cli
pkill -f "dotnet run" || true
pkill -f "python3 app.py" || true
pkill -f "npm run dev" || true
```

Or run the helper script from workspace root:
```cli
cd /Users/rahulkumar/Dot_Net_Project
./run-all.sh stop
```

## 7) Notes
- If ports are in use, follow the command line output and run on a different port.
- For .NET, use `dotnet run --urls http://localhost:<port>`.
- For Python, set envs in `PythonSortApi/config.py` or on CLI:
  `HOST=0.0.0.0 PORT=5002 python3 app.py`
