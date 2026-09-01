from signal_sifter.loader import load_json_files


products = load_json_files("data")


print("Total files:", len(products))


print(products[0])