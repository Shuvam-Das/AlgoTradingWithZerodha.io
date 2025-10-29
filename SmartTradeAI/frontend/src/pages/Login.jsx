import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'

export default function Login(){
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const navigate = useNavigate()

  const submit = async (e) => {
    e.preventDefault()
    // Placeholder: POST to /api/v1/auth/login and handle tokens
    navigate('/dashboard')
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-50">
      <form onSubmit={submit} className="w-full max-w-md bg-white p-8 rounded shadow">
        <h1 className="text-2xl font-semibold mb-6">Sign in</h1>
        <label className="block mb-2 text-sm">Email</label>
        <input value={email} onChange={(e)=>setEmail(e.target.value)} className="w-full p-2 border rounded mb-4" />
        <label className="block mb-2 text-sm">Password</label>
        <input type="password" value={password} onChange={(e)=>setPassword(e.target.value)} className="w-full p-2 border rounded mb-4" />
        <button className="w-full bg-primary-600 text-white py-2 rounded">Sign in</button>
      </form>
    </div>
  )
}
