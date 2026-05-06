import { useState, useEffect } from 'react'
import { BrowserRouter, Routes, Route, NavLink } from 'react-router-dom'
import Dashboard from './pages/Dashboard'
import NewScan from './pages/NewScan'
import Reports from './pages/Reports'
import ReportView from './pages/ReportView'
import KnowledgeBase from './pages/KnowledgeBase'
import Tools from './pages/Tools'

function App() {
  const [apiStatus, setApiStatus] = useState(null)

  useEffect(() => {
    const checkStatus = async () => {
      try {
        const res = await fetch('/api/status')
        const data = await res.json()
        setApiStatus(data)
      } catch {
        setApiStatus(null)
      }
    }
    checkStatus()
    const interval = setInterval(checkStatus, 10000)
    return () => clearInterval(interval)
  }, [])

  return (
    <BrowserRouter>
      <div className="app">
        <aside className="sidebar">
          <div className="sidebar-logo">
            <div className="shield">🛡️</div>
            <div>
              <h1>Praedix</h1>
              <span>AI Security Firm</span>
            </div>
          </div>

          <nav className="sidebar-nav">
            <NavLink to="/" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`} end>
              <span className="nav-icon">📊</span> Dashboard
            </NavLink>
            <NavLink to="/scan" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
              <span className="nav-icon">🎯</span> New Scan
            </NavLink>
            <NavLink to="/reports" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
              <span className="nav-icon">📄</span> Reports
            </NavLink>
            <NavLink to="/tools" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
              <span className="nav-icon">🔧</span> Tools
            </NavLink>
            <NavLink to="/knowledge" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
              <span className="nav-icon">📚</span> Knowledge Base
            </NavLink>
          </nav>

          <div className="sidebar-status">
            <div style={{ fontSize: '12px', color: 'var(--text-muted)', marginBottom: '8px' }}>SYSTEM STATUS</div>
            <div style={{ fontSize: '13px', marginBottom: '6px' }}>
              <span className={`status-dot ${apiStatus ? 'online' : 'offline'}`}></span>
              API: {apiStatus ? 'Online' : 'Offline'}
            </div>
            <div style={{ fontSize: '13px' }}>
              <span className={`status-dot ${apiStatus?.scanner === 'online' ? 'online' : 'offline'}`}></span>
              Scanner: {apiStatus?.scanner || 'Offline'}
            </div>
            <div style={{ fontSize: '13px', marginTop: '6px' }}>
              <span className={`status-dot ${apiStatus?.database === 'online' ? 'online' : 'offline'}`}></span>
              Database: {apiStatus?.database || 'Offline'}
            </div>
            <div style={{ fontSize: '13px', marginTop: '6px' }}>
              <span className={`status-dot ${apiStatus?.onionclaw === 'online' && apiStatus?.onionclaw_installed ? 'online' : 'offline'}`}></span>
              OnionClaw: {apiStatus?.onionclaw_installed ? apiStatus?.onionclaw : 'Not installed'}
            </div>
          </div>
        </aside>

        <main className="main-content">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/scan" element={<NewScan />} />
            <Route path="/reports" element={<Reports />} />
            <Route path="/reports/:filename" element={<ReportView />} />
            <Route path="/tools" element={<Tools />} />
            <Route path="/knowledge" element={<KnowledgeBase />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  )
}

export default App
