import React, { useEffect, useState, useCallback } from 'react'
import { useNavigate } from 'react-router-dom'
import NavBar from '../components/NavBar'
import Chart from '../components/Chart'

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000'
const WS_URL = process.env.REACT_APP_WS_URL || 'ws://localhost:8000/ws'

export default function Dashboard() {
  const [liveData, setLiveData] = useState([])
  const [portfolio, setPortfolio] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const navigate = useNavigate()

  const connectWebSocket = useCallback(() => {
    const token = localStorage.getItem('token')
    if (!token) {
      navigate('/login')
      return
    }

    const ws = new WebSocket(`${WS_URL}?token=${token}`)
    
    ws.onopen = () => {
      console.log('WebSocket connected')
      setError('')
    }

    ws.onmessage = (ev) => {
      try {
        const data = JSON.parse(ev.data)
        if (data.event === 'marketData') {
          setLiveData((prev) => [...prev.slice(-199), data.data])
        } else if (data.event === 'portfolio') {
          setPortfolio(data.data)
        }
      } catch (e) {
        console.warn('WebSocket message parse error:', e)
      }
    }

    ws.onclose = (ev) => {
      console.log('WebSocket closed:', ev.reason)
      if (ev.code === 1008) {  // Policy violation (auth error)
        navigate('/login')
      } else {
        setError('Connection lost. Retrying...')
        setTimeout(connectWebSocket, 5000)  // Retry after 5s
      }
    }

    ws.onerror = (ev) => {
      console.error('WebSocket error:', ev)
      setError('Connection error')
    }

    return ws
  }, [navigate])

  useEffect(() => {
    const ws = connectWebSocket()
    setLoading(false)
    
    return () => {
      try { ws.close() } catch (e) {}
    }
  }, [connectWebSocket])

  return (
    <div>
      <NavBar />
      <main className="p-6">
        <h1 className="text-2xl font-semibold mb-4">Dashboard</h1>
        <section className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div className="col-span-2 bg-white rounded shadow p-4">
            <Chart data={liveData} />
          </div>
          <aside className="bg-white rounded shadow p-4">
            <h2 className="text-lg font-medium">Portfolio</h2>
            <div className="mt-3 text-sm text-slate-600">Placeholder for portfolio summary, P&L, positions.</div>
          </aside>
        </section>
      </main>
    </div>
  )
}
