"""src/nlp/config_fall_risk.py - Clinical Fall Risk Project Configuration.

Author: Beth Spornitz
Date: 2026-11

Purpose

  Store configuration values for the clinical fall-risk
  HTML web document EVTL pipeline.

Source

  arXiv: An Interpretable Data-Driven Approach to
  Optimizing Clinical Fall Risk Assessment (2510.20714).

Analytical Questions

- What information can be extracted from the research paper's HTML page?
- How can the extracted metadata and abstract be analyzed?
- Where should the raw and processed data be stored?
"""

from pathlib import Path

# ============================================================
# SOURCE CONFIGURATION
# ============================================================

PAGE_URL: str = "https://arxiv.org/abs/2510.20714"

HTTP_REQUEST_HEADERS: dict = {
    "User-Agent": "Mozilla/5.0 (educational-use; web-mining-course)"
}

# ============================================================
# PATH CONFIGURATION
# ============================================================

ROOT_PATH: Path = Path.cwd()
DATA_PATH: Path = ROOT_PATH / "data"
RAW_PATH: Path = DATA_PATH / "raw"
PROCESSED_PATH: Path = DATA_PATH / "processed"

RAW_HTML_PATH: Path = RAW_PATH / "fall_risk_raw.html"
PROCESSED_CSV_PATH: Path = PROCESSED_PATH / "fall_risk_processed.csv"
