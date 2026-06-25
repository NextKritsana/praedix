---
title: "README_TAILWIND"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic  Copy\\integration-forenchain-frontend-main\\README_TAILWIND.md"
source_size_bytes: 1387
source_modified: 2025-11-30T14:49:41
imported_at: 2026-06-14T14:25:29
tags:
  - acs
  - acs-advanced
  - imported
---

# README_TAILWIND

- Source: [README_TAILWIND.md](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%20Copy/integration-forenchain-frontend-main/README_TAILWIND.md)

## Content

```md
Tailwind & Login Setup
======================

This project now includes a Tailwind-based login component at `src/components/LoginTailwind.jsx` and a small API helper at `src/lib/api.js`.

Quick start (Windows PowerShell):

```powershell
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
npm run dev
```

Environment variables:

Create a `.env` file in the project root with:

```
VITE_API_BASE=https://api.example.com
```

How login works

- The login component POSTs to `${VITE_API_BASE}/auth/login` with JSON `{ email, password }`.
- Expected success response: `{ token: string, user?: object }`.
- On success the token is saved to `localStorage` as `auth_token` and the user (if present) as `auth_user`. The component then redirects to `/dashboard` (change as needed).

Files added/changed

- `tailwind.config.cjs` – Tailwind content and color extensions.
- `postcss.config.cjs` – PostCSS setup for Tailwind.
- `src/index.css` – Tailwind directives added.
- `src/components/LoginTailwind.jsx` – New login UI using Tailwind.
- `src/lib/api.js` – Small helper wrapping the login request.

Next steps

- Install the Tailwind packages above.
- Adjust `VITE_API_BASE` and the endpoint path in `src/lib/api.js` if your backend uses a different route.
- Add routing (React Router) and a protected route wrapper to handle auth token validation on the client.
```
