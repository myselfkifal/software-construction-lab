from typing import Any


def calculate_items_subtotal(order: dict[str, Any]) -> float:
    subtotal: float = 0.0

    for item in order["items"]:
        price: float = item["price"]
        quantity: int = item["qty"]

        if price <= 0:
            continue

        if quantity <= 0:
            continue

        subtotal = subtotal + price * quantity

    return subtotal


def calculate_member_discount(
    subtotal: float, is_member: bool
) -> float:
    if not is_member:
        return 0.0

    if subtotal > 100:
        return subtotal * 0.2

    if subtotal > 50:
        return subtotal * 0.1

    return 0.0


def calculate_shipping_cost(country: str) -> float:
    if country == "PK":
        return 5.0

    if country == "US":
        return 15.0

    return 25.0


def calculate_order_total(order: dict[str, Any]) -> float:
    subtotal = calculate_items_subtotal(order)
    discount = calculate_member_discount(subtotal, order["member"])
    shipping_cost = calculate_shipping_cost(order["country"])

    total = subtotal - discount
    total = total + shipping_cost

    print("Total: " + str(total))
    return total