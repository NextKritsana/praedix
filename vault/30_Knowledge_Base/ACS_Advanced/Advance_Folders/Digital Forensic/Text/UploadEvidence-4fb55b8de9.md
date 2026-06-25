---
title: "UploadEvidence"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic  Copy\\integration-forenchain-frontend-main\\src\\components\\UploadEvidence.jsx"
source_size_bytes: 15843
source_modified: 2025-11-30T14:49:41
imported_at: 2026-06-14T14:25:30
tags:
  - acs
  - acs-advanced
  - imported
---

# UploadEvidence

- Source: [UploadEvidence.jsx](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%20Copy/integration-forenchain-frontend-main/src/components/UploadEvidence.jsx)

## Content

```jsx
// src/components/UploadEvidence.jsx
import React, { useState, useEffect } from 'react';
import { uploadEvidence, getCases, createCase, pollAnalysisCompletion } from '../lib/api';

export default function UploadEvidence() {
  const [file, setFile] = useState(null);
  const [metadata, setMetadata] = useState({
    caseId: '',
    description: '',
  });
  const [cases, setCases] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [analysisProgress, setAnalysisProgress] = useState(null);

  // Fetch existing cases on component mount
  useEffect(() => {
    fetchCases();
  }, []);

  const fetchCases = async () => {
    try {
      const casesData = await getCases();
      setCases(casesData);
    } catch (err) {
      console.error('Failed to fetch cases:', err);
    }
  };

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      // Validate file type
      const ext = selectedFile.name.toLowerCase().split('.').pop();
      if (!['pcap', 'dd'].includes(ext)) {
        setError('Unsupported file type. Only .pcap or .dd files are allowed.');
        setFile(null);
        return;
      }
      setError('');
      setFile(selectedFile);
    }
  };

  const handleMetadataChange = (e) => {
    setMetadata({
      ...metadata,
      [e.target.name]: e.target.value,
    });
  };

  const handleCreateNewCase = async () => {
    try {
      setLoading(true);
      const caseTitle = prompt('Enter case title:');
      const caseDescription = prompt('Enter case description:');
      
      if (caseTitle) {
        const newCase = await createCase({
          title: caseTitle,
          description: caseDescription || ''
        });
        
        setCases(prev => [...prev, newCase]);
        setMetadata(prev => ({ ...prev, caseId: newCase.id }));
        setSuccess(`New case "${caseTitle}" created successfully!`);
      }
    } catch (err) {
      setError(err.message || 'Failed to create case');
    } finally {
      setLoading(false);
    }
  };

  const startAnalysisPolling = async (evidenceId) => {
    try {
      setAnalysisProgress({
        evidenceId,
        status: 'ANALYSIS_IN_PROGRESS',
        message: 'Analysis started...'
      });

      const analysisResults = await pollAnalysisCompletion(evidenceId);
      
      setAnalysisProgress({
        evidenceId,
        status: 'COMPLETED',
        message: 'Analysis completed successfully!',
        results: analysisResults
      });

      setSuccess(`Evidence analysis completed! Check the case details for results.`);

    } catch (err) {
      setAnalysisProgress({
        evidenceId,
        status: 'FAILED',
        message: `Analysis failed: ${err.message}`
      });
      setError(`Analysis failed: ${err.message}`);
    }
  };

 
  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!file) {
      setError('Please select a file to upload');
      return;
    }

    if (!metadata.caseId) {
      setError('Please select or create a case');
      return;
    }

    setLoading(true);
    setError('');
    setSuccess('');
    setAnalysisProgress(null);

    try {
      console.log('Starting evidence upload...');
      console.log('Case ID:', metadata.caseId);
      console.log('File:', file.name);
      
      const result = await uploadEvidence(metadata.caseId, file);
      
      setSuccess(`Evidence uploaded successfully! ${result.message}`);
      
      // Start polling for analysis results if evidence ID is available
      if (result.evidence && result.evidence.id) {
        startAnalysisPolling(result.evidence.id);
      }

      // Reset form (keep case selected)
      setFile(null);
      setMetadata({
        caseId: metadata.caseId,
        description: '',
      });
      document.getElementById('file-upload').value = '';
      
    } catch (err) {
      console.error('Upload error:', err);
      setError(err.message || 'Failed to upload evidence');
    } finally {
      setLoading(false);
    }
  };

  const getAnalysisStatusColor = (status) => {
    const colors = {
      'UPLOADED': 'bg-blue-100 text-blue-800',
      'HASH_CALCULATED': 'bg-purple-100 text-purple-800',
      'BLOCKCHAIN_COMMITTED': 'bg-indigo-100 text-indigo-800',
      'ANALYSIS_IN_PROGRESS': 'bg-yellow-100 text-yellow-800',
      'COMPLETED': 'bg-green-100 text-green-800',
      'FAILED': 'bg-red-100 text-red-800'
    };
    return colors[status] || 'bg-gray-100 text-gray-800';
  };

  return (
    <div className="min-h-screen bg-slate-50">
      <div className="max-w-4xl mx-auto px-4 py-8">
        <div className="bg-white rounded-2xl shadow-lg border border-slate-200 overflow-hidden">
          {/* Page Header */}
          <div className="bg-gradient-to-r from-slate-900 to-slate-700 px-6 py-4">
            <h2 className="text-2xl font-bold text-white">Digital Evidence Upload</h2>
            <p className="text-slate-300 mt-1">
              Upload evidence files for blockchain verification and analysis
            </p>
          </div>

          {/* Status Messages */}
          {error && (
            <div className="mx-6 mt-6 p-4 bg-red-50 border border-red-200 rounded-lg">
              <p className="text-red-700 font-medium">Error: {error}</p>
            </div>
          )}

          {success && (
            <div className="mx-6 mt-6 p-4 bg-green-50 border border-green-200 rounded-lg">
              <p className="text-green-700 font-medium">Success: {success}</p>
            </div>
          )}

          {/* Analysis Progress */}
          {analysisProgress && (
            <div className="mx-6 mt-6 p-4 bg-blue-50 border border-blue-200 rounded-lg">
              <div className="flex items-center justify-between mb-2">
                <h4 className="font-semibold text-blue-900">Analysis Progress</h4>
                <span className={`px-2 py-1 text-xs font-medium rounded-full ${getAnalysisStatusColor(analysisProgress.status)}`}>
                  {analysisProgress.status.replace(/_/g, ' ')}
                </span>
              </div>
              <p className="text-blue-700 text-sm">{analysisProgress.message}</p>
              
              {analysisProgress.status === 'ANALYSIS_IN_PROGRESS' && (
                <div className="mt-2 w-full bg-blue-200 rounded-full h-2">
                  <div className="bg-blue-600 h-2 rounded-full animate-pulse"></div>
                </div>
              )}
              
              {analysisProgress.results && (
                <div className="mt-3 p-3 bg-white rounded border">
                  <h5 className="font-medium text-sm mb-2">Analysis Results:</h5>
                  <pre className="text-xs bg-slate-50 p-2 rounded overflow-auto">
                    {JSON.stringify(analysisProgress.results, null, 2)}
                  </pre>
                </div>
              )}
            </div>
          )}

          <form onSubmit={handleSubmit} className="p-6 space-y-6">
            {/* Case Selection Section - unchanged */}
            <div className="bg-slate-50 rounded-xl p-6 border border-slate-200">
              <h3 className="text-xl font-semibold mb-4 text-slate-900 flex items-center gap-2">
                <span className="text-2xl">📁</span>
                1. Select Case
              </h3>
              
              <div className="space-y-4">
                <div className="flex gap-4 items-start">
                  <div className="flex-1">
                    <label className="text-sm font-medium text-slate-700 mb-2 block">
                      Select Existing Case
                    </label>
                    <select 
                      name="caseId" 
                      value={metadata.caseId} 
                      onChange={handleMetadataChange}
                      required
                      className="w-full p-3 border border-slate-300 rounded-lg bg-white text-slate-900 focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition"
                    >
                      <option value="">Select a case...</option>
                      {cases.map(caseItem => (
                        <option key={caseItem.id} value={caseItem.id}>
                          {caseItem.caseName} ({caseItem.id})
                        </option>
                      ))}
                    </select>
                  </div>
                  
                  <div className="pt-6">
                    <button
                      type="button"
                      onClick={handleCreateNewCase}
                      disabled={loading}
                      className="px-4 py-3 bg-slate-600 text-white rounded-lg hover:bg-slate-700 transition disabled:opacity-50"
                    >
                      + New Case
                    </button>
                  </div>
                </div>
                
                {cases.length === 0 && (
                  <div className="p-4 bg-yellow-50 border border-yellow-200 rounded-lg">
                    <p className="text-yellow-700 text-sm">
                      No cases found. Please create a new case to upload evidence.
                    </p>
                  </div>
                )}
              </div>
            </div>

            {/* File Upload Section - unchanged */}
            <div className="bg-slate-50 rounded-xl p-6 border border-slate-200">
              <h3 className="text-xl font-semibold mb-4 text-slate-900 flex items-center gap-2">
                <span className="text-2xl">📡</span>
                2. Upload Evidence File
              </h3>
              
              <div className="border-2 border-dashed border-slate-300 rounded-lg p-8 text-center bg-white hover:border-slate-400 transition-colors">
                <input 
                  type="file"
                  onChange={handleFileChange}
                  accept=".pcap,.dd"
                  className="hidden"
                  id="file-upload"
                  disabled={loading}
                />
                <label 
                  htmlFor="file-upload"
                  className={`cursor-pointer block ${loading ? 'opacity-50 cursor-not-allowed' : ''}`}
                >
                  <div className="text-4xl mb-3">📁</div>
                  <p className="font-medium text-slate-700 mb-2">
                    {loading ? 'Uploading...' : 'Click to select evidence file'}
                  </p>
                  <p className="text-sm text-slate-500">
                    Supports .pcap (network capture) and .dd (disk image) files
                  </p>
                </label>
                
                {file && (
                  <div className="mt-4 p-3 bg-emerald-50 rounded-lg border border-emerald-200">
                    <p className="font-semibold text-emerald-700 text-sm">
                      ✅ {file.name}
                    </p>
                    <p className="text-xs text-slate-600 mt-1">
                      Size: {(file.size / (1024 * 1024)).toFixed(2)} MB • Type: {file.type || 'Binary file'}
                    </p>
                  </div>
                )}
              </div>
            </div>
            
            {/* Metadata Section - unchanged */}
            <div className="bg-slate-50 rounded-xl p-6 border border-slate-200">
              <h3 className="text-xl font-semibold mb-4 text-slate-900 flex items-center gap-2">
                <span className="text-2xl">📋</span>
                3. Evidence Description
              </h3>
              
              <div className="space-y-2">
                <label className="text-sm font-medium text-slate-700">
                  Evidence Description & Context
                </label>
                <textarea 
                  name="description" 
                  value={metadata.description} 
                  onChange={handleMetadataChange} 
                  required 
                  rows="4" 
                  placeholder="Describe the evidence context: Investigation purpose, acquisition method, relevant timestamps, suspected activities..."
                  className="w-full p-3 border border-slate-300 rounded-lg resize-y text-slate-900 focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition"
                  disabled={loading}
                ></textarea>
              </div>
            </div>

            {/* Enhanced Backend Processing Info */}
            <div className="bg-blue-50 rounded-xl p-6 border border-blue-200">
              <h3 className="text-lg font-semibold mb-3 text-blue-900 flex items-center gap-2">
                <span className="text-xl">⚙️</span>
                Backend Processing Pipeline
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-5 gap-4 text-sm">
                <div className="text-center p-3 bg-white rounded-lg border border-blue-200">
                  <div className="text-blue-600 font-bold">1. File Upload</div>
                  <div className="text-blue-500 text-xs mt-1">Secure Transfer</div>
                </div>
                <div className="text-center p-3 bg-white rounded-lg border border-blue-200">
                  <div className="text-blue-600 font-bold">2. Hash Calculation</div>
                  <div className="text-blue-500 text-xs mt-1">SHA-256 Generation</div>
                </div>
                <div className="text-center p-3 bg-white rounded-lg border border-blue-200">
                  <div className="text-blue-600 font-bold">3. Blockchain</div>
                  <div className="text-blue-500 text-xs mt-1">Transaction Creation</div>
                </div>
                <div className="text-center p-3 bg-white rounded-lg border border-blue-200">
                  <div className="text-blue-600 font-bold">4. Analysis</div>
                  <div className="text-blue-500 text-xs mt-1">Background Processing</div>
                </div>
                <div className="text-center p-3 bg-white rounded-lg border border-blue-200">
                  <div className="text-blue-600 font-bold">5. Results</div>
                  <div className="text-blue-500 text-xs mt-1">Report Generation</div>
                </div>
              </div>
            </div>

            {/* Submit Button */}
            <div className="bg-slate-900 rounded-xl p-6">
              <button 
                type="submit" 
                disabled={!file || !metadata.caseId || loading}
                className={`w-full py-4 px-6 text-lg font-semibold rounded-lg transition-all flex items-center justify-center gap-3
                  ${(!file || !metadata.caseId || loading)
                    ? 'bg-slate-600 cursor-not-allowed text-slate-300' 
                    : 'bg-gradient-to-r from-emerald-600 to-green-600 hover:from-emerald-700 hover:to-green-700 text-white shadow-lg hover:shadow-xl transform hover:scale-[1.02]'
                  }`}
              >
                {loading ? (
                  <>
                    <svg className="animate-spin h-5 w-5 text-white" viewBox="0 0 24 24">
                      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"/>
                      <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"/>
                    </svg>
                    <span>Uploading Evidence...</span>
                  </>
                ) : (
                  <>
                    <span className="text-xl">🚀</span>
                    <span>Upload & Start Analysis</span>
                  </>
                )}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}
```
