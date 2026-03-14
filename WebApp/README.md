# WebApp - Sort Algorithms React Application

A modular React TypeScript application that allows users to sort arrays using different backends (Python Flask API or .NET Web API).

## Project Structure

```
WebApp/
├── src/
│   ├── components/
│   │   ├── SortForm.tsx       # Form for selecting backend, algorithm, and input
│   │   ├── SortForm.css       # Styling for SortForm component
│   │   ├── SortResult.tsx     # Component to display sorting results
│   │   └── SortResult.css     # Styling for SortResult component
│   ├── App.tsx                # Main application component
│   ├── App.css                # Styling for App component
│   ├── types.ts               # TypeScript interfaces and types
│   ├── main.tsx               # Application entry point
│   └── index.css              # Global styles
├── index.html                 # HTML entry point
├── package.json               # Project dependencies and scripts
├── tsconfig.json              # TypeScript configuration
├── tsconfig.node.json         # TypeScript configuration for Node.js
├── vite.config.ts             # Vite configuration
└── README.md                  # This file
```

## Features

- **Modular Component Design:**
  - `App.tsx` - Orchestrates the application flow and API calls
  - `SortForm.tsx` - Handles user input (backend selection, algorithm, numbers)
  - `SortResult.tsx` - Displays results with statistics

- **Backend Selection:** Users can choose between Python (Flask) or .NET (Web API) backends

- **Algorithm Selection:** Currently supports Insertion Sort (extensible for more algorithms)

- **Performance Metrics:** Displays execution time in milliseconds

- **Statistics:** Shows array size, min, and max values of sorted array

## Installation

1. Navigate to the WebApp directory:
   ```bash
   cd WebApp
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

## Running the Application

1. Start the development server:
   ```bash
   npm run dev
   ```
   The application will open in your default browser at `http://localhost:5173`

2. Ensure the backend APIs are running:
   - **Python API:** Running on `http://localhost:5000`
   - **.NET API:** Running on `http://localhost:5001`

## Building for Production

```bash
npm run build
npm run preview
```

## Technology Stack

- **React 18** - UI framework
- **TypeScript** - Type safety
- **Vite** - Build tool and dev server
- **Axios** - HTTP client (can be used for API calls if needed)
- **CSS 3** - Styling

## Type Safety

The application uses TypeScript with strict mode enabled for maximum type safety:
- `SortRequest` - Request payload structure
- `SortResponse` - API response structure
- `BackendConfig` - Backend configuration

## Extensibility

The modular design makes it easy to:
- Add new sorting algorithms
- Add new backends
- Extend the result display with additional metrics
- Create custom hooks for API calls
