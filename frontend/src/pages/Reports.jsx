import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'

export default function Reports() {
  const [reports, setReports] = useState([])
  const navigate = useNavigate()

  useEffect(() => {
    fetch('/api/reports')
      .then(r => r.json())
      .then(setReports)
      .catch(() => {})
  }, [])

  return (
    <div>
      <div className="page-header">
        <h2>Reports</h2>
        <p>All generated security audit reports</p>
      </div>

      {reports.length === 0 ? (
        <div className="empty-state">
          <div className="icon">📄</div>
          <p>No reports yet. Run a scan to generate your first report!</p>
        </div>
      ) : (
        <div className="report-list">
          {reports.map(report => {
            const parts = report.filename.replace('.md', '').split('_')
            const date = parts.slice(0, 2).join(' ').replace('-', ':')
            const target = parts.slice(2).join('.')

            return (
              <div
                key={report.filename}
                className="report-card"
                onClick={() => navigate(`/reports/${report.filename}`)}
              >
                <div>
                  <div className="name">🛡️ {target || report.filename}</div>
                  <div className="meta">
                    📅 {date} &nbsp;|&nbsp; 📦 {(report.size / 1024).toFixed(1)} KB
                  </div>
                </div>
                <span style={{ color: 'var(--accent)', fontSize: '20px' }}>→</span>
              </div>
            )
          })}
        </div>
      )}
    </div>
  )
}
