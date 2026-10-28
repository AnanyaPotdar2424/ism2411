# Self-Assessment & Reflection
# 1-           
# The first bug I spotted was a parameter ordering mismatch in function calls. 
# I found it by reading the traceback and matching it up with the function signature. 
# This shows my debugging instincts rely heavily on tracking data flow from error logs.
# 2- 
# apply_discount(price, tier) takes a numerical price (float/int) and a string representing a membership tier ("gold", "silver", "bronze", "none").
# It computes and returns the reduced price based on tiered percentage discounts. 
# A colleague could easily use it without reading the body because the parameter names are intuitive.
# 3-
# Used AI to assist with structuring code, debugging Exercise 5, and formatting the script. 
# Reflection on AI use: Using AI helped speed up the syntax formatting and provided clarity on the loop bounds.
# But, building out the logic step-by-step still required understanding how functions and return values interact.


# Exercise 1
def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")


# Exercise 2
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver": 
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price 

original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")


# Exercise 3
def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")


# Exercise 4
orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")


# Exercise 5
# Fixed version of broken_sales.py logic
# Fix notes: Corrected accumulator assignment, added missing loop colon, and fixed while loop range bounds.
def fixed_sales_report():
    sales = [120, 80, 250, 175, 90]

    total = 0
    for sale in sales:
        total += sale
    print(f"Fixed Sales Total: ${total}")

    count = 0
    for sale in sales:
        count += 1
    print(f"Fixed Sales Count: {count}")

    i = 0
    while i < len(sales):
        print(f"Sale item {i}: ${sales[i]}")
        i += 1

fixed_sales_report()


# Exercise 6
x = 100 # global x

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # Prints 100 (references global x)
print(double_it()) # Prints 1998 (computes inside local function scope)
print(x)           # Prints 100 (global x remains unchanged)

# Explanation of Scope:
# Python uses lexical scoping where variables assigned inside a function block are local to that 
# function and do not overwrite or alter variables in the outer global scope unless explicitly declared.