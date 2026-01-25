import React, { useState } from 'react'

const ScholarshipCard = ({ scholarship }) => {
  const [showDetails, setShowDetails] = useState(false)

  const isEligible = scholarship.is_eligible

  return (
    <div
      className={`scholarship-card ${isEligible ? 'eligible' : 'missed'}`}
    >
      <div className="card-header">
        <h3>{scholarship.scholarship_name}</h3>

        <span className={isEligible ? 'eligible-badge' : 'not-eligible'}>
          {isEligible ? 'Eligible' : 'Not Eligible'}
        </span>
      </div>

      <p className="provider">{scholarship.provider}</p>
      <p className="amount">
        ₹{scholarship.amount.toLocaleString()}
      </p>

      <button
        onClick={() => setShowDetails(!showDetails)}
        className="btn-details"
      >
        {showDetails
          ? isEligible
            ? 'Hide Details'
            : 'Hide Reasons'
          : isEligible
            ? 'Show Details'
            : 'Show Reasons'}
      </button>

      {showDetails && (
        <div className="card-details">
          <p className="description">{scholarship.description}</p>

          <div className="explanation">
            <strong>
              {isEligible
                ? "Why you're eligible:"
                : "Why you're not eligible:"}
            </strong>

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
