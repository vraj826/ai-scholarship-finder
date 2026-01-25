import React, { useState } from 'react'

const MissedScholarshipCard = ({ scholarship }) => {
  const [showDetails, setShowDetails] = useState(false)

  return (
    <div className="scholarship-card missed">
      <div className="card-header">
        <h3>{scholarship.scholarship_name}</h3>
        <span className="not-eligible">Not Eligible</span>
      </div>
      
      <p className="provider">{scholarship.provider}</p>
      <p className="amount">₹{scholarship.amount.toLocaleString()}</p>
      
      <button
        onClick={() => setShowDetails(!showDetails)}
        className="btn-details"
      >
        {showDetails ? 'Hide Reasons' : 'Show Reasons'}
      </button>
      
      {showDetails && (
        <div className="card-details">
          <p className="description">{scholarship.description}</p>
          <div className="explanation">
            <strong>Why you're not eligible:</strong>
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

const MissedScholarships = ({ scholarships }) => {
  return (
    <div className="scholarships-section missed-section">
      <h2>❌ Missed Scholarships ({scholarships.length})</h2>
      {scholarships.length === 0 ? (
        <p className="no-results">Great! You're eligible for all available scholarships.</p>
      ) : (
        <div className="scholarships-grid">
          {scholarships.map((scholarship, idx) => (
            <MissedScholarshipCard key={idx} scholarship={scholarship} />
          ))}
        </div>
      )}
    </div>
  )
}

export default MissedScholarships