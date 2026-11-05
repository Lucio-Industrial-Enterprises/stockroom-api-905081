"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Return a nonnegative quantity, raising ValueError for negatives."""
    quantity = int(value.strip())
    if quantity < 0:
        raise ValueError("quantity must be nonnegative")
    return quantity
