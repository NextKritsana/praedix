import { useState, useEffect, useRef } from 'react'

export default function NewScan() {
  const [target, setTarget] = useState('')
  const [streamType, setStreamType] = useState('local_vm')
  const [scanProfile, setScanProfile] = useState('standard')
  const [researchScope, setResearchScope] = useState({
    enable_dark_web: false,
    client: '',
    allowed_keywords: '',
    blocked_keywords: '',
    allow_onion_fetch: false,
    allow_identity_rotation: false,
    approved: false,
    approved_by: '',
    notes: '',
  })
  const [scanning, setScanning] = useState(false)
  const [scanId, setScanId] = useState(null)
  const [scanData, setScanData] = useState(null)
  const [expandedStep, setExpandedStep] = useState(null)
  const intervalRef = useRef(null)
  const bottomRef = useRef(null)

  const startScan = async () => {
    if (!target.trim()) return
    setScanning(true)
    setScanData(null)
    setExpandedStep(null)

    try {
      const body = { target: target.trim(), stream_type: streamType, scan_profile: scanProfile }
      if (streamType === 'research') {
        body.research_scope = {
          ...researchScope,
          allowed_keywords: researchScope.allowed_keywords || target.trim(),
          approved_by: researchScope.approved_by || 'human-review',
        }
      }
      const res = await fetch('/api/scan', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
      })
      const data = await res.json()
      if (!res.ok) throw new Error(data.error || 'Failed to start scan')
      setScanId(data.scan_id)
    } catch (err) {
      alert('Failed to start scan: ' + err.message)
      setScanning(false)
    }
  }

  useEffect(() => {
    if (!scanId) return

    const poll = async () => {
      try {
        const res = await fetch(`/api/scan/${scanId}`)
        const data = await res.json()
        setScanData(data)
        if (data.status === 'done') {
          setScanning(false)
          clearInterval(intervalRef.current)
        }
      } catch {}
    }

    poll()
    intervalRef.current = setInterval(poll, 2000)
    return () => clearInterval(intervalRef.current)
  }, [scanId])

  // Auto-scroll to bottom when new steps appear
  useEffect(() => {
    if (bottomRef.current) {
      bottomRef.current.scrollIntoView({ behavior: 'smooth' })
    }
  }, [scanData?.steps?.length])

  const progress = scanData ? (scanData.current_step / scanData.max_steps) * 100 : 0

  const streamOptions = [
    {
      id: 'local_vm',
      name: 'Local VM Testing',
      desc: 'OWASP checks and pre-deploy report for local apps',
      color: '#10b981',
    },
    {
      id: 'research',
      name: 'Vulnerability Research',
      desc: 'Recon, CVE triage, and advisory workflow',
      color: '#8b5cf6',
    },
  ]

  const profileOptions = [
    {
      id: 'standard',
      name: 'Standard Audit',
      desc: 'Balanced scan path for quick evidence-backed checks',
      color: '#06b6d4',
    },
    {
      id: 'web_deep',
      name: 'Web App Deep Scan',
      desc: 'Adds subfinder, httpx, katana, ffuf, and nuclei',
      color: '#f97316',
    },
  ]

  const getStepIcon = (step) => {
    if (step.status === 'running') return '⏳'
    if (step.exit_code === 0) return '✅'
    if (step.exit_code === -1) return '⏱️'
    return '❌'
  }

  const getToolName = (cmd) => {
    const tool = cmd.split(' ')[0]
    const colors = {
      nmap: '#06b6d4',
      nikto: '#f97316',
      dirb: '#eab308',
      sqlmap: '#ef4444',
      whois: '#3b82f6',
      subfinder: '#14b8a6',
      httpx: '#22c55e',
      katana: '#a855f7',
      ffuf: '#f59e0b',
      nuclei: '#f43f5e',
    }
    return { name: tool, color: colors[tool] || '#94a3b8' }
  }

  const updateResearchScope = (field, value) => {
    setResearchScope(prev => ({ ...prev, [field]: value }))
  }

  const canStart = target.trim() && (!scanning) && (
    streamType !== 'research' ||
    !researchScope.enable_dark_web ||
    (researchScope.approved && (researchScope.allowed_keywords || target.trim()))
  )

  return (
    <div>
      <div className="page-header">
        <h2>New Scan</h2>
        <p>Enter a target to begin autonomous security audit</p>
      </div>

      <div className="scan-panel">
        <label style={{ fontSize: '14px', color: 'var(--text-secondary)', marginBottom: '10px', display: 'block' }}>
          Workflow stream
        </label>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '10px', marginBottom: '18px' }}>
          {streamOptions.map(option => {
            const selected = streamType === option.id
            return (
              <button
                key={option.id}
                type="button"
                onClick={() => setStreamType(option.id)}
                disabled={scanning}
                style={{
                  textAlign: 'left',
                  cursor: scanning ? 'not-allowed' : 'pointer',
                  border: `1px solid ${selected ? option.color : 'var(--border)'}`,
                  background: selected ? `${option.color}18` : 'var(--bg-primary)',
                  color: 'var(--text-primary)',
                  borderRadius: '8px',
                  padding: '12px 14px',
                }}
              >
                <div style={{ fontWeight: 700, color: option.color, marginBottom: '4px' }}>{option.name}</div>
                <div style={{ fontSize: '12px', color: 'var(--text-muted)', lineHeight: 1.4 }}>{option.desc}</div>
              </button>
            )
          })}
        </div>

        <label style={{ fontSize: '14px', color: 'var(--text-secondary)', marginBottom: '10px', display: 'block' }}>
          Scan profile
        </label>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '10px', marginBottom: '18px' }}>
          {profileOptions.map(option => {
            const selected = scanProfile === option.id
            return (
              <button
                key={option.id}
                type="button"
                onClick={() => setScanProfile(option.id)}
                disabled={scanning}
                style={{
                  textAlign: 'left',
                  cursor: scanning ? 'not-allowed' : 'pointer',
                  border: `1px solid ${selected ? option.color : 'var(--border)'}`,
                  background: selected ? `${option.color}18` : 'var(--bg-primary)',
                  color: 'var(--text-primary)',
                  borderRadius: '8px',
                  padding: '12px 14px',
                }}
              >
                <div style={{ fontWeight: 700, color: option.color, marginBottom: '4px' }}>{option.name}</div>
                <div style={{ fontSize: '12px', color: 'var(--text-muted)', lineHeight: 1.4 }}>{option.desc}</div>
              </button>
            )
          })}
        </div>

        {streamType === 'research' && (
          <div style={{ border: '1px solid var(--border)', background: 'var(--bg-primary)', borderRadius: '8px', padding: '14px', marginBottom: '18px' }}>
            <label style={{ display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--text-primary)', fontWeight: 700 }}>
              <input
                type="checkbox"
                checked={researchScope.enable_dark_web}
                onChange={e => updateResearchScope('enable_dark_web', e.target.checked)}
                disabled={scanning}
              />
              Search dark web / OSINT with OnionClaw
            </label>
            <div style={{ color: 'var(--text-muted)', fontSize: '12px', marginTop: '6px', marginBottom: researchScope.enable_dark_web ? '12px' : 0 }}>
              Leave this off for normal web vulnerability research.
            </div>
            {researchScope.enable_dark_web && (
              <>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '10px', marginBottom: '10px' }}>
                  <input
                    className="scan-input"
                    placeholder="Client or engagement name"
                    value={researchScope.client}
                    onChange={e => updateResearchScope('client', e.target.value)}
                    disabled={scanning}
                  />
                  <input
                    className="scan-input"
                    placeholder="Allowed keywords, comma separated"
                    value={researchScope.allowed_keywords}
                    onChange={e => updateResearchScope('allowed_keywords', e.target.value)}
                    disabled={scanning}
                  />
                </div>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '10px', marginBottom: '10px' }}>
                  <input
                    className="scan-input"
                    placeholder="Extra blocked keywords, comma separated"
                    value={researchScope.blocked_keywords}
                    onChange={e => updateResearchScope('blocked_keywords', e.target.value)}
                    disabled={scanning}
                  />
                  <input
                    className="scan-input"
                    placeholder="Approved by"
                    value={researchScope.approved_by}
                    onChange={e => updateResearchScope('approved_by', e.target.value)}
                    disabled={scanning}
                  />
                </div>
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: '14px', color: 'var(--text-secondary)', fontSize: '13px' }}>
              <label>
                <input
                  type="checkbox"
                  checked={researchScope.allow_identity_rotation}
                  onChange={e => updateResearchScope('allow_identity_rotation', e.target.checked)}
                  disabled={scanning}
                /> Allow Tor identity rotation
              </label>
              <label>
                <input
                  type="checkbox"
                  checked={researchScope.allow_onion_fetch}
                  onChange={e => updateResearchScope('allow_onion_fetch', e.target.checked)}
                  disabled={scanning}
                /> Allow .onion fetch
              </label>
              <label>
                <input
                  type="checkbox"
                  checked={researchScope.approved}
                  onChange={e => updateResearchScope('approved', e.target.checked)}
                  disabled={scanning}
                /> Human-approved scope
              </label>
            </div>
              </>
            )}
          </div>
        )}

        <label style={{ fontSize: '14px', color: 'var(--text-secondary)', marginBottom: '4px', display: 'block' }}>
          Target (domain, IP, or Docker service name)
        </label>
        <div className="scan-input-group">
          <input
            className="scan-input"
            placeholder="e.g. dvwa, scanme.nmap.org, 192.168.1.1"
            value={target}
            onChange={e => setTarget(e.target.value)}
            onKeyDown={e => e.key === 'Enter' && startScan()}
            disabled={scanning}
          />
          <button
            className="btn btn-primary"
            onClick={startScan}
            disabled={!canStart}
          >
            {scanning ? <><span className="spinner"></span> Scanning...</> : '🚀 Start Audit'}
          </button>
        </div>
      </div>

      {scanData && (
        <div className="scan-progress">
          <div className="progress-header">
            <div>
              <span style={{ fontWeight: 600 }}>Target: </span>
              <span style={{ color: 'var(--accent)', fontFamily: 'var(--font-mono)' }}>{scanData.target}</span>
              <span style={{ marginLeft: '16px', fontSize: '12px', color: 'var(--text-secondary)', background: 'var(--bg-primary)', padding: '3px 10px', borderRadius: '12px', textTransform: 'uppercase' }}>
                {scanData.stream_type || 'local_vm'}
              </span>
              <span style={{ marginLeft: '8px', fontSize: '12px', color: '#f97316', background: 'rgba(249,115,22,0.1)', padding: '3px 10px', borderRadius: '12px', textTransform: 'uppercase' }}>
                {scanData.scan_profile || 'standard'}
              </span>
              <span style={{ marginLeft: '8px', fontSize: '12px', color: 'var(--accent)', background: 'rgba(6,182,212,0.1)', padding: '3px 10px', borderRadius: '12px' }}>
                {scanData.workflow_status || 'queued'}
              </span>
              {scanData.kb_loaded > 0 && (
                <span style={{ marginLeft: '16px', fontSize: '12px', color: 'var(--success)', background: 'rgba(16,185,129,0.1)', padding: '3px 10px', borderRadius: '12px' }}>
                  📚 {scanData.kb_loaded} KB files loaded
                </span>
              )}
            </div>
            <div style={{ fontSize: '13px', color: 'var(--text-muted)' }}>
              {scanData.status === 'done' ? '✅ Complete' :
               scanData.status === 'loading_kb' ? '📚 Loading Knowledge Base...' :
               `Step ${scanData.current_step}/${scanData.max_steps}`}
            </div>
          </div>

          <div className="progress-bar-track">
            <div className="progress-bar-fill" style={{ width: `${scanData.status === 'done' ? 100 : progress}%` }}></div>
          </div>

          <div className="step-list">
            {scanData.steps.map((step, i) => {
              const tool = getToolName(step.command)
              const isExpanded = expandedStep === i
              const isLatest = i === scanData.steps.length - 1 && scanning

              return (
                <div key={i}>
                  <div
                    className="step-item"
                    onClick={() => setExpandedStep(isExpanded ? null : i)}
                    style={{
                      cursor: 'pointer',
                      borderLeft: `3px solid ${tool.color}`,
                      background: isLatest ? 'rgba(6, 182, 212, 0.05)' : 'var(--bg-primary)',
                    }}
                  >
                    <span className="step-status">{getStepIcon(step)}</span>
                    <span style={{
                      color: tool.color,
                      fontFamily: 'var(--font-mono)',
                      fontSize: '11px',
                      background: `${tool.color}20`,
                      padding: '2px 8px',
                      borderRadius: '4px',
                      fontWeight: 600,
                    }}>
                      {tool.name}
                    </span>
                    <span className="step-cmd">{step.command}</span>
                    <span className={`step-exit ${step.status === 'running' ? 'running' : step.exit_code === 0 ? 'success' : 'error'}`}>
                      {step.status === 'running' ? (
                        <><span className="spinner" style={{ width: 12, height: 12, borderWidth: 1.5 }}></span> running</>
                      ) : (
                        `exit: ${step.exit_code}`
                      )}
                    </span>
                    <span style={{ color: 'var(--text-muted)', fontSize: '12px', marginLeft: '8px' }}>
                      {isExpanded ? '▲' : '▼'}
                    </span>
                  </div>

                  {isExpanded && step.output && (
                    <div style={{
                      background: '#0a0e17',
                      border: '1px solid var(--border)',
                      borderTop: 'none',
                      borderRadius: '0 0 8px 8px',
                      padding: '16px',
                      fontFamily: 'var(--font-mono)',
                      fontSize: '12px',
                      lineHeight: '1.6',
                      color: '#a0f0a0',
                      whiteSpace: 'pre-wrap',
                      maxHeight: '300px',
                      overflowY: 'auto',
                    }}>
                      {step.output || 'No output'}
                    </div>
                  )}
                </div>
              )
            })}
            <div ref={bottomRef} />
          </div>
        </div>
      )}

      {scanData?.report && (
        <div className="report-content">
          <h2 style={{ marginTop: 0, display: 'flex', alignItems: 'center', gap: '12px' }}>
            📋 Audit Report
            {scanData.report_file && (
              <span style={{ fontSize: '12px', color: 'var(--success)', fontWeight: 400 }}>
                💾 Saved to vault
              </span>
            )}
          </h2>
          <div style={{ whiteSpace: 'pre-wrap', lineHeight: '1.8', marginTop: '16px' }}>
            {scanData.report}
          </div>
        </div>
      )}
    </div>
  )
}
