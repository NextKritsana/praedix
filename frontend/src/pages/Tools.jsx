import { useState } from 'react'

const TOOL_CATEGORIES = [
  {
    name: 'Modern Web Recon',
    color: '#a855f7',
    tools: [
      { id: 'subfinder', name: 'Subfinder', desc: 'Discover subdomains for public root domains', template: 'subfinder -d {target} -silent' },
      { id: 'httpx', name: 'httpx', desc: 'Probe live web service, title, status, and tech stack', template: 'httpx -u https://{target} -status-code -title -tech-detect -follow-redirects' },
      { id: 'katana', name: 'Katana', desc: 'Crawl pages, scripts, and endpoints', template: 'katana -u https://{target} -silent -depth 2 -jc' },
      { id: 'ffuf', name: 'ffuf', desc: 'Controlled content discovery with common paths', template: 'ffuf -u https://{target}/FUZZ -w /usr/share/wordlists/dirb/common.txt -mc all -fc 404 -t 20 -rate 50' },
      { id: 'nuclei', name: 'Nuclei', desc: 'Template-based vulnerability checks with rate limiting', template: 'nuclei -u https://{target} -severity low,medium,high,critical -exclude-tags intrusive,dos -rl 10 -no-color' },
    ]
  },
  {
    name: '🔍 Reconnaissance',
    color: '#06b6d4',
    tools: [
      { id: 'dig', name: 'Dig', desc: 'ค้นหา DNS records (A, MX, NS, TXT)', template: 'dig {target} ANY' },
      { id: 'wafw00f', name: 'WAFw00f', desc: 'ตรวจจับ Web Application Firewall', template: 'wafw00f http://{target}' },
      { id: 'traceroute', name: 'Traceroute', desc: 'ติดตามเส้นทาง Network', template: 'traceroute {target}' },
      { id: 'whois', name: 'Whois', desc: 'ข้อมูลจดทะเบียนโดเมน', template: 'whois {target}' },
    ]
  },
  {
    name: '🌐 Web Scanning',
    color: '#f97316',
    tools: [
      { id: 'nikto', name: 'Nikto', desc: 'สแกนช่องโหว่ Web Server', template: 'nikto -h {target} -maxtime 120' },
      { id: 'dirb', name: 'Dirb', desc: 'Brute-force หา Directory ซ่อน', template: 'dirb http://{target} -r' },
      { id: 'curl', name: 'cURL Headers', desc: 'ดู HTTP Response Headers', template: 'curl -I http://{target}' },
      { id: 'curl-body', name: 'cURL Body', desc: 'ดูเนื้อหาหน้าเว็บ', template: 'curl -s http://{target}' },
    ]
  },
  {
    name: '🔒 Network & Crypto',
    color: '#10b981',
    tools: [
      { id: 'nmap-fast', name: 'Nmap Fast', desc: 'สแกนพอร์ตเร็ว (100 พอร์ต)', template: 'nmap -F {target}' },
      { id: 'nmap-version', name: 'Nmap Version', desc: 'ตรวจเวอร์ชัน Service', template: 'nmap -sV {target}' },
      { id: 'nmap-scripts', name: 'Nmap Scripts', desc: 'สแกน HTTP Headers + Enum', template: 'nmap --script http-headers,http-enum {target}' },
      { id: 'sslscan', name: 'SSLScan', desc: 'ตรวจ SSL/TLS (Cipher, ใบรับรอง)', template: 'sslscan {target}' },
    ]
  },
  {
    name: '💉 Exploitation',
    color: '#ef4444',
    tools: [
      { id: 'sqlmap', name: 'SQLMap', desc: 'ทดสอบ SQL Injection อัตโนมัติ', template: 'sqlmap -u "http://{target}/page?id=1" --batch --dbs' },
    ]
  },
]

export default function Tools() {
  const [target, setTarget] = useState('')
  const [activeCommand, setActiveCommand] = useState('')
  const [running, setRunning] = useState(false)
  const [result, setResult] = useState(null)

  const runTool = async (template) => {
    if (!target.trim()) {
      alert('กรุณาใส่ Target ก่อน!')
      return
    }
    const command = template.replace(/\{target\}/g, target.trim())
    setActiveCommand(command)
    setRunning(true)
    setResult(null)

    try {
      // Send directly to scanner via API proxy
      const res = await fetch('/api/tool/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ command })
      })
      const data = await res.json()
      setResult(data)
    } catch (err) {
      setResult({ error: err.message, stdout: '', stderr: '', exit_code: -1 })
    }
    setRunning(false)
  }

  return (
    <div>
      <div className="page-header">
        <h2>Tools</h2>
        <p>เลือกใช้เครื่องมือแต่ละตัวแยก — ทดสอบเฉพาะจุด</p>
      </div>

      {/* Target Input */}
      <div className="scan-panel" style={{ marginBottom: '24px' }}>
        <label style={{ fontSize: '14px', color: 'var(--text-secondary)', marginBottom: '4px', display: 'block' }}>
          Target
        </label>
        <input
          className="scan-input"
          placeholder="e.g. dvwa, example.com, 192.168.1.1"
          value={target}
          onChange={e => setTarget(e.target.value)}
          style={{ maxWidth: '500px' }}
        />
      </div>

      {/* Tool Categories */}
      {TOOL_CATEGORIES.map(cat => (
        <div key={cat.name} style={{ marginBottom: '32px' }}>
          <h3 style={{ color: cat.color, marginBottom: '16px', fontSize: '18px' }}>{cat.name}</h3>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))', gap: '12px' }}>
            {cat.tools.map(tool => (
              <div
                key={tool.id}
                className="kb-card"
                style={{ cursor: 'pointer', borderColor: activeCommand.startsWith(tool.id) ? cat.color : 'var(--border)' }}
                onClick={() => runTool(tool.template)}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                  <div>
                    <div className="title" style={{ color: cat.color, fontSize: '15px' }}>{tool.name}</div>
                    <div className="desc" style={{ marginTop: '4px' }}>{tool.desc}</div>
                  </div>
                  <button
                    className="btn btn-primary"
                    style={{ padding: '6px 14px', fontSize: '12px', flexShrink: 0 }}
                    disabled={running || !target.trim()}
                    onClick={(e) => { e.stopPropagation(); runTool(tool.template) }}
                  >
                    ▶ Run
                  </button>
                </div>
                <div style={{
                  marginTop: '8px',
                  fontFamily: 'var(--font-mono)',
                  fontSize: '11px',
                  color: 'var(--text-muted)',
                  background: 'var(--bg-primary)',
                  padding: '6px 10px',
                  borderRadius: '6px',
                }}>
                  {tool.template.replace(/\{target\}/g, target || '...')}
                </div>
              </div>
            ))}
          </div>
        </div>
      ))}

      {/* Running Indicator */}
      {running && (
        <div className="scan-progress" style={{ borderColor: 'var(--accent)' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
            <span className="spinner"></span>
            <div>
              <div style={{ fontWeight: 600 }}>Running...</div>
              <div style={{ fontFamily: 'var(--font-mono)', fontSize: '13px', color: 'var(--accent)', marginTop: '4px' }}>
                {activeCommand}
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Result Output */}
      {result && !running && (
        <div className="scan-progress">
          <div className="progress-header">
            <div style={{ fontFamily: 'var(--font-mono)', fontSize: '13px', color: 'var(--accent)' }}>
              $ {activeCommand}
            </div>
            <span className={`step-exit ${result.exit_code === 0 ? 'success' : 'error'}`}>
              exit: {result.exit_code}
            </span>
          </div>

          {result.error && (
            <div style={{ color: 'var(--critical)', fontSize: '13px', marginBottom: '12px', padding: '8px 12px', background: 'rgba(239,68,68,0.1)', borderRadius: '6px' }}>
              ⚠️ {result.error}
            </div>
          )}

          <div style={{
            background: '#0a0e17',
            border: '1px solid var(--border)',
            borderRadius: '8px',
            padding: '16px',
            fontFamily: 'var(--font-mono)',
            fontSize: '12px',
            lineHeight: '1.6',
            color: '#a0f0a0',
            whiteSpace: 'pre-wrap',
            maxHeight: '500px',
            overflowY: 'auto',
          }}>
            {result.stdout || result.stderr || 'No output'}
          </div>
        </div>
      )}
    </div>
  )
}
