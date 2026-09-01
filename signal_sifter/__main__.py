import argparse

from .loader import load_json_files
from .normalizer import normalize
from .deduplicator import deduplicate
from .scorer import calculate_score
from .reporter import write_reports


def main():
    print("Signal Sifter started")

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input",
        default="data",
    )

    parser.add_argument(
        "--output",
        default="report",
    )

    args = parser.parse_args()

    # 1. Load JSON files
    raw_products = load_json_files(args.input)

    print(
        "Raw files loaded:",
        len(raw_products),
    )

    # 2. Normalize data
    products = [
        normalize(item)
        for item in raw_products
    ]

    print(
        "Products after normalization:",
        len(products),
    )

    # 3. Remove duplicates
    products = deduplicate(products)

    print(
        "After deduplication:",
        len(products),
    )

    # 4. Calculate scores
    for product in products:
        product.score = calculate_score(product)

    print("Scoring completed")

    # 5. Sort by highest score
    products.sort(
        key=lambda x: x.score,
        reverse=True,
    )

    if products:
        print(
            "Highest score:",
            products[0].score,
        )

        print(
            "Highest scoring product:",
            products[0].name,
        )

    # 6. Generate reports
    print("Writing reports...")

    write_reports(
        products,
        args.output,
    )

    print("Finished successfully")


if __name__ == "__main__":
    main()