from signal_sifter.loader import load_json_files

def test_loader_reads_files():
    products = load_json_files("data")
    assert len(products) > 0