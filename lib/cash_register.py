#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []

  def add_item(self, title, price, quantity=1):
    self.items.extend([title] * quantity)
    self.total += price * quantity

  def apply_discount(self):
        # If there is a discount, apply it to the total
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

  def void_last_transaction(self):
    if self.items:
      last_item = self.items.pop()
      self.total -= last_item['price']
    if not sel.items:
      self.total = 0

  