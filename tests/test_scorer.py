from datetime import date

from signal_sifter.models import Product
from signal_sifter.scorer import calculate_score

def test_product_score():

    product = Product(

        name="Test Plugin",
        installs=10000,
        rating=4.5,
        reviews=500,
        last_updated=date(2026, 8, 1)

    )

    score = calculate_score(product)
    assert score > 0