def rate_to_price_level(rate: int) -> str:
    """Convert a 0-3 quality rating to a price level string."""
    if rate <= 1:
        return "budget"
    if rate == 2:
        return "mid_range"
    return "luxury"
