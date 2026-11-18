"""Create a terminology frequency chart from the processed fall-risk abstract."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    """Read the processed CSV and save a clinical terminology bar chart."""
    csv_path = Path("data/processed/fall_risk_processed.csv")
    output_path = Path("docs/images/fall_risk_term_frequencies.png")

    df = pd.read_csv(csv_path)
    if len(df) != 1:
        raise ValueError("Expected exactly one processed paper.")

    row = df.iloc[0]

    terms = [
        "Fall risk",
        "Assessment",
        "Prediction",
        "Patient safety",
        "Prevention",
    ]

    columns = [
        "fall_risk_mentions",
        "assessment_mentions",
        "prediction_mentions",
        "patient_safety_mentions",
        "prevention_mentions",
    ]

    counts = [int(row[column]) for column in columns]

    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.barh(terms, counts)

    ax.invert_yaxis()
    ax.set_xlabel("Number of occurrences")
    ax.set_title("Selected Clinical Terms in a Fall-Risk Research Abstract")
    ax.set_xlim(0, max(counts) + 1)
    ax.bar_label(bars, padding=4)

    fig.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)

    print(f"Chart saved to: {output_path}")
    print(dict(zip(terms, counts, strict=True)))


if __name__ == "__main__":
    main()
