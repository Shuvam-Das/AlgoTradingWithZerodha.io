import React from 'react'
import { Link, useNavigate } from 'react-router-dom'

export default function NavBar(){
  const navigate = useNavigate()
  const token = localStorage.getItem('token')

  const handleLogout = () => {
    localStorage.removeItem('token')
    navigate('/login')
  }

  return (
    <header className="bg-white border-b">
      <div className="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="text-xl font-bold">SmartTradeAI</div>
          <div className="text-sm text-slate-500">AI Trading Dashboard</div>
        </div>
        <nav className="flex items-center gap-4">
          {token ? (
            <>
              <Link to="/dashboard" className="text-slate-700">Dashboard</Link>
              <button 
                onClick={handleLogout} 
                className="text-slate-700 hover:text-slate-900"
              >
                Sign out
              </button>
            </>
          ) : (
            <Link to="/login" className="text-slate-700">Sign in</Link>
          )}
        </nav>
      </div>
    </header>
  )
}
