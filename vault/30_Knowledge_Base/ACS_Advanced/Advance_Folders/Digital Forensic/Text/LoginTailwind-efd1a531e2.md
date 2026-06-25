---
title: "LoginTailwind"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic  Copy\\integration-forenchain-frontend-main\\src\\components\\LoginTailwind.jsx"
source_size_bytes: 6490
source_modified: 2025-11-30T14:49:41
imported_at: 2026-06-14T14:25:29
tags:
  - acs
  - acs-advanced
  - imported
---

# LoginTailwind

- Source: [LoginTailwind.jsx](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%20Copy/integration-forenchain-frontend-main/src/components/LoginTailwind.jsx)

## Content

```jsx
// src/components/LoginTailwind.jsx
import { useState } from "react";
import { loginRequest } from "../lib/api";

export default function LoginTailwind() {
  const [username, setUsername] = useState(""); // Changed from email to username
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [showPassword, setShowPassword] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setLoading(true);
    try {
      const data = await loginRequest({ username, password }); // Send username instead of email
      if (data.access_token) localStorage.setItem("auth_token", data.access_token); // Changed from data.token
      if (data.user) localStorage.setItem("auth_user", JSON.stringify(data.user));
      window.location.href = "/dashboard";
    } catch (err) {
      setError(err.message || "Login failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-b from-white to-slate-50 text-slate-900">
      <div className="absolute inset-0 bg-[radial-gradient(60%_60%_at_50%_0%,rgba(99,102,241,0.08),transparent_80%)]" />

      <div className="relative z-10 w-full max-w-md p-8 bg-white rounded-2xl shadow-lg border border-slate-200">
        <div className="flex items-center gap-2 mb-6">
          <span className="grid h-9 w-9 place-items-center rounded-xl bg-gradient-to-tr from-sky-500 to-violet-500 text-white shadow-sm shadow-sky-500/20 ring-1 ring-slate-200">
            ⚡
          </span>
          <h1 className="text-xl font-semibold tracking-tight text-slate-900">
            ForenChain Access
          </h1>
        </div>
        <p className="text-sm text-slate-600 mb-6">
          Sign in to continue your investigation securely.
        </p>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-slate-700 mb-1">
              Username {/* Changed from Email */}
            </label>
            <input
              type="text" // Changed from email to text
              required
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="Enter your username" // Updated placeholder
              className="w-full rounded-lg border border-slate-300 bg-white px-4 py-2 text-slate-900 placeholder-slate-400 focus:border-sky-400 focus:ring-2 focus:ring-sky-200 outline-none transition"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-slate-700 mb-1">
              Password
            </label>
            <div className="relative">
              <input
                type={showPassword ? "text" : "password"}
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="••••••••"
                className="w-full rounded-lg border border-slate-300 bg-white px-4 py-2 pr-10 text-slate-900 placeholder-slate-400 focus:border-sky-400 focus:ring-2 focus:ring-sky-200 outline-none transition"
              />
              <button
                type="button"
                onClick={() => setShowPassword(!showPassword)}
                className="absolute right-3 top-1/2 transform -translate-y-1/2 text-slate-500 hover:text-slate-700 focus:outline-none"
              >
                {showPassword ? (
                  <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21" />
                  </svg>
                ) : (
                  <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                  </svg>
                )}
              </button>
            </div>
          </div>

          <div className="flex items-center justify-between text-sm">
            <label className="flex items-center gap-2">
              <input
                type="checkbox"
                className="h-4 w-4 rounded border-slate-300 text-sky-500 focus:ring-sky-400"
              />
              <span className="text-slate-600">Remember me</span>
            </label>
            <a href="#" className="text-sky-600 hover:text-sky-700 font-medium">
              Forgot?
            </a>
          </div>

          {error && <div className="text-sm text-rose-500">{error}</div>}

          <button
            type="submit"
            disabled={loading}
            className="w-full inline-flex items-center justify-center gap-2 rounded-lg bg-slate-900 text-white py-2 font-medium hover:bg-slate-800 transition disabled:opacity-60"
          >
            {loading && (
              <svg
                className="h-5 w-5 animate-spin text-white"
                viewBox="0 0 24 24"
                fill="none"
              >
                <circle
                  className="opacity-25"
                  cx="12"
                  cy="12"
                  r="10"
                  stroke="currentColor"
                  strokeWidth="4"
                />
                <path
                  className="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"
                />
              </svg>
            )}
            <span>Sign in</span>
          </button>
        </form>

        <p className="mt-6 text-center text-sm text-slate-600">
          Don't have an account?{" "}
          <a href="/signup" className="text-sky-600 hover:text-sky-700 font-medium">
            Sign up 
          </a>
        </p>
      </div>
    </div>
  );
}
```
