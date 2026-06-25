---
title: "ProtectedRoute"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic (backend)\\frontend-forenchain\\src\\components\\ProtectedRoute.jsx"
source_size_bytes: 304
source_modified: 2025-11-26T16:38:06
imported_at: 2026-06-14T14:25:34
tags:
  - acs
  - acs-advanced
  - imported
---

# ProtectedRoute

- Source: [ProtectedRoute.jsx](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%28backend%29/frontend-forenchain/src/components/ProtectedRoute.jsx)

## Content

```jsx
// src/components/ProtectedRoute.jsx
import { Navigate } from "react-router-dom";

const isAuthenticated = () => {
  return localStorage.getItem("auth_token") !== null;
};

export default function ProtectedRoute({ children }) {
  return isAuthenticated() ? children : <Navigate to="/login" />;
}
```
