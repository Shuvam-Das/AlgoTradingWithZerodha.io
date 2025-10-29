import React from 'react'
import { Link } from 'react-router-dom'

export default function NavBar(){
  return (
    <header className="bg-white border-b">
      <div className="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="text-xl font-bold">SmartTradeAI</div>
          <div className="text-sm text-slate-500">AI Trading Dashboard</div>
        </div>
        <nav className="flex items-center gap-4">
          <Link to="/dashboard" className="text-slate-700">Dashboard</Link>
          <Link to="/login" className="text-slate-700">Sign in</Link>
        </nav>
      </div>
    </header>
  )
}
