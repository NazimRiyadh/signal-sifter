from datetime import date
from pydantic import BaseModel


class Product(BaseModel):
    id: str | None = None
    name: str
    url: str | None = None
    installs: int = 0
    rating: float = 0.0
    reviews: int = 0
    last_updated: date | None = None
    category: str | None = None
    score: float = 0.0