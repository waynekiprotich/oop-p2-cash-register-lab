
class CashRegister:
    def __init__(self, discount=0):
        if isinstance(discount, int) and 0 <= discount <= 100:
            self.discount = discount
        else:
            print("Not valid discount")
            self.discount = 0

        self.total = 0
        self.items = []
        self.previous_transactions = []
# add items
    def add_item(self, item, price, quantity=1):   
        self.total += price * quantity

        count = 0
        while count < quantity:
            self.items.append(item)
            count += 1

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:  
            print("There is no discount to apply.")
            return

        discount_amount = (self.discount / 100) * self.total
        self.total -= discount_amount

        print(f"After the discount, the total is {self.total}")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last = self.previous_transactions.pop()

        self.total -= last["price"] * last["quantity"]

        count = last["quantity"]

        while count > 0 and last["item"] in self.items:
            self.items.remove(last["item"])
            count -= 1