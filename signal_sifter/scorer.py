from datetime import date


REFERENCE_DATE = date(2026, 9, 1)


def calculate_score(product):

    # Check freshness

    if product.last_updated:

        age = (
            REFERENCE_DATE
            -
            product.last_updated
        ).days


        if age > 90:
            return 0.0


    install_points = min(
        product.installs / 1000,
        50
    )


    rating_points = (
        product.rating - 3.0
    ) * 10


    review_points = min(
        product.reviews / 100,
        20
    )


    score = (
        install_points
        +
        rating_points
        +
        review_points
    )


    return round(score, 2)