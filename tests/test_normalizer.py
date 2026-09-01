from signal_sifter.normalizer import normalize

def test_normalizer_converts_fields():
    raw = {
        "title": "Test Plugin",
        "installs": "18,300",
        "rating": "4.5",
        "reviews": "500"
    }

    product = normalize(raw)

    assert product.name == "Test Plugin"
    assert product.installs == 18300
    assert product.rating == 4.5
    assert product.reviews == 500