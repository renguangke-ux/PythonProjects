prompt = "Please input pizza topping."
prompt +="\n Please input 'quit' to stop."
toppings = ''
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    print(f'{topping.title()} will be added, do you want another?')
    if toppings =='':
        toppings = topping.title()
    else:
        toppings += f",{topping.title()}"
print(f'{toppings} are your finally ordering.')