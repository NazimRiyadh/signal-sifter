from signal_sifter.models import Product
from signal_sifter.deduplicator import deduplicate


def test_duplicate_products_removed():

    products = [
        Product(
            name="Cache Rocket",
            installs=1000
        ),

        Product(
            name="cache rocket",
            installs=2000
        )
    ]

    result = deduplicate(products)
    assert len(result) == 1