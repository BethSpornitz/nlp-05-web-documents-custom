# Clinical Fall Risk Research: Web Mining and NLP

Web Mining and Applied NLP | Project 05 | Beth Spornitz

## Overview

This project uses Python to extract and analyze information from an academic research paper about clinical fall-risk assessment.

The selected paper is **[An Interpretable Data-Driven Approach to Optimizing Clinical Fall Risk Assessment](https://arxiv.org/abs/2510.20714)**, available on arXiv.

The objective is to retrieve the paper's HTML abstract page, validate its structure, extract research metadata, and organize the information for analysis.

The project builds on the Extract, Validate, Transform, Load (EVTL) pipeline introduced in Module 4. Instead of working with JSON data from an API, this project processes semi-structured HTML documents.

The project also examines abstract length and the use of clinical terminology related to fall-risk assessment.

## Research Questions

This project explores three questions:

1. How can research metadata be reliably extracted from an HTML webpage?
2. How can abstract sentence count provide an additional measure of document length?
3. Which selected clinical terms appear most frequently in the research abstract?

## Tools and Methods

The project uses:

- **Python** for pipeline orchestration and processing.
- **Requests** for retrieving HTML documents.
- **BeautifulSoup** for parsing and inspecting HTML.
- **HTML selectors** for locating document content.
- **Validation checks** for confirming required elements.
- **Pandas** for structured data transformation.
- **Matplotlib** for visualizing clinical terminology frequencies.
- **CSV** for persistent output.
- **Logging** for execution records.
- **Ruff, ty, and pytest** for code verification.
- **Zensical and GitHub Pages** for published documentation.

### EVTL Pipeline

The pipeline implements four stages:

1. **Extract** – Retrieve the HTML page and save the original document.
2. **Validate** – Confirm that required HTML elements are present.
3. **Transform** – Extract research metadata and calculate derived fields.
4. **Load** – Save the structured information to a CSV file.

The Transform stage extracts the paper title, authors, abstract, subject categories, submission information, and arXiv identifier.

Derived fields include abstract word count, author count, and abstract sentence count.

### Technical Modification

The project extends the example transformation stage by adding an **abstract sentence count** field.

This provides an additional way to describe the length of a research abstract beyond its total word count.

The technical modification is evaluated against the original example before being applied to the selected clinical fall-risk paper.

### Custom Application

The custom application uses the same EVTL techniques to process the selected fall-risk research paper.

The analysis focuses on terminology associated with clinical fall-risk assessment. Selected terms are counted within the extracted abstract and presented in a bar chart.

The terminology analysis examines the abstract text, not individual patient records or clinical outcomes.

## Verification

The pipeline is checked through execution logs, generated output files, and the project's configured development tools.

Successful execution is indicated by:

```text
Pipeline executed successfully!
```

The example pipeline produces:

- `data/raw/case_raw.html` – original example HTML document.
- `data/processed/case_processed.csv` – structured example data.

The custom application uses separate output files:

- `data/raw/fall_risk_raw.html` – HTML from the selected fall-risk paper.
- `data/processed/fall_risk_processed.csv` – extracted and transformed research metadata.

The custom outputs are verified after implementation.

## Results and Visualization

*Results and the clinical terminology frequency chart will be added after the custom pipeline has been executed and its outputs verified.*

## Interpretation and Limitations

HTML documents are designed primarily for presentation in web browsers rather than structured data analysis.

Extracting information requires understanding the document's elements, attributes, and organization. Changes in webpage structure can affect validation and extraction results.

The validation stage helps identify missing or unexpected elements before the data is transformed.

Abstract word count and sentence count describe characteristics of the research text, but they do not measure the quality or clinical importance of the study.

Similarly, clinical terminology frequency identifies how often selected words or phrases appear in the abstract. Frequency alone does not establish the importance of a concept or the effectiveness of a fall-risk assessment method.

Because this project analyzes one paper's abstract, its findings are limited to that document and cannot be generalized to clinical practice.

## Documentation Index

- **Home** – This project report.
- [Project Instructions](project-instructions.md)
- [Glossary](glossary.md)

## Project Links

- [GitHub Repository](https://github.com/BethSpornitz/nlp-05-web-documents-custom)
- [Project Documentation](https://bethspornitz.github.io/nlp-05-web-documents-custom/)
- [Example Pipeline](https://github.com/BethSpornitz/nlp-05-web-documents-custom/blob/main/src/nlp/pipeline_web_html.py)
- [Python Source Files](https://github.com/BethSpornitz/nlp-05-web-documents-custom/tree/main/src/nlp)
- [Selected Research Paper](https://arxiv.org/abs/2510.20714)

## Project Resources

- [Project Instructions](project-instructions.md)
- [Professional Python Guide](https://denisecase.github.io/pro-analytics-02/)
- [Professional Python Project Explainer](https://pup-pack.github.io/professional-python-project-explainer/)
