import { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'

export default function ReportView() {
  const { filename } = useParams()
  const [content, setContent] = useState('')
  const navigate = useNavigate()

  useEffect(() => {
    fetch(`/api/reports/${filename}`)
      .then(r => r.json())
      .then(data => setContent(data.content || ''))
      .catch(() => setContent('Failed to load report.'))
  }, [filename])

  // Simple markdown to HTML conversion
  const renderMarkdown = (md) => {
    let html = md
      .replace(/^### (.*$)/gm, '<h3>$1</h3>')
      .replace(/^## (.*$)/gm, '<h2>$1</h2>')
      .replace(/^# (.*$)/gm, '<h1>$1</h1>')
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.*?)\*/g, '<em>$1</em>')
      .replace(/`([^`]+)`/g, '<code>$1</code>')
      .replace(/^- (.*$)/gm, '<li>$1</li>')
      .replace(/^---$/gm, '<hr />')
      .replace(/\n\n/g, '<br /><br />')

    // Handle code blocks
    html = html.replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>')

    return html
  }

  return (
    <div>
      <div className="page-header">
        <button
          onClick={() => navigate('/reports')}
          style={{ background: 'none', border: '1px solid var(--border)', color: 'var(--text-secondary)', padding: '8px 16px', borderRadius: '8px', cursor: 'pointer', marginBottom: '16px', fontSize: '13px' }}
        >
          ← Back to Reports
        </button>
        <h2>📄 {filename}</h2>
      </div>

      <div className="report-content" dangerouslySetInnerHTML={{ __html: renderMarkdown(content) }} />
    </div>
  )
}
