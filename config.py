# Contains configuration constants (Base URL, CSS selectors, etc.)

#TODO

# For Scrapping Venue

# BASE_URL = "https://www.theknot.com/marketplace/wedding-reception-venues-atlanta-ga"
# CSS_SELECTOR = "[class^='info-container']"
# REQUIRED_KEYS = [
#     "name",
#     "price",
#     "location",
#     "capacity",
#     "rating",
#     "reviews",
#     "description",
# ]


# For Scrapping Pharma website


BASE_URL = "https://www.dvago.pk/cat/multivitamins"
CSS_SELECTOR = "[class^='ProductCard_productContent']"
REQUIRED_KEYS = [
    "name",
    "regular_price",
    "sale_price"
]