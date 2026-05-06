import { useState, useEffect } from 'react'

export default function KnowledgeBase() {
  const [files, setFiles] = useState([])

  useEffect(() => {
    fetch('/api/knowledge')
      .then(r => r.json())
      .then(setFiles)
      .catch(() => {})
  }, [])

  const getOWASPInfo = (filename) => {
    const map = {
      'A01': { icon: '🔓', title: 'Broken Access Control', color: '#ef4444' },
      'A02': { icon: '🔐', title: 'Cryptographic Failures', color: '#f97316' },
      'A03': { icon: '💉', title: 'Injection', color: '#ef4444' },
      'A04': { icon: '🏗️', title: 'Insecure Design', color: '#eab308' },
      'A05': { icon: '⚙️', title: 'Security Misconfiguration', color: '#f97316' },
      'A06': { icon: '📦', title: 'Vulnerable Components', color: '#eab308' },
      'A07': { icon: '🔑', title: 'Auth Failures', color: '#ef4444' },
      'A08': { icon: '🔗', title: 'Data Integrity Failures', color: '#3b82f6' },
      'A09': { icon: '📋', title: 'Logging Failures', color: '#3b82f6' },
      'A10': { icon: '🌐', title: 'SSRF', color: '#f97316' },
    }
    for (const [key, val] of Object.entries(map)) {
      if (filename.includes(key)) return val
    }
    return { icon: '📄', title: filename, color: '#64748b' }
  }

  return (
    <div>
      <div className="page-header">
        <h2>Knowledge Base</h2>
        <p>OWASP Top 10 reference files used by the AI during scans</p>
      </div>

      {files.length === 0 ? (
        <div className="empty-state">
          <div className="icon">📚</div>
          <p>No knowledge base files found.</p>
        </div>
      ) : (
        <div className="kb-grid">
          {files.map(file => {
            const info = getOWASPInfo(file.filename)
            return (
              <div key={file.filename} className="kb-card">
                <div style={{ fontSize: '32px', marginBottom: '12px' }}>{info.icon}</div>
                <div className="title" style={{ color: info.color }}>
                  {file.filename.replace('OWASP_', '').replace('.md', '').replaceAll('_', ' ')}
                </div>
                <div className="desc">{info.title}</div>
              </div>
            )
          })}
        </div>
      )}
    </div>
  )
}
