---
title: "NavBar"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic  Copy\\integration-forenchain-frontend-main\\src\\components\\NavBar.jsx"
source_size_bytes: 2444
source_modified: 2025-11-30T14:49:41
imported_at: 2026-06-14T14:25:30
tags:
  - acs
  - acs-advanced
  - imported
---

# NavBar

- Source: [NavBar.jsx](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%20Copy/integration-forenchain-frontend-main/src/components/NavBar.jsx)

## Content

```jsx
// src/components/NavBar.jsx
import { Link } from 'react-router-dom';
import { logout } from '../lib/api';

export default function NavBar() {
  const user = JSON.parse(localStorage.getItem("auth_user") || "{}");
  const isLoggedIn = localStorage.getItem("auth_token") !== null;

  const handleLogout = () => {
    logout();
  };

  return (
    <nav className="bg-white border-b border-slate-200">
      <div className="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
        <div className="flex items-center gap-2">
          {/* Clickable Logo */}
          <Link 
            to="/" 
            className="flex items-center gap-2 hover:opacity-80 transition-opacity"
          >
            <span className="grid h-8 w-8 place-items-center rounded-lg bg-gradient-to-tr from-sky-500 to-violet-500 text-white text-sm font-bold">
              FC
            </span>
            <h1 className="text-xl font-bold text-slate-900">ForenChain</h1>
          </Link>
        </div>
        
        <div className="flex items-center gap-4">
          {isLoggedIn ? (
            <>
              <div className="flex gap-4">
                <Link to="/dashboard" className="text-slate-700 hover:text-slate-900 font-medium">
                  Dashboard
                </Link>
                <Link to="/upload" className="text-slate-700 hover:text-slate-900 font-medium">
                  Upload Evidence
                </Link>
                <Link to="/cases" className="text-slate-700 hover:text-slate-900 font-medium">
                  View Cases
                </Link>
              </div>
              <div className="text-right">
                <p className="text-sm font-medium text-slate-900">
                  {user.username || 'User'}
                </p>
                <button
                  onClick={handleLogout}
                  className="text-xs text-slate-500 hover:text-slate-700"
                >
                  Logout
                </button>
              </div>
            </>
          ) : (
            <div className="flex gap-4">
              <Link to="/login" className="text-slate-700 hover:text-slate-900 font-medium">
                Login
              </Link>
              <Link to="/signup" className="text-slate-700 hover:text-slate-900 font-medium">
                Sign Up
              </Link>
            </div>
          )}
        </div>
      </div>
    </nav>
  );
}
```
