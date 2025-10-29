import React, { useEffect, useState } from 'react'
import NavBar from '../components/NavBar'
import Chart from '../components/Chart'

export default function Dashboard() {
  const [liveData, setLiveData] = useState([])

  useEffect(() => {
    const wsUrl = process.env.REACT_APP_WS_URL || 'ws://localhost:8000/ws'
    let ws
    try {
      ws = new WebSocket(wsUrl)
      ws.onopen = () => console.log('WS connected')
      ws.onmessage = (ev) => {
        try {
          const d = JSON.parse(ev.data)
          setLiveData((prev) => [...prev.slice(-199), d])
        } catch (e) {
          // ignore non-json
        }
      }
      ws.onclose = () => console.log('WS closed')
    } catch (e) {
      console.warn('WS init error', e)
    }

    return () => {
      try { ws && ws.close() } catch (e) {}
    }
  }, [])

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
