from signal_sifter.loader import load_json_files
from signal_sifter.normalizer import normalize
from signal_sifter.deduplicator import deduplicate

raw_products = load_json_files("data")

products = [
    normalize(item)
    for item in raw_products
]

print("Before:", len(products))

unique_products = deduplicate(products)

print("After:", len(unique_products))

for product in unique_products:
    print(product.name)