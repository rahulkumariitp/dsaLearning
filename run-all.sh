#!/usr/bin/env bash
set -e

# Starts DotNet API, Python API, and WebApp in background.
# Usage: ./run-all.sh

echo "Starting DotNet API on http://localhost:5050..."
cd "$(dirname "$0")/DotNetSortApi"
dotnet run --urls http://localhost:5050 &
DOTNET_PID=$!

echo "Starting Python API on http://127.0.0.1:5002..."
cd "$(dirname "$0")/PythonSortApi"
python3 app.py &
PY_PID=$!

echo "Starting WebApp on http://localhost:5173..."
cd "$(dirname "$0")/WebApp"
npm run dev &
WEB_PID=$!

echo "All services started."
echo "DotNet PID: $DOTNET_PID"
echo "Python PID: $PY_PID"
echo "Web PID: $WEB_PID"

echo "Run 'pkill -P $$' to stop all child processes, or use kill <pid>."
wait