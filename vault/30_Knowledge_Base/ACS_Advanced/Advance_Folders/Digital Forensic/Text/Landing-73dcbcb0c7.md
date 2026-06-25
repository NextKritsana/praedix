---
title: "Landing"
type: "acs-advance-text"
course: "ACS Advanced"
course_folder: "Digital Forensic"
source_path: "E:\\ProJect\\ACS File\\advance\\Digital Forensic\\Project Digital Forensic (backend)\\frontend-forenchain\\src\\components\\Landing.jsx"
source_size_bytes: 6496
source_modified: 2025-11-26T16:38:06
imported_at: 2026-06-14T14:25:34
tags:
  - acs
  - acs-advanced
  - imported
---

# Landing

- Source: [Landing.jsx](file:///E:/ProJect/ACS%20File/advance/Digital%20Forensic/Project%20Digital%20Forensic%20%28backend%29/frontend-forenchain/src/components/Landing.jsx)

## Content

```jsx
// src/components/Landing.jsx
import { Link } from "react-router-dom";

function Section({ id, children, className = "" }) {
  return (
    <section id={id} className={`mx-auto max-w-6xl px-4 py-16 ${className}`}>
      {children}
    </section>
  );
}

export default function Landing() {
  return (
    <main className="min-h-screen bg-gradient-to-b from-white to-slate-50">
      <div className="mx-auto w-full max-w-7xl px-4 py-12">
        <div className="mb-6 inline-block rounded-md bg-emerald-500 px-3 py-1 text-sm font-semibold text-white">TAILWIND OK</div>

        {/* HERO */}
        <Section>
          <div className="grid items-center gap-12 lg:grid-cols-2">
            <div className="space-y-6">
              <h1 className="text-4xl font-extrabold tracking-tight text-slate-900 md:text-5xl">
                Digital Forensics, <span className="underline decoration-4 decoration-slate-900">Trustworthy</span> &amp; Verifiable
              </h1>
              <p className="max-w-xl text-lg text-slate-600">
                ForenChain helps investigators manage digital evidence (.pcap/.dd), track chain of custody on blockchain, and generate court-ready reports.
              </p>

              <div className="flex flex-wrap gap-3">
                <Link to="/login" className="inline-flex items-center gap-2 rounded-full bg-slate-900 px-6 py-3 text-sm font-semibold text-white shadow hover:opacity-95">
                  Get Started
                </Link>
                <a href="#features" className="inline-flex items-center gap-2 rounded-full border px-5 py-3 text-sm hover:bg-slate-100">
                  See Features
                </a>
              </div>

              <p className="mt-4 text-xs text-slate-500">Testnet: Sepolia • Integrations: VirusTotal • Export: PDF</p>
            </div>

            {/* Preview Card */}
            <div className="relative flex items-center justify-center">
              <div className="absolute -inset-6 rounded-3xl bg-gradient-to-br from-slate-200/70 to-white/40 blur-3xl" />
              <div className="relative w-full max-w-md rounded-3xl bg-white p-6 shadow-lg ring-1 ring-slate-200">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm text-slate-500">Sample Case</p>
                    <h3 className="text-lg font-semibold">INV-2025-001</h3>
                  </div>
                  <span className="rounded-full border px-2 py-1 text-xs text-emerald-700">REPORT READY</span>
                </div>

                <div className="mt-4 grid grid-cols-2 gap-4 text-sm">
                  <div className="rounded-xl p-3 ring-1 ring-slate-200">
                    <p className="text-slate-500">File</p>
                    <p className="font-medium">capture.pcap</p>
                  </div>
                  <div className="rounded-xl p-3 ring-1 ring-slate-200">
                    <p className="text-slate-500">Hash</p>
                    <p className="break-all font-mono text-xs">0x9f3…a12</p>
                  </div>
                  <div className="rounded-xl p-3 ring-1 ring-slate-200">
                    <p className="text-slate-500">Tx (Sepolia)</p>
                    <p className="break-all font-mono text-xs">0x7b0…e88</p>
                  </div>
                  <div className="rounded-xl p-3 ring-1 ring-slate-200">
                    <p className="text-slate-500">VT Flags</p>
                    <p className="font-medium">2 malicious</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </Section>

        {/* FEATURES */}
        <Section id="features" className="pt-6">
          <h2 className="text-3xl font-bold text-slate-900">Key Features</h2>
          <div className="mt-8 grid gap-6 md:grid-cols-3">
            {[
              { title: "Evidence Upload", desc: "Accept .pcap & .dd with validation and case metadata." },
              { title: "Chain of Custody", desc: "Hashes & transactions recorded on Sepolia for integrity." },
              { title: "Analysis & Reports", desc: "Summarize findings (VirusTotal) and export PDF." },
            ].map((f) => (
              <div key={f.title} className="rounded-2xl bg-white p-6 shadow-sm ring-1 ring-slate-200">
                <div className="text-2xl">🔍</div>
                <h3 className="mt-3 font-semibold text-slate-900">{f.title}</h3>
                <p className="mt-2 text-slate-600">{f.desc}</p>
              </div>
            ))}
          </div>
        </Section>

        {/* HOW IT WORKS */}
        <Section id="how">
          <h2 className="text-3xl font-bold text-slate-900">How it works</h2>
          <ol className="mt-6 grid gap-4 text-sm md:grid-cols-4">
            {[
              ["1. Upload", "Upload evidence & metadata."],
              ["2. Hashing", "Create hash & record to blockchain."],
              ["3. Analysis", "VirusTotal scan + artifact extraction."],
              ["4. Report", "Preview & download the PDF report."],
            ].map(([title, desc]) => (
              <li key={title} className="rounded-2xl bg-white p-4 shadow-sm ring-1 ring-slate-200">
                <p className="text-xs text-slate-500">{title}</p>
                <p className="font-medium">{desc}</p>
              </li>
            ))}
          </ol>
        </Section>

        {/* CTA */}
        <Section className="text-center">
          <h3 className="text-2xl font-semibold text-slate-900">Ready to try ForenChain?</h3>
          <p className="mt-2 text-slate-600">Create a trial account and start managing your digital evidence.</p>
          <Link to="/login" className="mt-6 inline-flex rounded-xl bg-slate-900 px-5 py-3 text-white hover:opacity-90">Sign in / Register</Link>
        </Section>

        {/* FOOTER */}
        <footer id="contact" className="border-t bg-white mt-12">
          <div className="mx-auto flex max-w-6xl flex-col gap-2 px-4 py-8 text-sm text-slate-600 md:flex-row md:items-center md:justify-between">
            <p>© {new Date().getFullYear()} ForenChain</p>
            <p className="text-xs">Contact: <a href="mailto:team@forenchain.local" className="underline">team@forenchain.local</a></p>
          </div>
        </footer>
      </div>
    </main>
  );
}
```
