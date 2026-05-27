# CWE Collection System

A Python-based tool that automates the collection and classification of CWE (Common Weakness Enumeration) security data from MITRE's website, matching standardized keywords against published weakness descriptions to reduce manual analysis effort.

---

## What This Project Does

This tool addresses a manual, time-consuming process: reading through CWE web pages and identifying which security weaknesses and design considerations apply to each entry. The program automates this by:

1. Scraping CWE pages directly from `cwe.mitre.org`
2. Extracting relevant sections such as Common Consequences and Potential Mitigations
3. Matching extracted text against two curated keyword lists — Security Impacts and Security Related Design
4. Storing results in a SQLite database for analysis and reporting

---

## Keyword Lists

Two keyword lists were carefully curated from a source CSV file (`More Weaknesses(CWEs Analyzed) - Updated.csv`):

- **Security Impact** — 68 unique keyword phrases describing the potential consequences of a weakness (e.g., `execute unauthorized code`, `bypass protection mechanism`, `read application data`)
- **Security Related Design** — 141 unique keyword phrases describing design and implementation considerations (e.g., `input validation`, `parameterization`, `access control`)

---

## How the Keywords Are Parsed from the CSV

The CSV file requires specific handling:

- **Encoding:** `latin-1`
- **Non-breaking spaces:** `\xa0` characters are normalized to regular spaces before any processing
- **Splitting:** Values are split on commas only to preserve full multi-word phrases
- **Cleaning:** Each phrase is lowercased, whitespace-collapsed, and trailing periods removed
- **Deduplication:** A Python `set` ensures each keyword appears only once

---

## How the Web Scraping Works

Each CWE page is fetched using `requests` and parsed with `BeautifulSoup`. The scraper anchors to known HTML IDs — such as `id="common_consequences"` and `id="Potential_Mitigations"` — to reliably extract only the relevant sections without picking up unrelated page content. Text is extracted, newlines are normalized, and the content is matched against the keyword lists using partial matching.

---

## Keyword Matching

The program uses partial/substring matching to identify keywords within scraped text. This approach accounts for natural variation in phrasing across CWE pages. Each match is recorded alongside the section it was found in.

---

## Database

Results are stored in a SQLite database with separate tables for:

- `Weaknesses` — CWE entries including ID, name, and description
- `Impacts` — Security Impact keywords
- `Relateds` — Security Related Design keywords

Duplicate entries are handled using `INSERT OR IGNORE` with unique constraints on keyword columns.

---

## Requirements

- Python 3
- `requests`
- `beautifulsoup4`
- `sqlite3` (built into Python)
