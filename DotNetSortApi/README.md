# DotNetSortApi - Sorting Algorithms Web API

An ASP.NET Core Web API for sorting algorithms with performance metrics and CORS support.

## Features

- **Insertion Sort** endpoint at `/api/sort/insertion`
- **CORS enabled** for cross-origin requests from the React frontend
- **Dependency Injection** using ASP.NET Core DI container
- **Performance metrics** - returns execution time in milliseconds
- **Input validation** - ensures proper data format
- **Health check** endpoint at `/api/sort/health`
- **Logging** for debugging and monitoring

## Project Structure

```
DotNetSortApi/
├── Controllers/
│   └── SortController.cs       # API endpoints for sorting operations
├── Models/
│   └── SortModels.cs           # Request and Response DTOs
├── Services/
│   └── SortService.cs          # Sorting algorithm implementations
├── Program.cs                  # Application configuration and startup
├── DotNetSortApi.csproj        # Project file
└── README.md                   # This file
```

## Installation

### Prerequisites

- .NET 9.0 or higher
- Visual Studio, Visual Studio Code, or any .NET CLI

### Setup

The project is already created. To install dependencies:

```bash
dotnet restore
```

## Running the API

Start the API server:

```bash
dotnet run
```

By default, the API will be available at:
- HTTP: `http://localhost:5000`
- HTTPS: `https://localhost:5001`

## API Endpoints

### POST /api/sort/insertion

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
  "sortedNumbers": [1, 2, 5, 8, 9],
  "timeTakenMs": 0.1234,
  "success": true
}
```

**Error Response:**
```json
{
  "sortedNumbers": [],
  "timeTakenMs": 0,
  "success": false,
  "message": "Invalid request. Numbers array is required and must not be empty."
}
```

### GET /api/sort/health

Health check endpoint.

**Response:**
```json
{
  "status": "healthy"
}
```

## Algorithm Details

**Insertion Sort:**
- Time Complexity: O(n²) average and worst case, O(n) best case
- Space Complexity: O(1)
- Stable: Yes
- Use Case: Good for small datasets and nearly sorted data

## CORS Configuration

The API is configured to accept requests from any origin. This is set in `Program.cs`:

```csharp
options.AddPolicy("AllowReactApp", builder =>
{
    builder.AllowAnyOrigin()
           .AllowAnyMethod()
           .AllowAnyHeader();
});
```

For production, you should restrict the origins to your React frontend URL.

## Building for Production

```bash
dotnet build -c Release
dotnet publish -c Release
```

## Project Dependencies

- ASP.NET Core (included in template)
- No external NuGet packages required beyond framework defaults
