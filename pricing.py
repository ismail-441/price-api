def final_price(base_price: float, discount_percent: float, tax_percent: float) -> float:
    """Takes a product's base price, applies a discount, then applies tax."""
    discounted = base_price - (base_price * discount_percent / 100)
    final = discounted + (discounted * tax_percent / 100)
    return round(final, 2)


if __name__ == "__main__":
    price = final_price(base_price=1200, discount_percent=20, tax_percent=18)
    print(f"Final price: ₹{price}")