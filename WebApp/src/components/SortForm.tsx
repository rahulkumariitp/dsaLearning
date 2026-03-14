import { useState } from 'react'
import { SortRequest, BackendConfig } from '../types'
import './SortForm.css'

interface SortFormProps {
  onSort: (request: SortRequest) => void
  loading: boolean
}

// Configuration for available backends (base URLs)
const BACKENDS: BackendConfig[] = [
  { name: 'Python (Flask)', value: 'python', url: 'http://localhost:5002/sort' },
  { name: '.NET (Web API)', value: 'dotnet', url: 'http://localhost:5001/api/sort' }
]

// Available algorithm keys (must match backend endpoints)
const ALGORITHMS = ['insertion', 'merge', 'quick']

// SortForm component - handles user input for sorting
// Props: onSort callback, loading state
// State: selected backend, algorithm, and input numbers
function SortForm({ onSort, loading }: SortFormProps) {
  const [selectedBackend, setSelectedBackend] = useState<'python' | 'dotnet'>('python')
  const [selectedAlgorithm, setSelectedAlgorithm] = useState('insertion')
  const [inputValue, setInputValue] = useState('')

  // Parse input string and validate numbers
  const parseNumbers = (input: string): number[] | null => {
    try {
      const numbers = input
        .trim()
        .split(/\s+/)
        .map(num => parseFloat(num))
      
      if (numbers.some(isNaN)) {
        return null
      }
      return numbers
    } catch {
      return null
    }
  }

  // Handle form submission
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    
    const numbers = parseNumbers(inputValue)
    if (!numbers || numbers.length === 0) {
      alert('Please enter valid numbers separated by spaces')
      return
    }

    const backend = BACKENDS.find(b => b.value === selectedBackend)
    if (!backend) return

    // Build the API URL from backend base and selected algorithm
    const apiUrl = `${backend.url}/${selectedAlgorithm}`

    const request: SortRequest = {
      backend: selectedBackend,
      algorithm: selectedAlgorithm as any,
      numbers,
      apiUrl
    }

    onSort(request)
  }

  return (
    <form className="sort-form" onSubmit={handleSubmit}>
      <h2>Sort Configuration</h2>

      {/* Backend Selection Dropdown */}
      <div className="form-group">
        <label htmlFor="backend">Select Backend:</label>
        <select
          id="backend"
          value={selectedBackend}
          onChange={(e) => setSelectedBackend(e.target.value as 'python' | 'dotnet')}
          disabled={loading}
        >
          {BACKENDS.map(backend => (
            <option key={backend.value} value={backend.value}>
              {backend.name}
            </option>
          ))}
        </select>
      </div>

      {/* Algorithm Selection Dropdown */}
      <div className="form-group">
        <label htmlFor="algorithm">Select Algorithm:</label>
        <select
          id="algorithm"
          value={selectedAlgorithm}
          onChange={(e) => setSelectedAlgorithm(e.target.value)}
          disabled={loading}
        >
          {ALGORITHMS.map(algo => (
            <option key={algo} value={algo}>
              {algo.charAt(0).toUpperCase() + algo.slice(1)} Sort
            </option>
          ))}
        </select>
      </div>

      {/* Numbers Input Field */}
      <div className="form-group">
        <label htmlFor="numbers">Enter Numbers (space-separated):</label>
        <input
          id="numbers"
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="e.g., 5 2 8 1 9"
          disabled={loading}
        />
      </div>

      {/* Submit Button */}
      <button type="submit" disabled={loading} className="submit-btn">
        {loading ? 'Sorting...' : 'Sort'}
      </button>
    </form>
  )
}

export default SortForm
