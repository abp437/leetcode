from item import Item
from phone import Phone

phone = Item("Phone", 75.02, 3)

# Calls the setter method
phone.name = "New Phone"

# Doesn't do anything
phone.__name = "Akshay's Phone"

print(type(phone))
print(type(phone.price))
print(type(phone.quantity))
print(type(phone.name))
print(phone.price)
print(phone.calculate_price())

print("hello".upper())
print("hello".isalnum())

# Class variables
print(Item.discount_rate)
phone.apply_discount()
print(phone.price)

table = Item("Table", 22321, 5)
# This change doesn't apply for the full class, it applies only to this instance
# Subsequent instances will pick up values from the class variable itself
table.discount_rate = 0.3
table.apply_discount()
print(table.price)

chair = Item("Chair", 383, 8)
chair.apply_discount()
print(chair.price)

print(chair + table)

# This will call the __repr__
print(Item.all)

for inst in Item.all:
    # This will call the __str__
    print(inst)

Item.instantiate_from_csv()
# This will call the __repr__
print(Item.all)

print(Item.is_int("2"))

# Testing type & value validations
# testing = Item("TV", -23, -35)
# print(testing.calculate_price())

phone = Phone(23.44, 45)
print(phone)
