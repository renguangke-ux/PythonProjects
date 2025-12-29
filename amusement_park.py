age = 105
if age < 4:
   price = 0
elif age < 18 or age>65:
    price = 25
elif age < 65:
    price = 40
print(f"Your admission cost is ${price}.")