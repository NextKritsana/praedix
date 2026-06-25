---
title: "Dashboard"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic  Copy\\integration-forenchain-frontend-main\\src\\components\\Dashboard.jsx"
source_size_bytes: 4454
source_modified: 2025-11-30T14:49:41
imported_at: 2026-06-14T14:25:29
tags:
  - acs
  - acs-advanced
  - imported
---

# Dashboard

- Source: [Dashboard.jsx](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%20Copy/integration-forenchain-frontend-main/src/components/Dashboard.jsx)

## Content

```jsx
// src/components/Dashboard.jsx
import { Link } from 'react-router-dom';
import { logout } from '../lib/api';

export default function Dashboard() {
  const user = JSON.parse(localStorage.getItem("auth_user") || "{}");

  const handleLogout = () => {
    logout();
  };

  return (
    <div className="min-h-screen bg-slate-50">
      {/* Header removed - now using the NavBar from App.jsx */}

      <div className="max-w-6xl mx-auto px-4 py-8">
        {/* Welcome Section */}
        <div className="bg-white rounded-2xl shadow-lg p-6 mb-6">
          <h1 className="text-2xl font-bold text-slate-900 mb-2">Dashboard</h1>
          <p className="text-slate-600">
            Welcome back, {user.username || "Investigator"}!
          </p>
        </div>
        
        {/* Quick Actions Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {/* Upload Evidence Card */}
          <div className="bg-white rounded-2xl shadow-lg p-6">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-12 h-12 bg-sky-100 rounded-lg flex items-center justify-center">
                <span className="text-2xl text-sky-600">📁</span>
              </div>
              <h3 className="font-semibold text-slate-900 text-lg">Upload Evidence</h3>
            </div>
            <p className="text-slate-600 text-sm mb-4">
              Upload new digital evidence files for blockchain verification and analysis.
            </p>
            <Link 
              to="/upload" 
              className="inline-flex items-center gap-2 px-4 py-2 bg-sky-600 text-white rounded-lg hover:bg-sky-700 transition-colors"
            >
              <span>Upload Evidence</span>
              <span>→</span>
            </Link>
          </div>

          {/* View Cases Card */}
          <div className="bg-white rounded-2xl shadow-lg p-6">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-12 h-12 bg-emerald-100 rounded-lg flex items-center justify-center">
                <span className="text-2xl text-emerald-600">📊</span>
              </div>
              <h3 className="font-semibold text-slate-900 text-lg">Case History</h3>
            </div>
            <p className="text-slate-600 text-sm mb-4">
              View all investigation cases, check status, and manage your forensic analyses.
            </p>
            <Link 
              to="/cases" 
              className="inline-flex items-center gap-2 px-4 py-2 bg-emerald-600 text-white rounded-lg hover:bg-emerald-700 transition-colors"
            >
              <span>View All Cases</span>
              <span>→</span>
            </Link>
          </div>

          {/* Generate Reports Card */}
          <div className="bg-white rounded-2xl shadow-lg p-6">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center">
                <span className="text-2xl text-purple-600">📄</span>
              </div>
              <h3 className="font-semibold text-slate-900 text-lg">Generate Reports</h3>
            </div>
            <p className="text-slate-600 text-sm mb-4">
              Create comprehensive investigation reports with blockchain verification.
            </p>
            <Link 
              to="/reports" 
              className="inline-flex items-center gap-2 px-4 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700 transition-colors"
            >
              <span>Generate Reports</span>
              <span>→</span>
            </Link>
          </div>
        </div>

        {/* Recent Activity Preview */}
        <div className="mt-8 bg-white rounded-2xl shadow-lg p-6">
          <div className="flex items-center justify-between mb-6">
            <h3 className="font-semibold text-slate-900 text-lg">Recent Activity</h3>
            <Link 
              to="/cases" 
              className="text-sky-600 hover:text-sky-700 font-medium text-sm"
            >
              View All →
            </Link>
          </div>
          <div className="text-center py-8">
            <div className="text-4xl mb-3">🔍</div>
            <p className="text-slate-600">
              No recent activity. Start by uploading evidence or viewing cases.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
```
