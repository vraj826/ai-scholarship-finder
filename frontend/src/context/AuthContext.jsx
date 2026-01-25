import React, { createContext, useState, useContext, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/axios";

const AuthContext = createContext(null);

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within AuthProvider");
  }
  return context;
};

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [hasProfile, setHasProfile] = useState(false);
  const [loading, setLoading] = useState(true);

  const navigate = useNavigate();

  // 🔹 Load auth state from localStorage on app start
  useEffect(() => {
    const token = localStorage.getItem("token");
    const storedHasProfile = localStorage.getItem("hasProfile") === "true";

    if (token) {
      setUser({ token });
      setHasProfile(storedHasProfile);
    }

    setLoading(false);
  }, []);

  // 🔹 Login handler
  const login = (token, profileExists) => {
    localStorage.setItem("token", token);
    localStorage.setItem("hasProfile", profileExists.toString());

    setUser({ token });
    setHasProfile(profileExists);

    // 🔐 Delay navigation to avoid render race conditions
    setTimeout(() => {
      if (profileExists) {
        navigate("/dashboard");
      } else {
        navigate("/onboarding");
      }
    }, 0);
  };

  // 🔹 Logout handler
  const logout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("hasProfile");

    setUser(null);
    setHasProfile(false);

    setTimeout(() => {
      navigate("/login");
    }, 0);
  };

  // 🔹 Update profile completion status
  const updateProfileStatus = (status) => {
    localStorage.setItem("hasProfile", status.toString());
    setHasProfile(status);
  };

  // ⏳ Prevent rendering until auth state is resolved
  if (loading) {
    return null;
  }

  return (
    <AuthContext.Provider
      value={{
        user,
        hasProfile,
        loading,
        login,
        logout,
        updateProfileStatus,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};
