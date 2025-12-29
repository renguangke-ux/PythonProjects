sandwich_orders = ['blt sandwich','pastrami','club sandwich','sub','pastrami','panini','veggie sandwich','pastrami','turkey sandwich']
finished_sandwiches = []
print(sandwich_orders)
solden_sandwich = 'pastrami'
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your  {sandwich.title()}.")
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)
