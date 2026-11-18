# nlp-05-web-documents-custom

[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](pyproject.toml)
[![CI](https://github.com/BethSpornitz/nlp-05-web-documents-custom/actions/workflows/ci-python-zensical.yml/badge.svg)](https://github.com/BethSpornitz/nlp-05-web-documents-custom/actions/workflows/ci-python-zensical.yml)
[![Documentation](https://img.shields.io/badge/docs-site-blue?logo=github)](https://bethspornitz.github.io/nlp-05-web-documents-custom/)

[![uv managed](https://img.shields.io/badge/uv-managed-DE5FE9)](https://docs.astral.sh/uv/)
[![ty type checked](https://img.shields.io/badge/ty-type_checked-2F80ED)](https://docs.astral.sh/ty/)
[![Zensical docs](https://img.shields.io/badge/Zensical-docs-purple)](https://zensical.org/)
[![MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

> Extract and analyze clinical fall risk research from HTML web documents using Python.

## Project Overview

**Author:** Beth Spornitz
**Date:** November 2026
**Course:** Web Mining and Applied NLP — Module 5

This project demonstrates how Python can be used to retrieve information from an academic research paper published on arXiv.

The project focuses on clinical fall risk assessment, a topic related to nursing quality and patient safety.

It uses an Extract, Validate, Transform, Load (EVTL) pipeline to retrieve the paper's HTML webpage, verify its structure, extract meaningful information, and save the results for analysis.

The project builds on the EVTL approach introduced in Module 4, applying it to HTML webpages instead of JSON API responses.

The project is configured in [pyproject.toml](pyproject.toml).

## Data

The custom project analyzes the arXiv paper [An Interpretable Data-Driven Approach to Optimizing Clinical Fall Risk Assessment](https://arxiv.org/abs/2510.20714).

The paper examines approaches to improving clinical fall risk assessment.

The webpage provides information including:

- Paper title
- Authors
- Abstract
- Subject categories
- Submission information
- arXiv identifier

The project preserves the original HTML document and organizes extracted information into a structured CSV dataset.

The instructor's original example, [Agents of Chaos](https://arxiv.org/abs/2602.20021), is retained as a reference for understanding and testing the pipeline.

## Approach

The project uses Python to extract and process information from an HTML webpage.

The pipeline follows four stages:

1. **Extract** — Retrieve the HTML webpage using Requests.
2. **Validate** — Check that the required HTML elements are present.
3. **Transform** — Use BeautifulSoup to extract information and Pandas to organize it into a DataFrame.
4. **Load** — Save the structured information to a CSV file.

The project extracts bibliographic information and calculates additional measures, including:

- Abstract word count
- Author count
- Abstract sentence count

The project also examines the frequency of selected clinical terms in the abstract and presents the results in a visualization.

This analysis provides a simple example of how web mining and text analysis can be applied to healthcare research.

### Project Components

- [pyproject.toml](pyproject.toml) — Project identity, dependencies, and tool configuration.
- [src/nlp/pipeline_web_html.py](src/nlp/pipeline_web_html.py) — Main EVTL pipeline.
- [src/nlp/config.py](src/nlp/config.py) — Example webpage and file path configuration.
- [src/nlp/stage01_extract.py](src/nlp/stage01_extract.py) — Retrieve HTML.
- [src/nlp/stage02_validate.py](src/nlp/stage02_validate.py) — Validate HTML structure.
- [src/nlp/stage03_transform.py](src/nlp/stage03_transform.py) — Extract and transform data.
- [src/nlp/stage04_load.py](src/nlp/stage04_load.py) — Save processed results.
- [tests/](tests/) — Automated tests.
- [.github/workflows/](.github/workflows/) — Automated testing and documentation deployment.
- [docs/](docs/) — Project documentation.
- [zensical.toml](zensical.toml) — Documentation configuration.

The original Python stages are preserved as examples. The custom application uses separate processing files to adapt the pipeline to the selected fall-risk paper.

### Custom Application Files

- `src/nlp/config_fall_risk.py` — Custom arXiv URL and output paths.
- `src/nlp/pipeline_fall_risk.py` — Custom EVTL pipeline.
- `src/nlp/stage01_extract_fall_risk.py` — Retrieve the selected paper's HTML.
- `src/nlp/stage02_validate_fall_risk.py` — Validate required HTML elements.
- `src/nlp/stage03_transform_fall_risk.py` — Extract metadata and calculate derived fields and clinical terminology frequencies.
- `src/nlp/stage04_load_fall_risk.py` — Save the processed CSV.
- `src/nlp/visualize_fall_risk.py` — Generate the clinical terminology frequency chart.

## Run the Project

Follow the [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/) to set up the development environment.

From a VS Code terminal in the project root, run the original example:

```shell
uv run python -m nlp.pipeline_web_html
```

The custom pipeline uses the same EVTL approach with the selected clinical fall-risk paper. It uses separate configuration and processing stages to preserve the original example.

Run the custom fall-risk pipeline:

```powershell
uv run python -m nlp.pipeline_fall_risk
```

This retrieves the paper's HTML page, validates the required elements, extracts research metadata, calculates derived fields, and saves the results to `data/processed/fall_risk_processed.csv`.

Generate the clinical terminology frequency chart:

```powershell
uv run python -m nlp.visualize_fall_risk
```

The visualization script reads the processed CSV and saves the chart to `docs/images/fall_risk_term_frequencies.png`.

The custom pipeline and visualization should be run in that order.

## Results

The pipeline produces structured information extracted from the academic paper's HTML webpage.

The original example generates the following artifacts:

- `project.log` — Pipeline execution log.
- `data/raw/case_raw.html` — Original HTML document.
- `data/processed/case_processed.csv` — Extracted and transformed data.

Successful execution displays:

```text
========================
Pipeline executed successfully!
========================
```

### Custom Fall-Risk Analysis Results

The custom EVTL pipeline successfully retrieved and processed the HTML abstract page for [An Interpretable Data-Driven Approach to Optimizing Clinical Fall Risk Assessment](https://arxiv.org/abs/2510.20714).

All five required HTML elements were validated, and the extracted information was saved in a Pandas DataFrame containing **1 row and 14 columns**.

The analysis produced the following results:

| Measure | Result |
|---|---:|
| Authors | 5 |
| Abstract words | 190 |
| Estimated sentences | 8 |
| Fall risk mentions | 4 |
| Assessment mentions | 3 |
| Prediction mentions | 1 |
| Patient safety mentions | 1 |
| Prevention mentions | 1 |

The terms **fall risk** and **assessment** appeared most frequently among the five selected clinical terms. These results demonstrate how BeautifulSoup and Python can extract research information from an HTML document and transform it into structured data for analysis.

The terminology frequencies were visualized using Matplotlib. The chart and a more detailed discussion of the methods, results, interpretation, and limitations are available in the [project report](https://bethspornitz.github.io/nlp-05-web-documents-custom/).

The analysis is limited to one research abstract, and terminology frequency does not establish clinical significance.

## Verification

Run the automated tests:

```shell
uv run python -m pytest
```

The project uses validation, logging, automated tests, and GitHub Actions to support reproducible results.

## Project Documentation

The [hosted documentation site](https://bethspornitz.github.io/nlp-05-web-documents-custom/) is published using Zensical and GitHub Pages.

The documentation presents the selected research paper, extraction methods, validation, transformations, results, visualization, interpretation, and limitations.

## CI/CD and GitHub Actions

The project includes continuous integration and deployment workflows to check project files and publish documentation.

- [CI: Python and Documentation Checks](https://github.com/BethSpornitz/nlp-05-web-documents-custom/actions/workflows/ci-python-zensical.yml)
- [CD: Documentation Deployment](https://github.com/BethSpornitz/nlp-05-web-documents-custom/actions/workflows/deploy-zensical.yml)

## Developer Reference

Follow the [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/) for detailed instructions and troubleshooting.

### Initialize and Update the Python Environment

From a VS Code terminal in the project root:

```shell
uvx pup-clean --delete
uv self update
uv python pin 3.14
uv python install
uv lock --upgrade
uv sync
uv audit
```

### Set Up and Run Git Hooks

```shell
uvx prek install --force
uvx prek update --freeze --cooldown-days 7

git add -A
uvx prek run --all-files
# repeat if changes were made
uvx prek run --all-files
```

### Run Common Chores

```shell
uv run ruff check . --fix
uv run ruff format .

uv run ty check
uv run python -m pytest
uv run python -m zensical build
```

### Git Add-Commit-Push to GitHub

After making useful changes, save the work to GitHub.

```shell
git add -A
git commit -m "describe your changes in quotes"
git push -u origin main
```

## Developer Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through previous commands.
- Use `CTRL+f` to find text within a file.

## Developer Tools

This project uses professional Python tools for development, testing, documentation, and code quality.

- [uv](https://docs.astral.sh/uv/) — Python environments and dependencies.
- [Ruff](https://docs.astral.sh/ruff/) — Python linting and formatting, configured in [.ruff.toml](.ruff.toml).
- [ty](https://docs.astral.sh/ty/) — Python type checking.
- [pytest](https://docs.pytest.org/) — Automated Python testing, configured in [.pytest.toml](.pytest.toml).
- [prek](https://prek.j178.dev/) — Git hooks and automated checks, configured in [prek.toml](prek.toml).
- [Zensical](https://zensical.org/) — Project documentation, configured in [zensical.toml](zensical.toml).

## Links

- [Hosted Documentation](https://bethspornitz.github.io/nlp-05-web-documents-custom/)
- [Original Example Repository](https://github.com/denisecase/nlp-05-web-documents)
- [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/)
- [Citation](CITATION.cff)
- [License](LICENSE)
