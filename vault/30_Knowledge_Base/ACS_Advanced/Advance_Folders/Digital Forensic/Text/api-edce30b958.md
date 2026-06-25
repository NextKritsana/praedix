---
title: "api"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic  Copy\\integration-forenchain-frontend-main\\src\\lib\\api.js"
source_size_bytes: 13775
source_modified: 2025-11-30T16:10:12
imported_at: 2026-06-14T14:25:30
tags:
  - acs
  - acs-advanced
  - imported
---

# api

- Source: [api.js](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%20Copy/integration-forenchain-frontend-main/src/lib/api.js)

## Content

```js
// src/lib/api.js

export const API_BASE_URL = 'http://localhost:8000';

// Enhanced fetch wrapper with better error handling
const apiFetch = async (endpoint, options = {}) => {
  const url = `${API_BASE_URL}${endpoint}`;
  
  try {
    console.log(`🔄 API Call: ${options.method || 'GET'} ${url}`);
    
    const response = await fetch(url, {
      ...options,
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
    });

    console.log(`📡 Response: ${response.status} ${response.statusText}`);

    if (!response.ok) {
      let errorMessage = `HTTP Error: ${response.status} ${response.statusText}`;
      
      try {
        const errorText = await response.text();
        console.error('Error response text:', errorText);
        
        if (errorText) {
          const errorData = JSON.parse(errorText);
          errorMessage = errorData.detail || errorData.message || errorText;
        }
      } catch (parseError) {
        console.error('Error parsing error response:', parseError);
      }
      
      throw new Error(errorMessage);
    }

    // For empty responses
    if (response.status === 204) {
      return null;
    }

    const data = await response.json();
    console.log('✅ API Success:', data);
    return data;

  } catch (error) {
    console.error('❌ API Error:', error.message);
    
    // Enhanced error messages
    if (error.name === 'TypeError' && error.message.includes('fetch')) {
      throw new Error('Cannot connect to server. Please check if the backend is running.');
    }
    
    throw error;
  }
};

// Auth API functions
export const signupRequest = async (userData) => {
  return apiFetch('/api/auth/register', {
    method: 'POST',
    body: JSON.stringify({
      username: userData.username,
      password: userData.password
    }),
  });
};

export const loginRequest = async (credentials) => {
  return apiFetch('/api/auth/login', {
    method: 'POST',
    body: JSON.stringify({
      username: credentials.username,
      password: credentials.password
    }),
  });
};

// Cases API functions
// In your api.js - update the createCase function
// In api.js - update the createCase function
export const createCase = async (caseData) => {
  const url = `${API_BASE_URL}/api/cases`;
  
  try {
    // Transform the data to match backend schema
    const backendCaseData = {
      caseName: caseData.title,  // Map 'title' to 'caseName'
      description: caseData.description
    };
    
    console.log('🔄 Creating case with transformed data:', backendCaseData);
    
    const response = await fetch(url, {
      method: 'POST',
      headers: getAuthHeaders(),
      body: JSON.stringify(backendCaseData),
    });

    console.log('📡 Response status:', response.status);

    // In the same createCase function, improve the 422 error handling
    if (response.status === 422) {
      const errorText = await response.text();
      console.error('Validation error details:', errorText);
      
      try {
        const errorData = JSON.parse(errorText);
        // Extract the specific validation error message
        if (Array.isArray(errorData.detail)) {
          const firstError = errorData.detail[0];
          throw new Error(`Validation error: ${firstError.msg} (field: ${firstError.loc.join('.')})`);
        } else {
          throw new Error(`Validation error: ${errorData.detail}`);
        }
      } catch (parseError) {
        throw new Error('Invalid data format. Please check your input.');
      }
    }

    if (!response.ok) {
      const errorText = await response.text();
      let errorMessage = `Failed to create case: ${response.status}`;
      
      try {
        const errorData = JSON.parse(errorText);
        errorMessage = errorData.detail || errorMessage;
      } catch {
        errorMessage = errorText || errorMessage;
      }
      
      throw new Error(errorMessage);
    }

    const data = await response.json();
    console.log('✅ Case created successfully:', data);
    return data;

  } catch (error) {
    console.error('❌ Create case failed:', error);
    throw error;
  }
};

export const getCases = async () => {
  return apiFetch('/api/cases', {
    method: 'GET',
    headers: getAuthHeaders(),
  });
};

export const getCaseDetails = async (caseId) => {
  return apiFetch(`/api/cases/${caseId}`, {
    method: 'GET',
    headers: getAuthHeaders(),
  });
};

// Evidence API functions
export const uploadEvidence = async (caseId, file) => {
  const url = `${API_BASE_URL}/api/cases/${caseId}/upload`;
  
  try {
    console.log(`🔄 Uploading evidence to case: ${caseId}`);
    console.log(`📁 File: ${file.name} (${(file.size / (1024 * 1024)).toFixed(2)} MB)`);
    
    const formData = new FormData();
    formData.append('evidenceFile', file);

    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${getToken()}`,
      },
      body: formData,
    });

    console.log(`📡 Upload Response Status: ${response.status} ${response.statusText}`);

    if (!response.ok) {
      let errorMessage = `Upload failed: ${response.status} ${response.statusText}`;
      
      try {
        const errorText = await response.text();
        console.error('Upload error response text:', errorText);
        
        if (errorText) {
          try {
            const errorData = JSON.parse(errorText);
            errorMessage = errorData.detail || errorData.message || errorText;
          } catch {
            errorMessage = errorText;
          }
        }
      } catch (parseError) {
        console.error('Error parsing upload error response:', parseError);
      }
      
      throw new Error(errorMessage);
    }

    const data = await response.json();
    console.log('✅ Evidence upload successful:', data);
    
    // Handle the backend response structure
    if (data.evidence) {
      return {
        evidence: {
          id: data.evidence.id,
          fileName: data.evidence.fileName,
          fileType: data.evidence.fileType,
          sha256Hash: data.evidence.sha256Hash, // Updated field name
          blockchainTxHash: data.evidence.blockchainTxHash, // Updated field name
          uploadedAt: data.evidence.uploadedAt
        },
        message: data.message
      };
    }
    
    return data;

  } catch (error) {
    console.error('❌ Evidence upload error:', error);
    throw error;
  }
};

export const getEvidenceStatus = async (evidenceId) => {
  return apiFetch(`/api/evidence/${evidenceId}/status`, {
    method: 'GET',
    headers: getAuthHeaders(),
  });
};

// Report API functions
// In src/lib/api.js - update the downloadCaseReport function
export const downloadCaseReport = async (caseId) => {
  const url = `${API_BASE_URL}/api/cases/${caseId}/report`;
  
  try {
    console.log(`📥 Downloading JSON report for case: ${caseId}`);
    
    const response = await fetch(url, {
      method: 'GET',
      headers: getAuthHeaders(),
    });

    if (!response.ok) {
      if (response.status === 404) {
        throw new Error('Case not found');
      }
      const errorData = await response.json();
      throw new Error(errorData.detail || errorData.message || 'Failed to download report');
    }

    // For JSON response, we'll create a blob and download as JSON file
    const data = await response.json();
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    
    console.log('✅ JSON report download successful');
    return blob;
  } catch (error) {
    console.error('❌ Report download error:', error);
    throw error;
  }
};

// Analysis API functions
export const getAnalysisResults = async (evidenceId) => {
  return apiFetch(`/api/evidence/${evidenceId}/analysis`, {
    method: 'GET',
    headers: getAuthHeaders(),
  });
};

export const getCaseAnalyses = async (caseId) => {
  return apiFetch(`/api/cases/${caseId}/analyses`, {
    method: 'GET',
    headers: getAuthHeaders(),
  });
};



// Health check with detailed logging
export const healthCheck = async () => {
  console.log('🏥 Checking backend health...');
  try {
    const response = await fetch(`${API_BASE_URL}/healthz`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });
    
    console.log('Health check status:', response.status);
    
    if (!response.ok) {
      throw new Error(`Backend returned ${response.status}`);
    }
    
    const data = await response.json();
    console.log('Backend health:', data);
    return data;
  } catch (error) {
    console.error('Health check failed:', error);
    throw new Error(`Cannot connect to backend at ${API_BASE_URL}. Make sure the server is running.`);
  }
};

// Utility functions
export const getToken = () => {
  return localStorage.getItem('auth_token');
};

export const getAuthHeaders = () => {
  const token = getToken();
  const headers = {
    'Content-Type': 'application/json',
  };
  
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }
  
  return headers;
};

export const getCurrentUser = () => {
  const userStr = localStorage.getItem('auth_user');
  if (userStr) {
    try {
      return JSON.parse(userStr);
    } catch (error) {
      console.error('Error parsing user data:', error);
      return null;
    }
  }
  return null;
};

export const isAuthenticated = () => {
  return !!getToken();
};

export const logout = () => {
  localStorage.removeItem('auth_token');
  localStorage.removeItem('auth_user');
  window.location.href = '/login';
};

// File validation helper
export const validateEvidenceFile = (file) => {
  const allowedTypes = ['.pcap', '.dd'];
  const fileExtension = file.name.toLowerCase().split('.').pop();
  
  if (!allowedTypes.includes(fileExtension)) {
    throw new Error(`Unsupported file type. Only ${allowedTypes.join(', ')} files are allowed.`);
  }
  
  // Check file size (e.g., 100MB limit)
  const maxSize = 100 * 1024 * 1024; // 100MB in bytes
  if (file.size > maxSize) {
    throw new Error(`File size too large. Maximum allowed size is 100MB.`);
  }
  
  return true;
};

// Case management helpers
export const generateCaseId = () => {
  return `INV-${new Date().getFullYear()}-${Math.random().toString(36).substr(2, 6).toUpperCase()}`;
};

// Evidence status constants
export const EvidenceStatus = {
  UPLOADED: 'uploaded',
  HASH_CALCULATED: 'hash_calculated',
  BLOCKCHAIN_COMMITTED: 'blockchain_committed',
  ANALYSIS_IN_PROGRESS: 'analysis_in_progress',
  ANALYSIS_COMPLETED: 'analysis_completed',
  ERROR: 'error'
};

// Case status constants
export const CaseStatus = {
  CREATED: 'created',
  EVIDENCE_UPLOADED: 'evidence_uploaded',
  ANALYSIS_IN_PROGRESS: 'analysis_in_progress',
  ANALYSIS_COMPLETED: 'analysis_completed',
  REPORT_GENERATED: 'report_generated'
};

export const deleteCase = async (caseId) => {
  return apiFetch(`/api/cases/${caseId}`, {
    method: 'DELETE',
    headers: getAuthHeaders(),
  });
};

// Add this function to your src/lib/api.js file

export const pollAnalysisCompletion = async (evidenceId, maxAttempts = 30, interval = 2000) => {
  console.log(`🔄 Starting analysis polling for evidence: ${evidenceId}`);
  
  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    try {
      console.log(`📊 Polling attempt ${attempt}/${maxAttempts} for evidence ${evidenceId}`);
      
      const status = await getEvidenceStatus(evidenceId);
      console.log(`📈 Evidence status:`, status);
      
      // Check if analysis is complete
      if (status.status === 'COMPLETED' || status.status === 'FAILED') {
        console.log(`✅ Analysis finished with status: ${status.status}`);
        
        // If completed, try to get detailed analysis results
        if (status.status === 'COMPLETED') {
          try {
            const analysisResults = await getAnalysisResults(evidenceId);
            return analysisResults;
          } catch (analysisError) {
            console.warn('Could not fetch detailed analysis results:', analysisError);
            return status; // Return status if analysis results aren't available
          }
        }
        
        return status;
      }
      
      // If not complete, wait before next attempt
      if (attempt < maxAttempts) {
        console.log(`⏳ Waiting ${interval}ms before next poll...`);
        await new Promise(resolve => setTimeout(resolve, interval));
      }
      
    } catch (error) {
      console.error(`❌ Polling attempt ${attempt} failed:`, error);
      
      // On last attempt, throw the error
      if (attempt === maxAttempts) {
        throw new Error(`Analysis polling failed after ${maxAttempts} attempts: ${error.message}`);
      }
      
      // Wait before retrying on error
      await new Promise(resolve => setTimeout(resolve, interval));
    }
  }
  
  throw new Error(`Analysis did not complete within ${maxAttempts * interval / 1000} seconds`);
};

// Add to your api.js
export const analyzeFileHash = async (fileHash) => {
  return apiFetch('/api/analyze/hash', {
    method: 'POST',
    headers: getAuthHeaders(),
    body: JSON.stringify({ file_hash: fileHash }),
  });
};

export const analyzeDomain = async (domain) => {
  return apiFetch('/api/analyze/domain', {
    method: 'POST',
    headers: getAuthHeaders(),
    body: JSON.stringify({ domain: domain }),
  });
};

export const analyzeIPAddress = async (ipAddress) => {
  return apiFetch('/api/analyze/ip', {
    method: 'POST',
    headers: getAuthHeaders(),
    body: JSON.stringify({ ip_address: ipAddress }),
  });
};



// API interceptor for automatic token refresh can be added here if needed

// Export for testing
export const API_BASE = API_BASE_URL;
```
