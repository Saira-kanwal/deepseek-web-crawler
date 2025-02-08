# Defines the Product data model using Pydantic

from pydantic import BaseModel


class Product(BaseModel):
    """
    Represents the data structure of a product.
    """
# TODO

    # For Scrapping Venue


    # name: str
    # location: str
    # price: str
    # capacity: str
    # rating: float
    # reviews: int
    # description: str

    # For Scrapping Pharma website

    name: str
    regular_price: str
    sale_price: str

