---
title: "ViewCases"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic  Copy\\integration-forenchain-frontend-main\\src\\components\\ViewCases.jsx"
source_size_bytes: 8594
source_modified: 2025-11-30T14:49:41
imported_at: 2026-06-14T14:25:30
tags:
  - acs
  - acs-advanced
  - imported
---

# ViewCases

- Source: [ViewCases.jsx](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%20Copy/integration-forenchain-frontend-main/src/components/ViewCases.jsx)

## Content

```jsx
// src/components/ViewCases.jsx
import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { getCases } from '../lib/api';

export default function ViewCases() {
  const [cases, setCases] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchCases();
  }, []);

  const fetchCases = async () => {
    try {
      setLoading(true);
      setError('');
      const casesData = await getCases();
      setCases(casesData);
    } catch (err) {
      console.error('Failed to fetch cases:', err);
      setError('Failed to load case history');
    } finally {
      setLoading(false);
    }
  };

  const formatDate = (dateString) => {
    if (!dateString) return 'N/A';
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const getStatusBadge = (status) => {
    const statusConfig = {
      'PENDING': { color: 'bg-yellow-100 text-yellow-800', label: 'Pending' },
      'ANALYSIS_IN_PROGRESS': { color: 'bg-blue-100 text-blue-800', label: 'Analysis in Progress' },
      'COMPLETED': { color: 'bg-green-100 text-green-800', label: 'Completed' },
      'FAILED': { color: 'bg-red-100 text-red-800', label: 'Failed' }
    };
    
    const config = statusConfig[status] || { color: 'bg-gray-100 text-gray-800', label: status };
    return (
      <span className={`px-2 py-1 text-xs font-medium rounded-full ${config.color}`}>
        {config.label}
      </span>
    );
  };

  return (
    <div className="min-h-screen bg-slate-50">
      <div className="max-w-6xl mx-auto px-4 py-8">
        {/* Page Header */}
        <div className="bg-white rounded-2xl shadow-lg p-6 mb-6">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-2xl font-bold text-slate-900 mb-2">Case History</h1>
              <p className="text-slate-600">
                Manage and monitor all your digital forensics investigations
              </p>
            </div>
            <Link 
              to="/upload" 
              className="inline-flex items-center gap-2 px-4 py-2 bg-sky-600 text-white rounded-lg hover:bg-sky-700 transition-colors"
            >
              <span>+ New Evidence</span>
            </Link>
          </div>
        </div>

        {/* Statistics Cards */}
        {cases.length > 0 && (
          <div className="mb-6 grid grid-cols-2 md:grid-cols-4 gap-4">
            <div className="bg-white rounded-xl p-4 shadow border border-slate-200 text-center">
              <div className="text-2xl font-bold text-slate-900">{cases.length}</div>
              <div className="text-sm text-slate-600">Total Cases</div>
            </div>
            <div className="bg-white rounded-xl p-4 shadow border border-slate-200 text-center">
              <div className="text-2xl font-bold text-yellow-600">
                {cases.filter(c => c.status === 'PENDING').length}
              </div>
              <div className="text-sm text-slate-600">Pending</div>
            </div>
            <div className="bg-white rounded-xl p-4 shadow border border-slate-200 text-center">
              <div className="text-2xl font-bold text-blue-600">
                {cases.filter(c => c.status === 'ANALYSIS_IN_PROGRESS').length}
              </div>
              <div className="text-sm text-slate-600">In Progress</div>
            </div>
            <div className="bg-white rounded-xl p-4 shadow border border-slate-200 text-center">
              <div className="text-2xl font-bold text-green-600">
                {cases.filter(c => c.status === 'COMPLETED').length}
              </div>
              <div className="text-sm text-slate-600">Completed</div>
            </div>
          </div>
        )}

        {/* Cases List */}
        <div className="bg-white rounded-2xl shadow-lg p-6">
          <div className="flex items-center justify-between mb-6">
            <h3 className="font-semibold text-slate-900 text-lg">All Cases</h3>
            <div className="flex items-center gap-4">
              <div className="text-sm text-slate-500">
                {cases.length} {cases.length === 1 ? 'case' : 'cases'} total
              </div>
              <button 
                onClick={fetchCases}
                disabled={loading}
                className="flex items-center gap-2 px-3 py-1 bg-slate-100 text-slate-700 rounded-lg hover:bg-slate-200 transition-colors text-sm"
              >
                <span>🔄</span>
                <span>Refresh</span>
              </button>
            </div>
          </div>

          {error && (
            <div className="mb-4 p-4 bg-red-50 border border-red-200 rounded-lg">
              <p className="text-red-700">{error}</p>
              <button 
                onClick={fetchCases}
                className="mt-2 px-3 py-1 bg-red-600 text-white text-sm rounded hover:bg-red-700"
              >
                Try Again
              </button>
            </div>
          )}

          {loading ? (
            <div className="text-center py-8">
              <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-sky-600 mx-auto"></div>
              <p className="text-slate-600 mt-2">Loading cases...</p>
            </div>
          ) : cases.length === 0 ? (
            <div className="text-center py-8">
              <div className="text-4xl mb-3">📂</div>
              <h4 className="font-semibold text-slate-900 mb-2">No cases yet</h4>
              <p className="text-slate-600 mb-4">Get started by uploading your first evidence file.</p>
              <Link 
                to="/upload" 
                className="inline-flex items-center gap-2 px-4 py-2 bg-sky-600 text-white rounded-lg hover:bg-sky-700 transition-colors"
              >
                <span>Upload Evidence</span>
              </Link>
            </div>
          ) : (
            <div className="space-y-4">
              {cases.map((caseItem) => (
                <div 
                  key={caseItem.id} 
                  className="border border-slate-200 rounded-lg p-4 hover:border-slate-300 transition-colors"
                >
                  <div className="flex items-start justify-between mb-2">
                    <div className="flex-1">
                      <h4 className="font-semibold text-slate-900 text-lg mb-1">
                        {caseItem.caseName || 'Unnamed Case'}
                      </h4>
                      <p className="text-slate-600 text-sm mb-2">
                        {caseItem.description || 'No description provided'}
                      </p>
                    </div>
                    <div className="flex items-center gap-2">
                      {getStatusBadge(caseItem.status)}
                    </div>
                  </div>
                  
                  <div className="flex items-center justify-between text-sm text-slate-500">
                    <div className="flex items-center gap-4 flex-wrap">
                      <span>ID: {caseItem.id}</span>
                      {caseItem.createable && (
                        <span>Created: {formatDate(caseItem.createable)}</span>
                      )}
                      {caseItem.updatedAt && caseItem.updatedAt !== caseItem.createable && (
                        <span>Updated: {formatDate(caseItem.updatedAt)}</span>
                      )}
                      {/* Evidence count */}
                      <span>Evidence: {caseItem.evidence?.length || 0}</span>
                      {/* Analysis results count */}
                      <span>Results: {caseItem.analysisResults?.length || 0}</span>
                    </div>
                    <div className="flex gap-2">
                      <Link 
                        to={`/cases/${caseItem.id}`}
                        className="text-sky-600 hover:text-sky-700 font-medium"
                      >
                        View Details
                      </Link>
                      {caseItem.status === 'COMPLETED' && (
                        <button className="text-emerald-600 hover:text-emerald-700 font-medium">
                          Download Report
                        </button>
                      )}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
```
