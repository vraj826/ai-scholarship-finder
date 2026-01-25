import React, { useEffect, useState } from 'react'
import { Navigate, useLocation } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import api from '../api/axios'

const ProtectedRoute = ({ children }) => {
  const { user, hasProfile, loading, updateProfileStatus } = useAuth()
  const location = useLocation()
  const [checking, setChecking] = useState(true)

  useEffect(() => {
    const checkProfile = async () => {
      if (user && !hasProfile && location.pathname === '/dashboard') {
        try {
          await api.get('/profile/')
          updateProfileStatus(true)
        } catch (error) {
          // Profile doesn't exist
          updateProfileStatus(false)
        }
      }
      setChecking(false)
    }

    if (!loading) {
      checkProfile()
    }
  }, [user, hasProfile, loading, location])

  if (loading || checking) {
    return <div className="loading">Loading...</div>
  }

  if (!user) {
    return <Navigate to="/login" replace />
  }

  // If trying to access dashboard without profile, redirect to onboarding
  if (location.pathname === '/dashboard' && !hasProfile) {
    return <Navigate to="/onboarding" replace />
  }

  // If trying to access onboarding with profile, redirect to dashboard
  if (location.pathname === '/onboarding' && hasProfile) {
    return <Navigate to="/dashboard" replace />
  }

  return children
}

export default ProtectedRoute