import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import api from '../api/axios'

const CATEGORIES = ['General', 'OBC', 'SC', 'ST']
const GENDERS = ['Male', 'Female', 'Other']
const MINORITIES = ['None', 'Muslim', 'Christian', 'Sikh', 'Buddhist', 'Jain', 'Parsi']
const STATES = [
  'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
  'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka',
  'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
  'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
  'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal',
  'Delhi', 'Jammu and Kashmir', 'Ladakh'
]

const EditProfile = () => {
  const [formData, setFormData] = useState({
    name: '',
    cgpa: '',
    income: '',
    category: 'General',
    gender: 'Male',
    state: 'Maharashtra',
    minority: 'None'
  })
  const [error, setError] = useState('')
  const [success, setSuccess] = useState(false)
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate()

  useEffect(() => {
    fetchProfile()
  }, [])

  const fetchProfile = async () => {
    try {
      const response = await api.get('/profile/')
      setFormData({
        name: response.data.name,
        cgpa: response.data.cgpa.toString(),
        income: response.data.income.toString(),
        category: response.data.category,
        gender: response.data.gender,
        state: response.data.state,
        minority: response.data.minority || 'None'
      })
    } catch (err) {
      setError('Failed to load profile')
    }
  }

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')
    setSuccess(false)
    setLoading(true)

    try {
      const profileData = {
        ...formData,
        cgpa: parseFloat(formData.cgpa),
        income: parseInt(formData.income),
        minority: formData.minority === 'None' ? null : formData.minority
      }

      await api.put('/profile/', profileData)
      setSuccess(true)
      setTimeout(() => navigate('/dashboard'), 1500)
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to update profile')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="onboarding-container">
      <div className="onboarding-card">
        <h1>Edit Your Profile</h1>
        
        {error && <div className="error-message">{error}</div>}
        {success && <div className="success-message">Profile updated successfully!</div>}
        
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Full Name *</label>
            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              required
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
              />
            </div>
          </div>

          <div className="form-row">
            <div className="form-group">
              <label>Category *</label>
              <select name="category" value={formData.category} onChange={handleChange} required>
                {CATEGORIES.map(cat => (
                  <option key={cat} value={cat}>{cat}</option>
                ))}
              </select>
            </div>

            <div className="form-group">
              <label>Gender *</label>
              <select name="gender" value={formData.gender} onChange={handleChange} required>
                {GENDERS.map(gen => (
                  <option key={gen} value={gen}>{gen}</option>
                ))}
              </select>
            </div>
          </div>

          <div className="form-group">
            <label>State *</label>
            <select name="state" value={formData.state} onChange={handleChange} required>
              {STATES.map(state => (
                <option key={state} value={state}>{state}</option>
              ))}
            </select>
          </div>

          <div className="form-group">
            <label>Minority Status</label>
            <select name="minority" value={formData.minority} onChange={handleChange}>
              {MINORITIES.map(min => (
                <option key={min} value={min}>{min}</option>
              ))}
            </select>
          </div>

          <div className="form-actions">
            <button type="button" onClick={() => navigate('/dashboard')} className="btn-secondary">
              Cancel
            </button>
            <button type="submit" disabled={loading} className="btn-primary">
              {loading ? 'Saving...' : 'Save Changes'}
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}

export default EditProfile