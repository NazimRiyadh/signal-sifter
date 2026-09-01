def normalize_name(name):

    return " ".join(
        name.lower().split()
    )

def deduplicate(products):

    unique_products = {}

    for product in products:
        key = normalize_name(product.name)

        if key not in unique_products:
            unique_products[key] = product

    return list(unique_products.values())