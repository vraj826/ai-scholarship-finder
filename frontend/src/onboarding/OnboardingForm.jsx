import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import api from '../api/axios'

const CATEGORIES = ['General', 'OBC', 'SC', 'ST']
const GENDERS = ['Male', 'Female', 'Other']
const MINORITIES = ['None', 'Muslim', 'Christian', 'Sikh', 'Buddhist', 'Jain', 'Parsi']
const STATES = [
  'Andhra Pradesh',
  'Arunachal Pradesh',
  'Assam',
  'Bihar',
  'Chhattisgarh',
  'Goa',
  'Gujarat',
  'Haryana',
  'Himachal Pradesh',
  'Jharkhand',
  'Karnataka',
  'Kerala',
  'Madhya Pradesh',
  'Maharashtra',
  'Manipur',
  'Meghalaya',
  'Mizoram',
  'Nagaland',
  'Odisha',
  'Punjab',
  'Rajasthan',
  'Sikkim',
  'Tamil Nadu',
  'Telangana',
  'Tripura',
  'Uttar Pradesh',
  'Uttarakhand',
  'West Bengal',
  'Delhi',
  'Jammu and Kashmir',
  'Ladakh',
]

const OnboardingForm = () => {
  const [formData, setFormData] = useState({
    name: '',
    cgpa: '',
    income: '',
    category: 'General',
    gender: 'Male',
    state: 'Maharashtra',
    minority: 'None',
  })

  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  const navigate = useNavigate()
  const { updateProfileStatus } = useAuth()

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')
    setLoading(true)

    try {
      const profileData = {
        ...formData,
        cgpa: parseFloat(formData.cgpa),
        income: parseInt(formData.income),
        minority: formData.minority === 'None' ? null : formData.minority,
      }

      await api.post('/profile/', profileData)
      updateProfileStatus(true)
      navigate('/dashboard')
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to create profile')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="onboarding-container">
      <div className="onboarding-card">
        <h1>Complete Your Profile</h1>
        <p>Help us find the best scholarships for you</p>

        {error && <div className="error-message">{error}</div>}

        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Full Name *</label>
            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              required
              placeholder="Enter your full name"
            />
          </div>

          <div className="form-row">
            <div className="form-group">
              <label>CGPA (0-10) *</label>
              <input
                type="number"
                name="cgpa"
                value={formData.cgpa}
                onChange={handleChange}
                required
                min="0"
                max="10"
                step="0.01"
                placeholder="e.g., 8.5"
              />
            </div>

            <div className="form-group">
              <label>Annual Family Income (₹) *</label>
              <input
                type="number"
                name="income"
                value={formData.income}
                onChange={handleChange}
                required
                min="0"
                placeholder="e.g., 500000"
              />
            </div>
          </div>

          <div className="form-row">
            <div className="form-group">
              <label>Category *</label>
              <select
                name="category"
                value={formData.category}
                onChange={handleChange}
                required
              >
                {CATEGORIES.map((cat) => (
                  <option key={cat} value={cat}>
                    {cat}
                  </option>
                ))}
              </select>
            </div>

            <div className="form-group">
              <label>Gender *</label>
              <select
                name="gender"
                value={formData.gender}
                onChange={handleChange}
                required
              >
                {GENDERS.map((gen) => (
                  <option key={gen} value={gen}>
                    {gen}
                  </option>
                ))}
              </select>
            </div>
          </div>

          <div className="form-group">
            <label>State *</label>
            <select
              name="state"
              value={formData.state}
              onChange={handleChange}
              required
            >
              {STATES.map((state) => (
                <option key={state} value={state}>
                  {state}
                </option>
              ))}
            </select>
          </div>

          <div className="form-group">
            <label>Minority Status</label>
            <select
              name="minority"
              value={formData.minority}
              onChange={handleChange}
            >
              {MINORITIES.map((min) => (
                <option key={min} value={min}>
                  {min}
                </option>
              ))}
            </select>
          </div>

          <button type="submit" disabled={loading} className="btn-primary">
            {loading ? 'Saving Profile...' : 'Continue to Dashboard'}
          </button>
        </form>
      </div>
    </div>
  )
}

export default OnboardingForm
