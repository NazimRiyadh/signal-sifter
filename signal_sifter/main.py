import json


with open("data/listing_001.json", "r") as file:
    product = json.load(file)


print(product["title"])
print(product["installs"])
print(product["rating"])