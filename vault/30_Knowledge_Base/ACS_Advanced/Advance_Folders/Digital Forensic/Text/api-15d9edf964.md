---
title: "api"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic (backend)\\frontend-forenchain\\src\\lib\\api.js"
source_size_bytes: 3758
source_modified: 2025-11-26T16:38:06
imported_at: 2026-06-14T14:25:35
tags:
  - acs
  - acs-advanced
  - imported
---

# api

- Source: [api.js](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%28backend%29/frontend-forenchain/src/lib/api.js)

## Content

```js
// src/lib/api.js
const API_BASE = import.meta.env.VITE_API_BASE || ''

// Mock user database for development
const mockUsers = [
  {
    id: 1,
    firstName: 'John',
    lastName: 'Investigator',
    email: 'demo@forenchain.com',
    password: 'demopass123',
    examinerId: 'EXM-047'
  },
  {
    id: 2,
    firstName: 'Jane',
    lastName: 'Analyst',
    email: 'jane@forenchain.com',
    password: 'password123',
    examinerId: 'EXM-048'
  }
];

// Mock login function for development
export async function loginRequest({ email, password }) {
  // If we have a real API base, use it
  if (API_BASE) {
    const url = `${API_BASE.replace(/\/$/, '')}/auth/login`
    const res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password }),
    })

    if (!res.ok) {
      const errText = await res.text().catch(() => null)
      let message = `Request failed with status ${res.status}`
      try {
        const json = JSON.parse(errText)
        message = json.message || message
      } catch (e) {
        if (errText) message = errText
      }
      const error = new Error(message)
      error.status = res.status
      throw error
    }

    const data = await res.json()
    return data
  }

  // Mock authentication for development
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const user = mockUsers.find(u => u.email === email && u.password === password);
      
      if (user) {
        // Remove password from user object
        const { password: _, ...userWithoutPassword } = user;
        
        resolve({
          token: `mock_jwt_token_${user.id}_${Date.now()}`,
          user: userWithoutPassword
        });
      } else {
        reject(new Error('Invalid email or password'));
      }
    }, 1000); // Simulate network delay
  });
}

// Mock signup function for development
export async function signupRequest({ firstName, lastName, email, password }) {
  // If we have a real API base, use it
  if (API_BASE) {
    const url = `${API_BASE.replace(/\/$/, '')}/auth/signup`
    const res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ 
        firstName, 
        lastName, 
        email, 
        password 
      }),
    })

    if (!res.ok) {
      const errText = await res.text().catch(() => null)
      let message = `Request failed with status ${res.status}`
      try {
        const json = JSON.parse(errText)
        message = json.message || message
      } catch (e) {
        if (errText) message = errText
      }
      const error = new Error(message)
      error.status = res.status
      throw error
    }

    const data = await res.json()
    return data
  }

  // Mock registration for development
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const existingUser = mockUsers.find(u => u.email === email);
      
      if (existingUser) {
        reject(new Error('User already exists with this email'));
        return;
      }

      const newUser = {
        id: mockUsers.length + 1,
        firstName,
        lastName,
        email,
        password, // In real app, this would be hashed
        examinerId: `EXM-${String(mockUsers.length + 1).padStart(3, '0')}`
      };

      // Remove password from response
      const { password: _, ...userWithoutPassword } = newUser;
      
      resolve({
        token: `mock_jwt_token_${newUser.id}_${Date.now()}`,
        user: userWithoutPassword
      });
    }, 1000); // Simulate network delay
  });
}
```
