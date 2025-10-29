import React from 'react'
import { Routes, Route, Navigate, HashRouter } from 'react-router-dom'
import Dashboard from './pages/Dashboard'
import Login from './pages/Login'
import ProtectedRoute from './components/ProtectedRoute'

const Layout = ({ children }) => {
  return (
    <div className="min-h-screen bg-slate-50">
      <div className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        {children}
      </div>
    </div>
  )
}

export default function App() {
  return (
    <HashRouter>
      <Layout>
        <Routes>
          <Route path="/" element={<Navigate to="/dashboard" replace />} />
          <Route 
            path="/dashboard" 
            element={
              <ProtectedRoute>
                <Dashboard />
              </ProtectedRoute>
            } 
          />
          <Route path="/login" element={<Login />} />
        </Routes>
      </Layout>
    </HashRouter>
  )
}
