import json
from pathlib import Path

def write_reports(products, output_folder):
    folder = Path(output_folder)

    folder.mkdir(exist_ok=True)

    json_report = []
    text_lines = []

    text_lines.append("Signal Sifter Top Products")
    text_lines.append("")

    for rank, product in enumerate(products[:10], start=1):
        item = {
            "rank": rank,
            "name": product.name,
            "score": product.score,
            "installs": product.installs,
            "rating": product.rating,
            "reviews": product.reviews,
            "last_updated": str(product.last_updated),
        }

        json_report.append(item)

        text_lines.extend([
            f"{rank}. {product.name}",
            f"Score: {product.score}",
            f"Installs: {product.installs}",
            f"Rating: {product.rating}",
            f"Reviews: {product.reviews}",
            "",
        ])

    with open(
        folder / "report.json",
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            json_report,
            f,
            indent=4,
        )

    with open(
        folder / "report.txt",
        "w",
        encoding="utf-8",
    ) as f:
        f.write(
            "\n".join(text_lines)
        )