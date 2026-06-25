---
title: "App"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic (backend)\\frontend-forenchain\\src\\App.jsx"
source_size_bytes: 3551
source_modified: 2025-11-26T16:38:06
imported_at: 2026-06-14T14:25:34
tags:
  - acs
  - acs-advanced
  - imported
---

# App

- Source: [App.jsx](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%28backend%29/frontend-forenchain/src/App.jsx)

## Content

```jsx
// src/App.jsx
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import NavBar from "./components/NavBar.jsx";
import Landing from "./components/Landing.jsx";
import LoginTailwind from "./components/LoginTailwind.jsx";
import SignUp from "./components/SignUp.jsx";
import UploadEvidence from "./components/UploadEvidence.jsx";

// Simple auth check
const isAuthenticated = () => {
  return localStorage.getItem("auth_token") !== null;
};

// Protected Route component
const ProtectedRoute = ({ children }) => {
  return isAuthenticated() ? children : <Navigate to="/login" />;
};

// Dashboard component
function Dashboard() {
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

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Public routes with navbar */}
        <Route path="/" element={
          <>
            <NavBar />
            <Landing />
          </>
        } />
        
        {/* Auth routes without navbar */}
        <Route path="/login" element={<LoginTailwind />} />
        <Route path="/signup" element={<SignUp />} />
        
        {/* Protected routes with navbar */}
        <Route path="/dashboard" element={
          <ProtectedRoute>
            <>
              <NavBar />
              <Dashboard />
            </>
          </ProtectedRoute>
        } />
        
        <Route path="/upload" element={
          <ProtectedRoute>
            <>
              <NavBar />
              <UploadEvidence />
            </>
          </ProtectedRoute>
        } />
        
        {/* Redirect unknown routes to home */}
        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
```
