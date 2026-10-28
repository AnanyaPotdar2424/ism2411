# Reflection 1:
# One thing that surprised me was how easy it is to organize and change items in a Python list. 
# I didn't realize that negative numbers could be used to access items from the end of a list. 
# I also found slicing interesting because it allows you to access multiple items at once. 
# Overall, I think lists make organizing information much easier.

# Reflection 2:
# When I worked at a farmers market, we had to keep track of different products and sales throughout the day.
# I think using Python lists would have made it easier to organize everything and update our inventory.
# For example, we could add new products, remove items that sold out, and keep track of what was available.
# This would have saved us time and made it easier to manage everything throughout the day.


# Exercise 1
inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(inventory)
print(len(inventory))

# Exercise 2
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

# Exercise 3

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# Exercise 5
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples cannot be changed after they are created.")
    print("This is useful for coordinates because it keeps them the same.")

print(coords)

# Exercise 6
sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))

# Exercise 7
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    new_price = round(price * 0.90, 2)
    discounted.append(new_price)

print("Original prices:", prices)
print("Discounted prices:", discounted)

# Exercise 8
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print("High sales:", high_sales)
print("Count:", len(high_sales))
print("Average:", sum(high_sales) / len(high_sales))
