# Engineering Decisions

## 1. Data Loading Strategy

The input dataset contains multiple JSON files with inconsistent quality. The loader was designed to process files independently so that one problematic file does not stop the entire pipeline.

The loader:
- Reads all JSON files from the provided input directory.
- Attempts multiple encodings (`utf-8`, `utf-8-sig`, and `latin-1`) to handle recoverable encoding issues.
- Skips files with invalid JSON syntax while continuing the remaining processing.

This approach prioritizes pipeline reliability over failing completely because of a single corrupted input file.

---

## 2. Data Validation and Normalization

The raw listings contain different field names and formats. To create a consistent internal representation, all records are converted into a common `Product` model using Pydantic.

Examples of normalization decisions:

- Product name fields:
  - `title`
  - `name`
  - `product_name`

  are mapped into a single `name` field.

- Install count fields:
  - `installs`
  - `install_count`
  - nested `stats.installs`

  are converted into an integer value.

- Rating fields:
  - `rating`
  - `stars`
  - `score`

  are converted into a floating-point value.

- Date fields are converted into a consistent Python `date` object.

Missing numeric values are assigned default values to allow consistent scoring.

---

## 3. Duplicate Detection Strategy

Duplicate products were identified using normalized product names.

The normalization process:
- Converts names to lowercase.
- Removes extra whitespace.
- Creates a consistent comparison key.

Example:


"Cache Rocket"
"cache rocket "
"CACHE ROCKET"


are treated as the same product.

When duplicates are found, the stronger listing based on engagement signals is retained.

This approach was chosen because the dataset does not provide a guaranteed universal product identifier.

---

## 4. Scoring Strategy

The ranking score represents product strength using three main signals:

- Installation popularity
- User rating
- Review volume

The score is calculated using:


Install points + Rating points + Review points


To avoid extremely large products dominating the ranking:

- Installation points are capped.
- Review points are capped.

Products that have not been updated within the defined stale period receive a score of zero.

---

## 5. Report Generation

The system produces two outputs:

### report.json

Designed for machine consumption and further processing.

### report.txt

Designed for human readability.

The final report contains the top-ranked products sorted by descending score.

---

## 6. Error Handling Philosophy

The pipeline follows a "continue processing where possible" approach.

Recoverable issues:
- Encoding problems → try alternative encodings.

Non-recoverable issues:
- Invalid JSON structure → skip the file.

This prevents a single bad input from breaking the entire analysis.

---

## 7. Use of AI Assistance

AI tools were used as a development assistant for:
- Understanding project requirements.
- Discussing Python implementation approaches.
- Debugging errors during development.
- Reviewing code structure.

All generated suggestions were reviewed, modified where necessary, and tested before being included in the final implemen