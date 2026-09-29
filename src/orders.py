def calculate_items_subtotal(order):
    subtotal = 0
    for item in order["items"]:
        price = item["price"]
        quantity = item["qty"]
        if price <= 0:
            continue
        if quantity <= 0:
            continue

        subtotal = subtotal + price * quantity
    return subtotal
def calculate_member_discount(subtotal, is_member):
    if not is_member:
        return 0

    if subtotal > 100:
        return subtotal * 0.2

    if subtotal > 50:
        return subtotal * 0.1

    return 0
def calculate_shipping_cost(country):
    if country == "PK":
        return 5

    if country == "US":
        return 15
    return 25
def calculate_order_total(order):
    subtotal = calculate_items_subtotal(order)
    discount = calculate_member_discount(subtotal, order["member"])
    shipping_cost = calculate_shipping_cost(order["country"])

    total = subtotal - discount
    total = total + shipping_cost

    print("Total: " + str(total))
    return total