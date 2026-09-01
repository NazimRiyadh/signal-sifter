from signal_sifter.loader import load_json_files
from signal_sifter.normalizer import normalize

raw_products = load_json_files("data")
product = normalize(raw_products[0])

print(product)