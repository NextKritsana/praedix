---
title: "CaseDetail"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic  Copy\\integration-forenchain-frontend-main\\src\\components\\CaseDetail.jsx"
source_size_bytes: 22021
source_modified: 2025-11-30T17:53:40
imported_at: 2026-06-14T14:25:29
tags:
  - acs
  - acs-advanced
  - imported
---

# CaseDetail

- Source: [CaseDetail.jsx](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%20Copy/integration-forenchain-frontend-main/src/components/CaseDetail.jsx)

## Content

```jsx
// src/components/CaseDetail.jsx
import React, { useState, useEffect } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { getCaseDetails, downloadCaseReport, deleteCase, getCaseAnalyses } from '../lib/api';

// Helper function to determine risk color and label
const getRiskStatus = (stats) => {
  if (!stats) return { label: 'UNKNOWN', color: 'bg-gray-50 border-gray-200', icon: '❓', text: 'text-gray-700' };
  
  // Danger (Malicious found)
  if (stats.malicious > 0) {
    return { 
      label: 'MALICIOUS', 
      color: 'bg-red-50 border-red-200', 
      icon: '🚨', 
      text: 'text-red-700' 
    };
  }
  // Warning (Suspicious found)
  if (stats.suspicious > 0) {
    return { 
      label: 'SUSPICIOUS', 
      color: 'bg-orange-50 border-orange-200', 
      icon: '⚠️', 
      text: 'text-orange-700' 
    };
  }
  // Safe (Clean)
  return { 
    label: 'SAFE', 
    color: 'bg-emerald-50 border-emerald-200', 
    icon: '✅', 
    text: 'text-emerald-700' 
  };
};

export default function CaseDetail() {
  const { caseId } = useParams();
  const navigate = useNavigate();
  const [caseDetail, setCaseDetail] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [actionLoading, setActionLoading] = useState({ download: false, delete: false });
  const [analyses, setAnalyses] = useState([]);

  useEffect(() => {
    fetchCaseDetail();
  }, [caseId]);

  const fetchCaseDetail = async () => {
    try {
      setLoading(true);
      setError('');
      const caseData = await getCaseDetails(caseId);
      setCaseDetail(caseData);
      
      // Also fetch detailed analyses
      try {
        const analysesData = await getCaseAnalyses(caseId);
        setAnalyses(analysesData);
      } catch (analysisErr) {
        console.warn('Could not fetch detailed analyses:', analysisErr);
      }
    } catch (err) {
      console.error('Failed to fetch case detail:', err);
      setError(err.message || 'Failed to load case details');
    } finally {
      setLoading(false);
    }
  };

  const handleDownloadReport = async () => {
    if (!caseId) return;
    
    setActionLoading(prev => ({ ...prev, download: true }));
    try {
      const blob = await downloadCaseReport(caseId);
      
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.style.display = 'none';
      a.href = url;
      
      const caseName = caseDetail?.caseName?.replace(/[^a-z0-9]/gi, '_').toLowerCase() || 'case';
      a.download = `ForenChain_Report_Case_${caseName}.json`;
      
      document.body.appendChild(a);
      a.click();
      
      window.URL.revokeObjectURL(url);
      document.body.removeChild(a);
      
    } catch (err) {
      console.error('Failed to download report:', err);
      setError(err.message || 'Failed to download report');
    } finally {
      setActionLoading(prev => ({ ...prev, download: false }));
    }
  };

  const handleDeleteCase = async () => {
    if (!caseId) return;
    
    const confirmed = window.confirm(
      `Are you sure you want to delete case "${caseDetail?.caseName}"? This action cannot be undone.`
    );
    
    if (!confirmed) return;
    
    setActionLoading(prev => ({ ...prev, delete: true }));
    try {
      await deleteCase(caseId);
      alert('Case deleted successfully!');
      navigate('/cases');
    } catch (err) {
      console.error('Failed to delete case:', err);
      setError(err.message || 'Failed to delete case');
      setActionLoading(prev => ({ ...prev, delete: false }));
    }
  };

  const formatDate = (dateString) => {
    if (!dateString) return 'N/A';
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit'
    });
  };

  const getStatusBadge = (status) => {
    const statusConfig = {
      'PENDING': { color: 'bg-yellow-100 text-yellow-800', label: 'Pending' },
      'ANALYSIS_IN_PROGRESS': { color: 'bg-blue-100 text-blue-800', label: 'Analysis in Progress' },
      'COMPLETED': { color: 'bg-green-100 text-green-800', label: 'Completed' },
      'FAILED': { color: 'bg-red-100 text-red-800', label: 'Failed' },
      'UPLOADED': { color: 'bg-blue-100 text-blue-800', label: 'Uploaded' },
      'HASH_CALCULATED': { color: 'bg-purple-100 text-purple-800', label: 'Hash Calculated' },
      'BLOCKCHAIN_COMMITTED': { color: 'bg-indigo-100 text-indigo-800', label: 'Blockchain Committed' }
    };
    
    const config = statusConfig[status] || { color: 'bg-gray-100 text-gray-800', label: status };
    return (
      <span className={`px-3 py-1 text-sm font-medium rounded-full ${config.color}`}>
        {config.label}
      </span>
    );
  };

  const getAnalysisStatusBadge = (status) => {
    const statusConfig = {
      'PENDING': { color: 'bg-yellow-100 text-yellow-800', label: 'Pending' },
      'IN_PROGRESS': { color: 'bg-blue-100 text-blue-800', label: 'In Progress' },
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

  const renderEvidenceDetails = (evidence) => {
    return (
      <div className="space-y-2 text-sm">
        {evidence.fileName && (
          <div className="flex justify-between">
            <span className="text-slate-600">File Name:</span>
            <span className="text-slate-900 font-medium">{evidence.fileName}</span>
          </div>
        )}
        {evidence.fileType && (
          <div className="flex justify-between">
            <span className="text-slate-600">File Type:</span>
            <span className="text-slate-900">{evidence.fileType}</span>
          </div>
        )}
        {evidence.sha256Hash && (
          <div className="flex justify-between">
            <span className="text-slate-600">SHA256 Hash:</span>
            <span className="text-slate-900 font-mono text-xs truncate" title={evidence.sha256Hash}>
              {evidence.sha256Hash.slice(0, 16)}...
            </span>
          </div>
        )}
        {evidence.blockchainTxHash && (
          <div className="flex justify-between">
            <span className="text-slate-600">Blockchain TX:</span>
            <span className="text-slate-900 font-mono text-xs truncate" title={evidence.blockchainTxHash}>
              {evidence.blockchainTxHash.slice(0, 16)}...
            </span>
          </div>
        )}
        {evidence.uploadedAt && (
          <div className="flex justify-between">
            <span className="text-slate-600">Uploaded:</span>
            <span className="text-slate-900">{formatDate(evidence.uploadedAt)}</span>
          </div>
        )}
      </div>
    );
  };

  // --- UPDATED RENDER FUNCTION FOR VIRUSTOTAL UI ---
  const renderAnalysisResults = (analysis) => {
    const isVirusTotal = analysis.source?.includes('VirusTotal');
    
    // Parse result if it's a string
    let resultData = analysis.result;
    if (typeof resultData === 'string') {
      try {
        resultData = JSON.parse(resultData);
      } catch (e) {
        console.error("Error parsing analysis result:", e);
      }
    }

    if (isVirusTotal && resultData) {
      const status = getRiskStatus(resultData);

      return (
        <div className={`mt-2 p-4 rounded-lg border flex flex-col gap-3 ${status.color}`}>
          {/* Header with Icon and IOC */}
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <span className="text-2xl">{status.icon}</span>
              <div>
                <span className={`text-xs font-bold uppercase tracking-wider ${status.text} opacity-75`}>
                   {analysis.analysisType || 'THREAT SCAN'}
                </span>
                <p className="font-mono font-semibold text-slate-800">
                  {/* Show Domain/IP if available in finding or result */}
                  {analysis.finding || 'Unknown Artifact'}
                </p>
              </div>
            </div>
            <div className={`px-3 py-1 rounded-full text-xs font-bold border ${status.color.replace('bg-', 'bg-white ')} ${status.text}`}>
              {status.label}
            </div>
          </div>

          {/* Stats Grid */}
          <div className="grid grid-cols-3 gap-2 mt-2 bg-white/60 p-3 rounded-md">
            <div className="text-center">
              <span className="block font-bold text-xl text-red-600">{resultData.malicious || 0}</span>
              <span className="text-xs text-slate-600 font-medium">Malicious</span>
            </div>
            <div className="text-center border-l border-slate-200">
              <span className="block font-bold text-xl text-orange-500">{resultData.suspicious || 0}</span>
              <span className="text-xs text-slate-600 font-medium">Suspicious</span>
            </div>
            <div className="text-center border-l border-slate-200">
              <span className="block font-bold text-xl text-emerald-600">{resultData.harmless || 0}</span>
              <span className="text-xs text-slate-600 font-medium">Harmless</span>
            </div>
          </div>

          {/* Summary Text */}
          <div className="text-xs text-slate-600 mt-1 px-1">
             <span className="font-semibold">Summary:</span> {analysis.summary || 'Scan completed.'}
          </div>
        </div>
      );
    }

    // Fallback for non-VirusTotal results
    return (
      <div className="p-3 border border-slate-200 rounded-lg bg-slate-50 text-sm text-slate-600">
        {typeof analysis.result === 'string' ? analysis.result : JSON.stringify(analysis.result)}
      </div>
    );
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-50 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-sky-600 mx-auto"></div>
          <p className="text-slate-600 mt-4">Loading case details...</p>
        </div>
      </div>
    );
  }

  if (error && !caseDetail) {
    return (
      <div className="min-h-screen bg-slate-50">
        <div className="max-w-4xl mx-auto px-4 py-8">
          <div className="bg-white rounded-2xl shadow-lg p-6">
            <div className="text-center py-8">
              <div className="text-4xl mb-3">❌</div>
              <h4 className="font-semibold text-slate-900 mb-2">Error Loading Case</h4>
              <p className="text-slate-600 mb-4">{error}</p>
              <div className="flex gap-3 justify-center">
                <button 
                  onClick={() => navigate('/cases')}
                  className="px-4 py-2 bg-slate-600 text-white rounded-lg hover:bg-slate-700 transition-colors"
                >
                  Back to Cases
                </button>
                <button 
                  onClick={fetchCaseDetail}
                  className="px-4 py-2 bg-sky-600 text-white rounded-lg hover:bg-sky-700 transition-colors"
                >
                  Try Again
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }

  if (!caseDetail) {
    return (
      <div className="min-h-screen bg-slate-50">
        <div className="max-w-4xl mx-auto px-4 py-8">
          <div className="bg-white rounded-2xl shadow-lg p-6">
            <div className="text-center py-8">
              <div className="text-4xl mb-3">🔍</div>
              <h4 className="font-semibold text-slate-900 mb-2">Case Not Found</h4>
              <p className="text-slate-600 mb-4">The requested case could not be found.</p>
              <button 
                onClick={() => navigate('/cases')}
                className="px-4 py-2 bg-sky-600 text-white rounded-lg hover:bg-sky-700 transition-colors"
              >
                Back to Cases
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50">
      <div className="max-w-6xl mx-auto px-4 py-8">
        {/* Header */}
        <div className="bg-white rounded-2xl shadow-lg p-6 mb-6">
          <div className="flex items-center justify-between mb-4">
            <div>
              <Link 
                to="/cases" 
                className="inline-flex items-center gap-2 text-sky-600 hover:text-sky-700 mb-2"
              >
                ← Back to Cases
              </Link>
              <h1 className="text-2xl font-bold text-slate-900">{caseDetail.caseName}</h1>
              <p className="text-slate-600 mt-1">Case ID: {caseDetail.id}</p>
            </div>
            <div className="text-right">
              {getStatusBadge(caseDetail.status)}
              <p className="text-sm text-slate-500 mt-2">
                Last updated: {formatDate(caseDetail.updatedAt)}
              </p>
            </div>
          </div>
          
          {caseDetail.description && (
            <div className="bg-slate-50 rounded-lg p-4">
              <h3 className="font-semibold text-slate-900 mb-2">Description</h3>
              <p className="text-slate-700">{caseDetail.description}</p>
            </div>
          )}
        </div>

        {/* Error Message */}
        {error && (
          <div className="mb-6 p-4 bg-red-50 border border-red-200 rounded-lg">
            <p className="text-red-700">{error}</p>
            <button 
              onClick={() => setError('')}
              className="mt-2 px-3 py-1 bg-red-600 text-white text-sm rounded hover:bg-red-700"
            >
              Dismiss
            </button>
          </div>
        )}

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Case Information */}
          <div className="bg-white rounded-2xl shadow-lg p-6">
            <h2 className="text-lg font-semibold text-slate-900 mb-4">Case Information</h2>
            <div className="space-y-3">
              <div className="flex justify-between py-2 border-b border-slate-100">
                <span className="text-slate-600">Created</span>
                <span className="text-slate-900">{formatDate(caseDetail.createdAt)}</span>
              </div>
              <div className="flex justify-between py-2 border-b border-slate-100">
                <span className="text-slate-600">Last Updated</span>
                <span className="text-slate-900">{formatDate(caseDetail.updatedAt)}</span>
              </div>
              <div className="flex justify-between py-2 border-b border-slate-100">
                <span className="text-slate-600">Status</span>
                <span>{getStatusBadge(caseDetail.status)}</span>
              </div>
              {caseDetail.evidence && (
                <div className="flex justify-between py-2 border-b border-slate-100">
                  <span className="text-slate-600">Evidence Files</span>
                  <span className="text-slate-900">{caseDetail.evidence.length}</span>
                </div>
              )}
            </div>
          </div>

          {/* Evidence Records */}
          <div className="bg-white rounded-2xl shadow-lg p-6">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-lg font-semibold text-slate-900">Evidence Records</h2>
              <span className="text-sm text-slate-500">
                {caseDetail.evidence?.length || 0} items
              </span>
            </div>
            
            {!caseDetail.evidence || caseDetail.evidence.length === 0 ? (
              <div className="text-center py-6">
                <div className="text-3xl mb-2">📁</div>
                <p className="text-slate-600">No evidence records found</p>
                <Link 
                  to="/upload" 
                  className="inline-block mt-2 px-4 py-2 bg-sky-600 text-white rounded-lg hover:bg-sky-700 transition-colors text-sm"
                >
                  Upload Evidence
                </Link>
              </div>
            ) : (
              <div className="space-y-4">
                {caseDetail.evidence.map((evidence, index) => (
                  <div key={evidence.id || index} className="border border-slate-200 rounded-lg p-4">
                    <div className="flex items-center justify-between mb-3">
                      <h4 className="font-medium text-slate-900">
                        Evidence {index + 1}
                      </h4>
                      {evidence.status && getAnalysisStatusBadge(evidence.status)}
                    </div>
                    {renderEvidenceDetails(evidence)}
                  </div>
                ))}
              </div>
            )}
          </div>

          {/* Analysis Results (Enhanced UI) */}
          <div className="bg-white rounded-2xl shadow-lg p-6 lg:col-span-2">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-lg font-semibold text-slate-900">Analysis Results</h2>
              <span className="text-sm text-slate-500">
                {analyses.length || caseDetail.analysisResults?.length || 0} results
              </span>
            </div>
            
            {(analyses.length === 0 && (!caseDetail.analysisResults || caseDetail.analysisResults.length === 0)) ? (
              <div className="text-center py-6">
                <div className="text-3xl mb-2">📊</div>
                <p className="text-slate-600">No analysis results available</p>
                {caseDetail.status === 'PENDING' && (
                  <p className="text-sm text-slate-500 mt-1">
                    Analysis will begin soon...
                  </p>
                )}
                {caseDetail.status === 'ANALYSIS_IN_PROGRESS' && (
                  <p className="text-sm text-slate-500 mt-1">
                    Analysis is currently in progress...
                  </p>
                )}
              </div>
            ) : (
              <div className="grid gap-4">
                {/* Show detailed analyses if available */}
                {analyses.length > 0 ? (
                  analyses.map((analysis, index) => (
                    <div key={analysis.id || index} className="w-full">
                       {renderAnalysisResults(analysis)}
                    </div>
                  ))
                ) : (
                  // Fallback for simple results
                  caseDetail.analysisResults?.map((result, index) => (
                     <div key={index}>
                       {renderAnalysisResults({ result, source: 'Unknown' })}
                     </div>
                  ))
                )}
              </div>
            )}
          </div>
        </div>

        {/* Actions */}
        <div className="bg-white rounded-2xl shadow-lg p-6 mt-6">
          <h3 className="text-lg font-semibold text-slate-900 mb-4">Actions</h3>
          <div className="flex gap-3 flex-wrap">
            <button 
              onClick={fetchCaseDetail}
              className="px-4 py-2 bg-slate-100 text-slate-700 rounded-lg hover:bg-slate-200 transition-colors flex items-center gap-2"
            >
              <span>🔄</span>
              <span>Refresh</span>
            </button>
            
            <button 
              onClick={handleDownloadReport}
              disabled={actionLoading.download || caseDetail.status !== 'COMPLETED'}
              className={`px-4 py-2 rounded-lg transition-colors flex items-center gap-2 ${
                actionLoading.download || caseDetail.status !== 'COMPLETED'
                  ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
                  : 'bg-emerald-600 text-white hover:bg-emerald-700'
              }`}
            >
              {actionLoading.download ? (
                <>
                  <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white"></div>
                  <span>Downloading...</span>
                </>
              ) : (
                <>
                  <span>📄</span>
                  <span>Download Report</span>
                </>
              )}
            </button>
            
            <button 
              onClick={handleDeleteCase}
              disabled={actionLoading.delete}
              className={`px-4 py-2 rounded-lg transition-colors flex items-center gap-2 ${
                actionLoading.delete
                  ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
                  : 'bg-red-600 text-white hover:bg-red-700'
              }`}
            >
              {actionLoading.delete ? (
                <>
                  <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white"></div>
                  <span>Deleting...</span>
                </>
              ) : (
                <>
                  <span>🗑️</span>
                  <span>Delete Case</span>
                </>
              )}
            </button>

            <Link 
              to="/upload"
              className="px-4 py-2 bg-sky-600 text-white rounded-lg hover:bg-sky-700 transition-colors flex items-center gap-2"
            >
              <span>📁</span>
              <span>Add More Evidence</span>
            </Link>
          </div>
          
          {caseDetail.status !== 'COMPLETED' && (
            <p className="text-sm text-yellow-600 mt-2">
              Report download is only available for completed cases.
            </p>
          )}
        </div>
      </div>
    </div>
  );
}
```
