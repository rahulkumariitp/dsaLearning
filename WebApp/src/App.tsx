import { useState } from 'react'
import './App.css'
import SortForm from './components/SortForm'
import SortResult from './components/SortResult'
import { SortRequest, SortResponse } from './types'

// Main App component - orchestrates the entire application flow
// Children: SortForm (input), SortResult (output)
function App() {
  const [result, setResult] = useState<SortResponse | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  // Callback function passed to SortForm to handle sort requests
  const handleSort = async (request: SortRequest) => {
    setLoading(true)
    setError(null)
    setResult(null)

    try {
      const response = await fetch(`${request.apiUrl}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ numbers: request.numbers })
      })

      if (!response.ok) {
        throw new Error(`API Error: ${response.statusText}`)
      }

      const data = await response.json()
      setResult(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An unknown error occurred')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app-container">
      <h1>Sort Algorithms Web App</h1>
      <div className="main-content">
        {/* SortForm component for user input */}
        <SortForm onSort={handleSort} loading={loading} />

        {/* Display error message if any */}
        {error && <div className="error-message">{error}</div>}

        {/* Display loading state */}
        {loading && <div className="loading-message">Processing...</div>}

        {/* SortResult component for displaying results */}
        {result && <SortResult result={result} />}
      </div>
    </div>
  )
}

export default App
