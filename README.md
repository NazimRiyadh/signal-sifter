# Signal Sifter

**Signal Sifter** is a Python-based data processing pipeline that analyzes plugin/product listings from JSON files.

The system cleans inconsistent listing data, validates records, removes duplicates, calculates ranking scores, and generates reports containing the highest-performing products.

---

## Features

* Reads multiple JSON listing files
* Handles inconsistent data formats
* Validates data using **Pydantic models**
* Normalizes product information
* Handles encoding problems and invalid JSON files gracefully
* Logs problematic files for manual review
* Removes duplicate listings
* Calculates product ranking scores
* Sorts products by ranking score
* Generates JSON and text reports

---

## Project Structure

```text
signal-sifter/
│
├── data/
│   └── JSON listing files
│
├── signal_sifter/
│   ├── models.py
│   ├── loader.py
│   ├── normalizer.py
│   ├── deduplicator.py
│   ├── scorer.py
│   ├── reporter.py
│   └── main.py
│
├── report/
│   ├── report.json
│   └── report.txt
│
├── requirements.txt
├── DECISIONS.md
├── README.md
└── .gitignore
```

> **Note:** The `report/` directory contains generated output and may be ignored by Git depending on the submission requirements.

---

## Installation

### Requirements

* Python 3.10+
* Pydantic

### 1. Clone the repository

```bash
git clone <repository-url>
cd signal-sifter
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
.venv\Scripts\activate.bat
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Run the pipeline with:

```bash
python -m signal_sifter --input data --output report
```

### Command-line Arguments

| Argument   | Description                                 | Default  |
| ---------- | ------------------------------------------- | -------- |
| `--input`  | Directory containing JSON listing files     | `data`   |
| `--output` | Directory where generated reports are saved | `report` |

### Example

```bash
python -m signal_sifter --input data --output report
```

---

## Processing Pipeline

The application processes the data through the following stages:

```text
Raw JSON Files
      │
      ▼
   Loader
      │
      ▼
Normalization
      │
      ▼
Pydantic Validation
      │
      ▼
Duplicate Removal
      │
      ▼
Score Calculation
      │
      ▼
   Ranking
      │
      ▼
Report Generation
```

---

## Data Handling

Signal Sifter is designed to continue processing even when individual input files contain problems.

### Encoding Problems

The loader attempts multiple character encodings when reading JSON files.

This allows recoverable encoding issues to be handled without stopping the entire pipeline.

### Invalid JSON

If a file contains malformed JSON, it is not allowed to interrupt the pipeline.

Instead, the file is:

1. Detected as invalid
2. Logged for review
3. Skipped
4. Processing continues with the remaining valid files

This approach prevents one corrupted input file from causing the entire pipeline to fail.

---

## Deduplication

Duplicate listings are identified using a normalized product name.

When duplicate products are found, the pipeline keeps the listing with the stronger available performance signals, such as:

* Installs
* Reviews

This prevents duplicate entries from affecting the final ranking.

---

## Scoring and Ranking

After normalization and deduplication, each product receives a ranking score.

Products are then sorted in descending order:

```text
Highest Score
      ↓
      ...
      ↓
Lowest Score
```

The highest-scoring products are included in the generated reports.

---

## Output

After successful execution, the application generates reports in the specified output directory:

```text
report/
├── report.json
└── report.txt
```

### `report.json`

Contains structured ranking information for the top products, including:

* Rank
* Product name
* Score
* Installs
* Rating
* Reviews
* Last update date

Example:

```json
{
    "rank": 1,
    "name": "Example Product",
    "score": 87.02,
    "installs": 18000,
    "rating": 4.5,
    "reviews": 250,
    "last_updated": "2026-08-08T10:00:00+00:00"
}
```

### `report.txt`

Contains a human-readable summary of the highest-ranked products.

Example:

```text
Signal Sifter Top Products

1. Example Product
Score: 87.02
Installs: 18000
Rating: 4.5
Reviews: 250
```

---

## Requirements

Dependencies are listed in `requirements.txt`.

Install them with:

```bash
pip install -r requirements.txt
```

---

## Design Decisions

Important implementation and design decisions are documented separately in:

```text
DECISIONS.md
```

This document explains the reasoning behind choices such as:

* Data normalization
* Validation
* Deduplication
* Error handling
* Encoding fallbacks
* Scoring
* Report generation

---

## Reliability

The project was designed with reliability and fault tolerance in mind.

Rather than failing because of a single problematic input file, Signal Sifter isolates the problematic record, logs the issue for review, and continues processing valid data whenever possible.

This makes the pipeline more suitable for real-world datasets where imperfect input is expected.
