import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'

export default function Dashboard() {
  const [status, setStatus] = useState(null)
  const [scans, setScans] = useState([])
  const [reports, setReports] = useState([])
  const navigate = useNavigate()

  useEffect(() => {
    fetch('/api/status').then(r => r.json()).then(setStatus).catch(() => {})
    fetch('/api/scans').then(r => r.json()).then(setScans).catch(() => {})
    fetch('/api/reports').then(r => r.json()).then(setReports).catch(() => {})
  }, [])

  const activeScans = scans.filter(s => !['done', 'error'].includes(s.status))
  const researchScans = scans.filter(s => s.stream_type === 'research')
  const localScans = scans.filter(s => (s.stream_type || 'local_vm') === 'local_vm')

  return (
    <div>
      <div className="page-header">
        <h2>Dashboard</h2>
        <p>Overview of your security operations</p>
      </div>

      <div className="stats-grid">
        <div className="stat-card">
          <div className="label">Total Scans</div>
          <div className="value accent">{scans.length}</div>
        </div>
        <div className="stat-card">
          <div className="label">Active Scans</div>
          <div className="value" style={{ color: activeScans.length > 0 ? 'var(--accent)' : 'var(--text-muted)' }}>
            {activeScans.length}
          </div>
        </div>
        <div className="stat-card">
          <div className="label">Research Stream</div>
          <div className="value" style={{ color: '#8b5cf6' }}>{researchScans.length}</div>
        </div>
        <div className="stat-card">
          <div className="label">Local VM Stream</div>
          <div className="value success">{localScans.length}</div>
        </div>
      </div>

      {activeScans.length > 0 && (
        <div className="scan-panel" style={{ borderColor: 'var(--accent)', marginBottom: '24px' }}>
          <h3 style={{ marginBottom: '16px', color: 'var(--accent)' }}>Active Scans</h3>
          {activeScans.map(scan => (
            <div key={scan.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '12px', background: 'var(--bg-primary)', borderRadius: '8px', marginBottom: '8px' }}>
              <div>
                <span style={{ fontFamily: 'var(--font-mono)', color: 'var(--accent)' }}>{scan.target}</span>
                <span style={{ color: 'var(--text-muted)', marginLeft: '12px', fontSize: '13px' }}>
                  Step {scan.current_step}/{scan.max_steps}
                </span>
                <span style={{ color: 'var(--text-muted)', marginLeft: '12px', fontSize: '12px', textTransform: 'uppercase' }}>
                  {scan.stream_type || 'local_vm'} / {scan.scan_profile || 'standard'} / {scan.workflow_status || 'queued'}
                </span>
              </div>
              <div className="spinner"></div>
            </div>
          ))}
        </div>
      )}

      <div className="scan-panel">
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '16px' }}>
          <h3>Recent Reports</h3>
          <button className="btn btn-primary" onClick={() => navigate('/scan')} style={{ padding: '10px 20px' }}>
            New Scan
          </button>
        </div>

        {reports.length === 0 ? (
          <div className="empty-state">
            <div className="icon">REPORT</div>
            <p>No reports yet. Start your first scan!</p>
          </div>
        ) : (
          <div className="report-list">
            {reports.slice(0, 5).map(report => (
              <div
                key={report.filename}
                className="report-card"
                onClick={() => navigate(`/reports/${report.filename}`)}
              >
                <div>
                  <div className="name">{report.filename}</div>
                  <div className="meta">{(report.size / 1024).toFixed(1)} KB</div>
                </div>
                <span style={{ color: 'var(--accent)', fontSize: '20px' }}>-&gt;</span>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}
