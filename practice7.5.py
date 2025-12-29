prompt = '\nPlease enter your age.'
prompt += "\nEnter 'quit' if you want to stop."
while True:
    visiter_age = input(prompt)
    if visiter_age == 'quit':
        break
    visiter_age = int(visiter_age)
    if visiter_age < 3:
        print(f"You are {visiter_age} ago,so your ticket is free.")
    elif visiter_age < 12:
        print(f"You are {visiter_age} ago,so your ticket is 10 dollor.")
    else:
        print(f"You are {visiter_age} ago,so your ticket is 15 dollor.")