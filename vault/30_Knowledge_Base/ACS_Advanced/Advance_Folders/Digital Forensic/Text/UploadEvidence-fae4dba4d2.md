---
title: "UploadEvidence"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic (backend)\\frontend-forenchain\\src\\components\\UploadEvidence.jsx"
source_size_bytes: 16189
source_modified: 2025-11-30T12:58:19
imported_at: 2026-06-14T14:25:35
tags:
  - acs
  - acs-advanced
  - imported
---

# UploadEvidence

- Source: [UploadEvidence.jsx](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%28backend%29/frontend-forenchain/src/components/UploadEvidence.jsx)

## Content

```jsx
// src/components/UploadEvidence.jsx
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

export default function UploadEvidence() {
  const [file, setFile] = useState(null);
  const [metadata, setMetadata] = useState({
    caseId: `INV-${new Date().getFullYear()}-${Math.random().toString().substr(2, 3)}`,
    description: '',
  });

  // Get user info from localStorage
  const user = JSON.parse(localStorage.getItem("auth_user") || "{}");

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
    }
  };

  const handleMetadataChange = (e) => {
    setMetadata({
      ...metadata,
      [e.target.name]: e.target.value,
    });
  };

 const handleSubmit = async (e) => { // เพิ่ม async
    e.preventDefault();
    
    if (!file) {
      alert("กรุณาเลือกไฟล์ก่อนครับ");
      return;
    }

    try {
      // 1. เตรียมข้อมูลใส่ซอง (FormData)
      const formData = new FormData();
      formData.append('evidenceFile', file); // ชื่อ 'evidenceFile' ต้องตรงกับ Backend เป๊ะๆ

      // 2. ดึง URL จาก .env
      const API_URL = import.meta.env.VITE_API_BASE_URL; 
      // หรือถ้าไม่ได้ config .env ให้ใช้ 'http://127.0.0.1:8000' ตรงๆ

      // 3. ส่งไปที่ Backend (POST /api/cases/{caseId}/upload)
      // ใช้ metadata.caseId ที่เจนมาจาก state
      const response = await axios.post(
        `${API_URL}/api/cases/${metadata.caseId}/upload`, 
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data',
            'Authorization': `Bearer ${localStorage.getItem("auth_token")}` // ส่ง Token ไปด้วย
          }
        }
      );

      // 4. ถ้าสำเร็จ
      console.log("Upload Success:", response.data);
      alert(`✅ Upload successful! \nBackend ตอบว่า: ${response.data.message}`);
      
      // (Optional) อาจจะเคลียร์ฟอร์ม หรือ Redirect ไปหน้า Dashboard
      // window.location.href = "/dashboard";

    } catch (error) {
      console.error("Upload Failed:", error);
      // เช็คว่า Error มาจาก Backend หรือเปล่า
      const errorMsg = error.response?.data?.detail || "เชื่อมต่อ Backend ไม่ได้";
      alert(`❌ เกิดข้อผิดพลาด: ${errorMsg}`);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem("auth_token");
    localStorage.removeItem("auth_user");
    window.location.href = "/login";
  };

  return (
    <div className="min-h-screen bg-slate-50">
      {/* Header with user info */}
      <header className="bg-white border-b border-slate-200">
        <div className="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <span className="grid h-8 w-8 place-items-center rounded-lg bg-gradient-to-tr from-sky-500 to-violet-500 text-white text-sm font-bold">
              FC
            </span>
            <h1 className="text-xl font-bold text-slate-900">ForenChain</h1>
          </div>
          
          <div className="flex items-center gap-4">
            <div className="text-right">
              <p className="text-sm font-medium text-slate-900">
                {user.firstName} {user.lastName}
              </p>
              <p className="text-xs text-slate-500">{user.email}</p>
            </div>
            <div className="flex gap-2">
              <Link 
                to="/dashboard" 
                className="px-3 py-1 text-sm text-slate-700 hover:bg-slate-100 rounded-md transition"
              >
                Dashboard
              </Link>
              <button
                onClick={handleLogout}
                className="px-3 py-1 text-sm text-slate-700 hover:bg-slate-100 rounded-md transition"
              >
                Logout
              </button>
            </div>
          </div>
        </div>
      </header>
      
      {/* Main Content */}
      <div className="max-w-4xl mx-auto px-4 py-8">
        <div className="bg-white rounded-2xl shadow-lg border border-slate-200 overflow-hidden">
          {/* Header */}
          <div className="bg-gradient-to-r from-slate-900 to-slate-700 px-6 py-4">
            <h2 className="text-2xl font-bold text-white">Digital Evidence Upload</h2>
            <p className="text-slate-300 mt-1">
              Upload evidence files for blockchain verification (Backend Integration Ready)
            </p>
          </div>

          <form onSubmit={handleSubmit} className="p-6 space-y-6">
            
            {/* File Upload Section */}
            <div className="bg-slate-50 rounded-xl p-6 border border-slate-200">
              <h3 className="text-xl font-semibold mb-4 text-slate-900 flex items-center gap-2">
                <span className="text-2xl">📁</span>
                1. Upload Evidence File
              </h3>
              
              <div className="border-2 border-dashed border-slate-300 rounded-lg p-8 text-center bg-white hover:border-slate-400 transition-colors">
                <input 
                  type="file"
                  onChange={handleFileChange}
                  accept=".pcap,.pcapng,.dd,.img,.e01,.ad1"
                  className="hidden"
                  id="file-upload"
                />
                <label 
                  htmlFor="file-upload"
                  className="cursor-pointer block"
                >
                  <div className="text-4xl mb-3">📡</div>
                  <p className="font-medium text-slate-700 mb-2">
                    Click to select evidence file
                  </p>
                  <p className="text-sm text-slate-500">
                    Supports .pcap, .pcapng, .dd, .img, .e01, .ad1 files
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

              {/* Backend Integration Note */}
              <div className="mt-4 p-4 bg-blue-50 border border-blue-200 rounded-lg">
                <h4 className="font-semibold text-blue-900 text-sm mb-2">Backend Integration Required:</h4>
                <ul className="text-xs text-blue-700 space-y-1">
                  <li>• File validation and type checking</li>
                  <li>• Secure file storage solution</li>
                  <li>• File size limits and processing</li>
                </ul>
              </div>
            </div>

            {/* Hash Calculation Section - Placeholder for Backend */}
            <div className="bg-slate-50 rounded-xl p-6 border border-slate-200">
              <h3 className="text-xl font-semibold mb-4 text-slate-900 flex items-center gap-2">
                <span className="text-2xl">🔐</span>
                2. Hash Verification (Backend)
              </h3>

              <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-6 text-center">
                <div className="text-3xl mb-3">⚙️</div>
                <h4 className="font-semibold text-yellow-800 mb-2">Backend Processing Required</h4>
                <p className="text-yellow-700 text-sm">
                  Hash calculation will be handled by the backend system
                </p>
                <div className="mt-3 text-xs text-yellow-600 space-y-1">
                  <p>• Cryptographic hash generation (SHA-256, MD5, etc.)</p>
                  <p>• Hash verification and validation</p>
                  <p>• Progress tracking for large files</p>
                </div>
              </div>
            </div>
            
            {/* Metadata Section */}
            <div className="bg-slate-50 rounded-xl p-6 border border-slate-200">
              <h3 className="text-xl font-semibold mb-4 text-slate-900 flex items-center gap-2">
                <span className="text-2xl">📋</span>
                3. Case Metadata
              </h3>
              
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="space-y-2">
                  <label className="text-sm font-medium text-slate-700">Case ID</label>
                  <input 
                    type="text" 
                    name="caseId" 
                    value={metadata.caseId} 
                    onChange={handleMetadataChange}
                    className="w-full p-3 border border-slate-300 rounded-lg bg-white text-slate-900 focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition"
                  />
                </div>
                
                <div className="space-y-2">
                  <label className="text-sm font-medium text-slate-700">Examiner</label>
                  <input 
                    type="text" 
                    value={`${user.firstName} ${user.lastName}`} 
                    readOnly
                    className="w-full p-3 border border-slate-300 rounded-lg bg-slate-100 text-slate-600 cursor-not-allowed"
                  />
                </div>
              </div>

              <div className="space-y-2 mt-4">
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
                ></textarea>
              </div>
            </div>

            {/* Blockchain Integration - Placeholder for Backend */}
            <div className="bg-slate-50 rounded-xl p-6 border border-slate-200">
              <h3 className="text-xl font-semibold mb-4 text-slate-900 flex items-center gap-2">
                <span className="text-2xl">⛓️</span>
                4. Blockchain Integration (Backend)
              </h3>

              <div className="bg-purple-50 border border-purple-200 rounded-lg p-6 text-center">
                <div className="text-3xl mb-3">🔗</div>
                <h4 className="font-semibold text-purple-800 mb-2">Blockchain Services Required</h4>
                <p className="text-purple-700 text-sm">
                  Smart contract interaction and transaction management
                </p>
                <div className="mt-3 text-xs text-purple-600 space-y-1">
                  <p>• Sepolia testnet transaction creation</p>
                  <p>• Gas fee estimation and management</p>
                  <p>• Smart contract method calls</p>
                  <p>• Transaction confirmation and status tracking</p>
                </div>
              </div>
            </div>

            {/* Submit Button */}
            <div className="bg-slate-900 rounded-xl p-6">
              <button 
                type="submit" 
                disabled={!file}
                className={`
                  w-full py-4 px-6 text-lg font-semibold rounded-lg transition-all flex items-center justify-center gap-3
                  ${!file
                    ? 'bg-slate-600 cursor-not-allowed text-slate-300' 
                    : 'bg-gradient-to-r from-emerald-600 to-green-600 hover:from-emerald-700 hover:to-green-700 text-white shadow-lg hover:shadow-xl transform hover:scale-[1.02]'
                  }
                `}
              >
                <span className="text-xl">🚀</span>
                <span>Ready for Backend Integration</span>
              </button>
              
              <div className="mt-4 p-4 bg-slate-800 rounded-lg">
                <h4 className="text-white font-semibold text-sm mb-2">Backend Integration Data:</h4>
                <div className="text-slate-300 text-xs space-y-1 font-mono">
                  <p>File: {file ? file.name : 'No file selected'}</p>
                  <p>Case ID: {metadata.caseId}</p>
                  <p>User: {user.email}</p>
                  <p>Description: {metadata.description || 'Not provided'}</p>
                </div>
              </div>
            </div>
          </form>
        </div>

        {/* Backend Integration Guide */}
        <div className="mt-8 bg-white rounded-2xl shadow-lg border border-slate-200 p-6">
          <h3 className="text-xl font-bold text-slate-900 mb-4">Backend Integration Guide</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-4">
              <div className="p-4 bg-slate-50 rounded-lg">
                <h4 className="font-semibold text-slate-900 mb-2">Required Endpoints</h4>
                <ul className="text-sm text-slate-600 space-y-1">
                  <li>• POST /api/evidence/upload</li>
                  <li>• POST /api/evidence/calculate-hash</li>
                  <li>• POST /api/blockchain/commit</li>
                  <li>• GET /api/evidence/{'{id}'}/status</li>
                </ul>
              </div>
              
              <div className="p-4 bg-slate-50 rounded-lg">
                <h4 className="font-semibold text-slate-900 mb-2">Expected Payload</h4>
                <pre className="text-xs bg-slate-900 text-green-400 p-3 rounded overflow-x-auto">
{`{
  "file": File,
  "caseId": "string",
  "description": "string",
  "userId": "string",
  "examinerId": "string"
}`}
                </pre>
              </div>
            </div>
            
            <div className="space-y-4">
              <div className="p-4 bg-slate-50 rounded-lg">
                <h4 className="font-semibold text-slate-900 mb-2">Integration Points</h4>
                <ul className="text-sm text-slate-600 space-y-2">
                  <li>• File upload and storage service</li>
                  <li>• Hash calculation service</li>
                  <li>• Blockchain wallet integration</li>
                  <li>• Smart contract interaction</li>
                  <li>• VirusTotal API integration</li>
                  <li>• Database for evidence records</li>
                </ul>
              </div>
              
              <div className="p-4 bg-slate-50 rounded-lg">
                <h4 className="font-semibold text-slate-900 mb-2">Next Steps</h4>
                <ol className="text-sm text-slate-600 space-y-1 list-decimal list-inside">
                  <li>Set up file upload endpoint</li>
                  <li>Implement hash calculation</li>
                  <li>Integrate with Sepolia testnet</li>
                  <li>Add VirusTotal scanning</li>
                  <li>Create evidence record storage</li>
                </ol>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
```
