# The Konditorei coffee shop sells coffee at $15.50 a pound plus the cost
# of shipping. Each order ships for $0.99 per pound + $4.50 fixed cost for
# overhead. Write a program that calculates the cost of an order.

COST_PER_POUND_COFFEE = 15.50
COST_PER_POUND_SHIPPING = 0.99
COST_PER_ORDER_OVERHEAD = 4.50

def main():
    lbs_coffee = float(input("Number of pounds of coffee: "))
    price_order = COST_PER_ORDER_OVERHEAD + \
        lbs_coffee * (COST_PER_POUND_COFFEE + COST_PER_POUND_SHIPPING)
    print("Price of order: ", price_order)

main()
