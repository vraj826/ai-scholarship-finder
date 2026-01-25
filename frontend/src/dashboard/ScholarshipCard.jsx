import React, { useState } from 'react'

const ScholarshipCard = ({ scholarship }) => {
  const [showDetails, setShowDetails] = useState(false)

  return (
    <div className="scholarship-card eligible">
      <div className="card-header">
        <h3>{scholarship.scholarship_name}</h3>
        <span className="match-score">Score: {scholarship.match_score}</span>
      </div>
      
      <p className="provider">{scholarship.provider}</p>
      <p className="amount">₹{scholarship.amount.toLocaleString()}</p>
      
      <button
        onClick={() => setShowDetails(!showDetails)}
        className="btn-details"
      >
        {showDetails ? 'Hide Details' : 'Show Details'}
      </button>
      
      {showDetails && (
        <div className="card-details">
          <p className="description">{scholarship.description}</p>
          <div className="explanation">
            <strong>Why you're eligible:</strong>
            <ul>
              {scholarship.explanation.map((reason, idx) => (
                <li key={idx}>{reason}</li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </div>
  )
}

export default ScholarshipCard