import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000'

export default function Login(){
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate()

  const submit = async (e) => {
    e.preventDefault()
    setError('')
    setLoading(true)
    
    try {
      const response = await fetch(`${API_URL}/api/v1/auth/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({
          username: email,  // OAuth2 expects username
          password: password
        })
      })

      const data = await response.json()
      
      if (!response.ok) {
        throw new Error(data.detail || 'Login failed')
      }

      // Store token
      localStorage.setItem('token', data.access_token)
      navigate('/dashboard')
      
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-50">
      <form onSubmit={submit} className="w-full max-w-md bg-white p-8 rounded shadow">
        <h1 className="text-2xl font-semibold mb-6">Sign in</h1>
        
        {error && (
          <div className="mb-4 p-3 bg-red-50 text-red-700 rounded">
            {error}
          </div>
        )}

        <label className="block mb-2 text-sm">Email</label>
        <input 
          type="email"
          required
          value={email} 
          onChange={(e)=>setEmail(e.target.value)} 
          className="w-full p-2 border rounded mb-4" 
        />
        
        <label className="block mb-2 text-sm">Password</label>
        <input 
          type="password"
          required
          value={password} 
          onChange={(e)=>setPassword(e.target.value)} 
          className="w-full p-2 border rounded mb-4" 
        />
        
        <button 
          type="submit"
          disabled={loading}
          className={`w-full py-2 rounded text-white ${
            loading ? 'bg-gray-400' : 'bg-primary-600 hover:bg-primary-700'
          }`}
        >
          {loading ? 'Signing in...' : 'Sign in'}
        </button>
      </form>
    </div>
  )
}
