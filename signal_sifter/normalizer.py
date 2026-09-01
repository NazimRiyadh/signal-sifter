from datetime import datetime
from .models import Product

def clean_number(value):
    if value is None:
        return 0

    if isinstance(value, str):
        value = value.replace(",", "").strip()

    try:
        return int(float(value))

    except:
        return 0

def clean_rating(value):

    if value is None:
        return 0.0

    try:
        return float(value)

    except:
        return 0.0

def parse_date(value):

    if value is None:
        return None

    try:
        value = str(value)

        if "T" in value:
            value = value.replace("Z", "")

            return datetime.fromisoformat(value).date()

        return datetime.strptime(
            value,
            "%Y-%m-%d"
        ).date()

    except:
        return None


def normalize(raw):

    stats = raw.get("stats", {})


    name = (
        raw.get("title")
        or raw.get("name")
        or raw.get("product_name")
        or "Unknown"
    )


    installs = (
        raw.get("installs")
        or raw.get("install_count")
        or stats.get("installs")
    )


    rating = (
        raw.get("rating")
        or raw.get("stars")
        or raw.get("score")
        or stats.get("rating")
    )


    reviews = (
        raw.get("reviews")
        or raw.get("review_count")
        or stats.get("reviews")
    )


    updated = (
        raw.get("last_updated")
        or raw.get("updated_at")
    )


    return Product(
        id=raw.get("id"),
        name=name,
        url=raw.get("url"),
        installs=clean_number(installs),
        rating=clean_rating(rating),
        reviews=clean_number(reviews),
        last_updated=parse_date(updated),
        category=raw.get("category")
    )