from signal_sifter.loader import load_json_files
from signal_sifter.normalizer import normalize
from signal_sifter.scorer import calculate_score

raw_products = load_json_files("data")

product = normalize(raw_products[0])

score = calculate_score(product)

print(product.name)
print(score)