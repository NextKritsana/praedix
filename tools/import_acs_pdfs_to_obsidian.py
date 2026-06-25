from __future__ import annotations

import re
import sys
from datetime import datetime
from pathlib import Path

from pypdf import PdfReader


SOURCE_DIR = Path(r"E:\ProJect\ACS File")
OUTPUT_DIR = Path(r"E:\ProJect\Praedix\vault\30_Knowledge_Base\ACS_Advanced")

PDF_FILES = [
    "AndroidPentest101.pdf",
    "Bug Bounting.pdf",
    "Consulting.pdf",
    "Cryptogtaphy.pdf",
    "Linux fundamentals ACS.pdf",
    "Network ACS.pdf",
    "Pentesting.pdf",
    "ProgramACS.pdf",
    "system ACS.pdf",
    "Web ACS.pdf",
    "คำศัพธืทั้งหมดที่เกี่ยวกับ System ACS.pdf",
]


def note_name(filename: str) -> str:
    stem = Path(filename).stem.strip()
    cleaned = re.sub(r'[<>:"/\\|?*]+', "-", stem)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return f"{cleaned}.md"


def yaml_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip()


def extract_pdf(pdf_path: Path) -> tuple[int, list[tuple[int, str]]]:
    reader = PdfReader(str(pdf_path))
    pages: list[tuple[int, str]] = []
    for index, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ""
        except Exception as exc:
            text = f"[Extraction error: {exc}]"
        pages.append((index, clean_text(text)))
    return len(reader.pages), pages


def write_note(pdf_path: Path) -> tuple[str, int, int]:
    page_count, pages = extract_pdf(pdf_path)
    output_path = OUTPUT_DIR / note_name(pdf_path.name)
    extracted_pages = sum(1 for _, text in pages if text)
    source_stat = pdf_path.stat()
    imported_at = datetime.now().isoformat(timespec="seconds")

    lines = [
        "---",
        f'title: "{yaml_escape(pdf_path.stem)}"',
        "type: acs-course-pdf",
        'course: "ACS Advanced"',
        f'source_pdf: "{yaml_escape(str(pdf_path))}"',
        f"source_size_bytes: {source_stat.st_size}",
        f"source_modified: {datetime.fromtimestamp(source_stat.st_mtime).isoformat(timespec='seconds')}",
        f"imported_at: {imported_at}",
        f"pages: {page_count}",
        "tags:",
        "  - acs",
        "  - imported-pdf",
        "  - cybersecurity",
        "---",
        "",
        f"# {pdf_path.stem}",
        "",
        f"- Source PDF: `{pdf_path}`",
        f"- Pages: {page_count}",
        f"- Pages with extracted text: {extracted_pages}",
        "",
        "> Imported from PDF for Obsidian search and review. Verify formatting against the original PDF when precision matters.",
        "",
    ]

    for page_number, text in pages:
        lines.append(f"## Page {page_number}")
        lines.append("")
        if text:
            lines.append(text)
        else:
            lines.append("_No extractable text found on this page._")
        lines.append("")

    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return output_path.name, page_count, extracted_pages


def write_index(results: list[tuple[str, int, int]]) -> None:
    lines = [
        "---",
        'title: "ACS Advanced Index"',
        "type: index",
        'course: "ACS Advanced"',
        "tags:",
        "  - acs",
        "  - index",
        "  - cybersecurity",
        "---",
        "",
        "# ACS Advanced Index",
        "",
        "Imported ACS course PDFs converted to Markdown notes for Obsidian search.",
        "",
        "| Note | Pages | Extracted pages |",
        "| --- | ---: | ---: |",
    ]
    for filename, page_count, extracted_pages in results:
        title = Path(filename).stem
        lines.append(f"| [[{title}]] | {page_count} | {extracted_pages} |")
    lines.append("")
    (OUTPUT_DIR / "_ACS Advanced Index.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    results: list[tuple[str, int, int]] = []
    missing: list[str] = []

    for filename in PDF_FILES:
        pdf_path = SOURCE_DIR / filename
        if not pdf_path.exists():
            missing.append(filename)
            continue
        results.append(write_note(pdf_path))

    write_index(results)

    print(f"Imported {len(results)} PDFs into {OUTPUT_DIR}")
    for filename, page_count, extracted_pages in results:
        print(f"- {filename}: {extracted_pages}/{page_count} pages with text")
    if missing:
        print("Missing files:")
        for filename in missing:
            print(f"- {filename}")


if __name__ == "__main__":
    main()
