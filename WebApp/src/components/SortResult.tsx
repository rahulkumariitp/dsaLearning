import { SortResponse } from '../types'
import './SortResult.css'

interface SortResultProps {
  result: SortResponse
}

// SortResult component - displays the sorting results
// Props: result object containing sorted numbers and time taken
function SortResult({ result }: SortResultProps) {
  // Handle both Python and .NET response formats
  const sortedNumbers = result.sorted_numbers || result.sortedNumbers || []
  const timeTaken = result.time_taken_ms || result.timeTakenMs || 0

  return (
    <div className="sort-result">
      <h2>Results</h2>
      
      {/* Display sorted numbers */}
      <div className="result-item">
        <h3>Sorted Array:</h3>
        <div className="array-display">
          {sortedNumbers.length > 0 ? (
            <div className="numbers-list">
              {sortedNumbers.map((num, index) => (
                <span key={index} className="number-badge">
                  {num}
                </span>
              ))}
            </div>
          ) : (
            <p className="empty-message">No numbers to display</p>
          )}
        </div>
      </div>

      {/* Display execution time */}
      <div className="result-item">
        <h3>Execution Time:</h3>
        <div className="time-display">
          <span className="time-value">{timeTaken.toFixed(4)}</span>
          <span className="time-unit">ms</span>
        </div>
      </div>

      {/* Display statistics */}
      <div className="result-item">
        <h3>Statistics:</h3>
        <div className="stats">
          <p><strong>Array Size:</strong> {sortedNumbers.length}</p>
          <p><strong>Min Value:</strong> {sortedNumbers.length > 0 ? Math.min(...sortedNumbers) : 'N/A'}</p>
          <p><strong>Max Value:</strong> {sortedNumbers.length > 0 ? Math.max(...sortedNumbers) : 'N/A'}</p>
        </div>
      </div>
    </div>
  )
}

export default SortResult
