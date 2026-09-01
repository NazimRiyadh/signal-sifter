# Development Notes and Reflections

## Time Spent

Approximately **4.30 hours** were spent completing this assessment.


The implementation took slightly longer than initially estimated because understanding variations in the input data and deciding how to handle edge cases required additional investigation.

---

# Key Decisions and Rationale

## 1. Modular Project Structure

The application was separated into dedicated modules:

* `loader.py`
* `normalizer.py`
* `models.py`
* `deduplicator.py`
* `scorer.py`
* `reporter.py`

This was chosen instead of implementing the entire pipeline in a single script because each module has a distinct responsibility.

The modular structure improves:

* Readability
* Maintainability
* Testability
* Separation of concerns
* Future extensibility

---

## 2. Handling Invalid and Inconsistent Input Files

The dataset contains files with different types of issues.

### Encoding Problems

For encoding-related problems, the loader attempts multiple encodings:

1. UTF-8
2. UTF-8 with BOM
3. Latin-1

This approach allows potentially recoverable encoding issues to be handled without stopping the entire pipeline.

### Invalid JSON

Structurally invalid JSON files are not automatically repaired.

Instead, they are:

1. Detected
2. Logged for review
3. Skipped
4. Excluded from further processing

Automatic repair was intentionally avoided because reconstructing corrupted data without knowing the original intended value could introduce inaccurate information.

---

## 3. Normalization Strategy

The raw dataset uses different field names for similar concepts.

Examples include:

| Raw Fields                                         | Internal Field |
| -------------------------------------------------- | -------------- |
| `title`, `name`, `product_name`                    | `name`         |
| `installs`, `install_count`, nested install values | `installs`     |
| `rating`, `stars`, `score`                         | `rating`       |

A dedicated normalization layer converts these variations into a consistent internal representation.

This allows downstream components to operate on a predictable data model rather than handling multiple possible field formats.

---

## 4. Duplicate Handling

The brief required duplicate removal but did not define a specific duplicate-identification strategy.

I chose **normalized product names** as the primary duplicate key because a universal unique identifier was not guaranteed across all records.

Normalization includes:

* Converting names to lowercase
* Removing leading and trailing whitespace
* Normalizing whitespace

For example:

```text
Cache Rocket
cache rocket
CACHE ROCKET
```

are treated as the same product.

When duplicate records are found, the record with stronger engagement signals is retained.

### Future Improvement

With additional time, I would explore more advanced duplicate detection techniques, such as:

* String similarity
* Token-based similarity
* Fuzzy matching
* Embedding-based similarity

These approaches could identify duplicates even when product names differ more substantially.

---

## 5. Scoring Approach

The brief required products to be ranked but did not prescribe a specific scoring formula.

The implementation combines three primary signals:

* Installation count
* User rating
* Review volume

The scoring system is deterministic and transparent, making the resulting ranking easy to understand and reproduce.

Limits are also applied to selected components so that extremely large products do not dominate the ranking solely because of one metric.

For stale products, the implementation follows the brief's requirement by assigning a score of zero when the product has not been updated within the defined recency window.

---

## Advanced Duplicate Detection

The current implementation primarily relies on normalized names.

A future version could incorporate fuzzy matching or semantic similarity to identify records with significantly different but equivalent names.

---

# Ambiguities and Interpretation

## Duplicate Definition

The brief did not explicitly specify how duplicate products should be identified.

Normalized product names were selected because they provide a simple, deterministic strategy without relying on a unique identifier that may not be consistently available.

---

## Missing Values

The brief did not fully define how missing numerical values should be handled.

Default values are used where appropriate so that the scoring pipeline can operate consistently without allowing individual incomplete records to terminate the entire process.

---

## Scoring Formula

The brief provided flexibility regarding ranking methodology.

I selected a transparent deterministic scoring method rather than a more complex machine-learning-based ranking model because:

* The dataset is relatively small
* The ranking should be explainable
* The scoring behavior should be reproducible
* There is no labeled ranking dataset available for supervised calibration

---

# AI Usage

AI tools were used during development as a **learning, debugging, and problem-solving assistant**.

AI assistance was used for:

* Understanding assessment requirements
* Exploring project structure
* Learning Pydantic concepts
* Debugging Python errors
* Discussing implementation approaches
* Reviewing edge-case handling

The resulting implementation was reviewed, adapted, and tested as part of the development process.

Examples of improvements made during development include:

* Adding fallback encoding support for recoverable input files
* Logging malformed files instead of silently ignoring them
* Improving duplicate handling
* Configuring pytest correctly for the project structure
* Adding documentation for engineering decisions

The final behavior was verified by running the complete processing pipeline against the provided dataset.

---

# New Skills Learned

## Pydantic

I learned how to use Pydantic models to validate and standardize structured data.

## Python Project Organization

I gained practical experience organizing a Python application into modules with clearly separated responsibilities.

## Data Pipeline Design

I gained experience designing an end-to-end data processing workflow:

```text
Raw Data
   ↓
Loading
   ↓
Normalization
   ↓
Validation
   ↓
Deduplication
   ↓
Scoring
   ↓
Ranking
   ↓
Reporting
```

---

# Additional Work Completed

Although not explicitly required, several additional improvements were implemented.

## Automated Tests

Tests were added for important parts of the pipeline, including:

* File loading
* Data normalization
* Duplicate removal
* Score calculation

These tests provide confidence that future changes do not unintentionally break existing functionality.

---

## Error Logging

Instead of silently ignoring problematic input files, the application records files that require review along with the reason they could not be processed.

This improves:

* Transparency
* Debuggability
* Data-quality monitoring
* Reproducibility

The pipeline can therefore continue processing valid data while preserving an audit trail of problematic inputs.

---

# Final Reflection

The assessment provided practical experience in building a small but complete data-processing system rather than focusing only on individual algorithms.

The main engineering lesson was that **real-world input data is rarely perfectly clean**. Designing the pipeline to handle inconsistent fields, duplicate records, encoding problems, malformed files, and missing values was therefore as important as implementing the core scoring logic.

The resulting system prioritizes **modularity, transparency, fault tolerance, and reproducibility**, while leaving clear opportunities for future improvements.
