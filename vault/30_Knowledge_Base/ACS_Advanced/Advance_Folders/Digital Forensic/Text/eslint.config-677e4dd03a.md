---
title: "eslint.config"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic (backend)\\frontend-forenchain\\eslint.config.js"
source_size_bytes: 792
source_modified: 2025-11-26T16:38:06
imported_at: 2026-06-14T14:25:30
tags:
  - acs
  - acs-advanced
  - imported
---

# eslint.config

- Source: [eslint.config.js](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%28backend%29/frontend-forenchain/eslint.config.js)

## Content

```js
import js from '@eslint/js'
import globals from 'globals'
import reactHooks from 'eslint-plugin-react-hooks'
import reactRefresh from 'eslint-plugin-react-refresh'
import { defineConfig, globalIgnores } from 'eslint/config'

export default defineConfig([
  globalIgnores(['dist']),
  {
    files: ['**/*.{js,jsx}'],
    extends: [
      js.configs.recommended,
      reactHooks.configs['recommended-latest'],
      reactRefresh.configs.vite,
    ],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
      parserOptions: {
        ecmaVersion: 'latest',
        ecmaFeatures: { jsx: true },
        sourceType: 'module',
      },
    },
    rules: {
      'no-unused-vars': ['error', { varsIgnorePattern: '^[A-Z_]' }],
    },
  },
])
```
