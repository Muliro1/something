#shopping cart class
class ShoppingCart(object):
  #constructor to initialise the dict and the value of total
  def __init__(self, total = 0):
    self.total = total
    self.items = {}
    #method to add items to the shopping cart
  def add_item(self, item_name, quantity, price):
    self.total += (price * quantity)
    self.items.update({item_name: quantity})
    #method to remove items from the shopping listc
  def remove_item(self, item_name, quantity, price):
    if quantity > self.items[item_name]:
      items_cost = self.items[item_name] * price
      self.total -= items_cost
      del self.items[item_name]
    else:
      cost = quantity * price
      self.total -= cost
      self.items[item_name] -= quantity
  def checkout(self, cash_paid):
    if cash_paid < self.total:
      return 'Cash paid not enough'
    else:
      balance = cash_paid - self.total
      return balance
      
    
    
#shop class that inherits from ShoppingCart    
class Shop(ShoppingCart):
  def __init__(self):
    self.quantity = 100
  def remove_item(self):
    self.quantity -= 1