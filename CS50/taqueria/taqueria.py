menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    price = float(0.00)
    while True:
        try:
            order = input("Item: ").title()
            price = price + find_price(order)
            print("Total: ${:.2f}".format(price))
        except EOFError:
            print()
            break
        except TypeError:
            pass


def find_price(sel):
    for item in menu:
        if item == sel:
            return menu[item]

main()

