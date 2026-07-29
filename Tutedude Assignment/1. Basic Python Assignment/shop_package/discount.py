def apply_discount(price, percent):
    discounted_price = price - (price * percent / 100)
    return discounted_price

def flat_discount(price):
    discounted_price = price - 50
    return discounted_price
