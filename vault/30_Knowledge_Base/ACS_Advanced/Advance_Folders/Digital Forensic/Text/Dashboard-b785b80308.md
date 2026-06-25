---
title: "Dashboard"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic (backend)\\frontend-forenchain\\src\\components\\Dashboard.jsx"
source_size_bytes: 1880
source_modified: 2025-11-26T16:38:06
imported_at: 2026-06-14T14:25:34
tags:
  - acs
  - acs-advanced
  - imported
---

# Dashboard

- Source: [Dashboard.jsx](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%28backend%29/frontend-forenchain/src/components/Dashboard.jsx)

## Content

```jsx
// src/components/Dashboard.jsx
export default function Dashboard() {
  const user = JSON.parse(localStorage.getItem("auth_user") || "{}");
  
  return (
    <div className="min-h-screen bg-slate-50 py-8">
      <div className="max-w-4xl mx-auto px-4">
        <div className="bg-white rounded-2xl shadow-lg p-6">
          <h1 className="text-2xl font-bold text-slate-900 mb-2">Dashboard</h1>
          <p className="text-slate-600 mb-6">
            Welcome back, {user.firstName || "Investigator"}!
          </p>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="bg-slate-50 rounded-xl p-6 border border-slate-200">
              <h3 className="font-semibold text-slate-900 mb-2">Quick Actions</h3>
              <ul className="space-y-2">
                <li>
                  <a href="/upload" className="text-sky-600 hover:text-sky-700 font-medium">
                    Upload New Evidence
                  </a>
                </li>
                <li>
                  <a href="#" className="text-sky-600 hover:text-sky-700 font-medium">
                    View Case History
                  </a>
                </li>
                <li>
                  <a href="#" className="text-sky-600 hover:text-sky-700 font-medium">
                    Generate Reports
                  </a>
                </li>
              </ul>
            </div>
            
            <div className="bg-slate-50 rounded-xl p-6 border border-slate-200">
              <h3 className="font-semibold text-slate-900 mb-2">Recent Activity</h3>
              <p className="text-slate-600 text-sm">
                No recent activity. Upload your first evidence file to get started.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
```
