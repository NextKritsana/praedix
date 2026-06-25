---
title: "NavBar"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic (backend)\\frontend-forenchain\\src\\components\\NavBar.jsx"
source_size_bytes: 1417
source_modified: 2025-11-26T16:38:06
imported_at: 2026-06-14T14:25:34
tags:
  - acs
  - acs-advanced
  - imported
---

# NavBar

- Source: [NavBar.jsx](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%28backend%29/frontend-forenchain/src/components/NavBar.jsx)

## Content

```jsx
// src/components/NavBar.jsx
import { useState } from "react";
import { Link } from "react-router-dom";

export default function NavBar() {
  const [open, setOpen] = useState(false);

  return (
    <header className="sticky top-0 z-30 bg-white/80 backdrop-blur border-b">
      <nav className="max-w-6xl mx-auto px-4 py-3 flex items-center justify-between">
        <Link to="/" className="flex items-center gap-2">
          <img src="/vite.svg" alt="logo" className="h-6 w-6" />
          <span className="font-semibold">ForenChain</span>
        </Link>

        <button
          className="md:hidden p-2 rounded-lg border"
          onClick={() => setOpen(!open)}
          aria-label="Toggle menu"
        >
          ☰
        </button>

        <ul className={`md:flex md:items-center gap-6 ${open ? "block mt-3" : "hidden md:flex"}`}>
          <li><a href="#features" className="hover:underline">Features</a></li>
          <li><a href="#how" className="hover:underline">How It Works</a></li>
          <li><a href="#contact" className="hover:underline">Contact</a></li>
          <li>
            <Link
              to="/login"
              className="inline-flex items-center rounded-xl px-4 py-2 border bg-black text-white hover:opacity-90"
            >
              Login
            </Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}
```
