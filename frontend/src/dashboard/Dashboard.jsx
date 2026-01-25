import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import api from '../api/axios'
import ScholarshipCard from './ScholarshipCard'
import MissedScholarships from './MissedScholarships'
import WhatIfSimulator from './WhatIfSimulator'

const Dashboard = () => {
  const [profile, setProfile] = useState(null)
  const [eligibleScholarships, setEligibleScholarships] = useState([])
  const [missedScholarships, setMissedScholarships] = useState([])
  const [showMissed, setShowMissed] = useState(false)
  const [showSimulator, setShowSimulator] = useState(false)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const { logout } = useAuth()
  const navigate = useNavigate()

  useEffect(() => {
    fetchData()
  }, [])

  const fetchData = async () => {
    setLoading(true)
    setError('')

    try {
      const [profileRes, eligibleRes, missedRes] = await Promise.all([
        api.get('/profile/'),
        api.get('/scholarships/eligible'),
        api.get('/scholarships/missed')
      ])

      setProfile(profileRes.data || null)
      setEligibleScholarships(eligibleRes.data || [])
      setMissedScholarships(missedRes.data || [])
    } catch (err) {
      console.error(err)
      setError('Failed to load data')
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return <div className="loading">Loading your scholarships...</div>
  }

  if (error) {
    return <div className="error-page">{error}</div>
  }

  return (
    <div className="dashboard">
      <nav className="dashboard-nav">
        <h1>🎓 AI Scholarship Finder</h1>
        <div className="nav-actions">
          <button
            onClick={() => navigate('/edit-profile')}
            className="btn-secondary"
          >
            Edit Profile
          </button>
          <button
            onClick={logout}
            className="btn-secondary"
          >
            Logout
          </button>
        </div>
      </nav>

      {profile && (
        <div className="profile-summary">
          <h2>Welcome, {profile.name || 'Student'}!</h2>

          <div className="profile-stats">
            <div className="stat">
              <span className="stat-label">CGPA:</span>
              <span className="stat-value">
                {profile.cgpa ?? 'N/A'}
              </span>
            </div>

            <div className="stat">
              <span className="stat-label">Income:</span>
              <span className="stat-value">
                ₹{Number(profile.income || 0).toLocaleString()}
              </span>
            </div>

            <div className="stat">
              <span className="stat-label">Category:</span>
              <span className="stat-value">
                {profile.category || 'N/A'}
              </span>
            </div>

            <div className="stat">
              <span className="stat-label">State:</span>
              <span className="stat-value">
                {profile.state || 'N/A'}
              </span>
            </div>
          </div>
        </div>
      )}

      <div className="dashboard-actions">
        <button
          onClick={() => setShowMissed(!showMissed)}
          className={showMissed ? 'btn-primary' : 'btn-secondary'}
        >
          {showMissed ? 'Hide' : 'Show'} Missed Scholarships ({missedScholarships.length})
        </button>

        <button
          onClick={() => setShowSimulator(!showSimulator)}
          className={showSimulator ? 'btn-primary' : 'btn-secondary'}
        >
          {showSimulator ? 'Hide' : 'Open'} What-If Simulator
        </button>
      </div>

      {showSimulator && profile && (
        <WhatIfSimulator
          currentCgpa={profile.cgpa ?? 0}
          currentIncome={profile.income ?? 0}
        />
      )}

      <div className="scholarships-section">
        <h2>✅ Eligible Scholarships ({eligibleScholarships.length})</h2>

        {eligibleScholarships.length === 0 ? (
          <p className="no-results">
            No eligible scholarships found. Try adjusting your profile.
          </p>
        ) : (
          <div className="scholarships-grid">
            {eligibleScholarships.map((scholarship) => (
              <ScholarshipCard
                key={scholarship._id}
                scholarship={scholarship}
              />
            ))}
          </div>
        )}
      </div>

      {showMissed && (
        <MissedScholarships scholarships={missedScholarships} />
      )}
    </div>
  )
}

export default Dashboard
