import React, { useState } from 'react'
import api from '../api/axios'

const WhatIfSimulator = ({ currentCgpa, currentIncome }) => {
  const [cgpa, setCgpa] = useState(currentCgpa)
  const [income, setIncome] = useState(currentIncome)
  const [results, setResults] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const runSimulation = async () => {
    setError('')
    setLoading(true)

    try {
      const response = await api.post('/scholarships/what-if', {
        cgpa: parseFloat(cgpa),
        income: parseInt(income)
      })
      setResults(response.data)
    } catch (err) {
      setError('Simulation failed')
    } finally {
      setLoading(false)
    }
  }

  const eligibleCount = results ? results.filter(s => s.is_eligible).length : 0
  const newlyEligible = results ? results.filter(s => s.is_eligible).slice(0, 5) : []

  return (
    <div className="what-if-simulator">
      <h2>🔮 What-If Simulator</h2>
      <p>Explore how changing your CGPA or income affects scholarship eligibility</p>

      <div className="simulator-inputs">
        <div className="form-group">
          <label>Simulated CGPA (0-10)</label>
          <input
            type="number"
            value={cgpa}
            onChange={(e) => setCgpa(e.target.value)}
            min="0"
            max="10"
            step="0.1"
          />
        </div>

        <div className="form-group">
          <label>Simulated Income (₹)</label>
          <input
            type="number"
            value={income}
            onChange={(e) => setIncome(e.target.value)}
            min="0"
            step="10000"
          />
        </div>

        <button onClick={runSimulation} disabled={loading} className="btn-primary">
          {loading ? 'Running...' : 'Run Simulation'}
        </button>
      </div>

      {error && <div className="error-message">{error}</div>}

      {results && (
        <div className="simulation-results">
          <div className="results-summary">
            <h3>Simulation Results</h3>
            <p className="eligible-count">
              With CGPA {cgpa} and income ₹{parseInt(income).toLocaleString()}, 
              you would be eligible for <strong>{eligibleCount}</strong> scholarships
            </p>
          </div>

          {newlyEligible.length > 0 && (
            <div className="top-matches">
              <h4>Top Eligible Scholarships:</h4>
              {newlyEligible.map((scholarship, idx) => (
                <div key={idx} className="simulation-card">
                  <h5>{scholarship.scholarship_name}</h5>
                  <p className="amount">₹{scholarship.amount.toLocaleString()}</p>
                  <p className="score">Match Score: {scholarship.match_score}</p>
                  <ul className="mini-explanation">
                    {scholarship.explanation.slice(0, 3).map((reason, i) => (
                      <li key={i}>{reason}</li>
                    ))}
                  </ul>
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  )
}

export default WhatIfSimulator