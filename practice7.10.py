prompt = "\nIf you could visit one place in the world, where would you go?"
prompt += "\nEnter 'quit' when you finished."
favorite_places = {}
response = True
while response:
    name = input("What is your name?")
    favorite_place = input("Where are you go?")
    favorite_places[name] = favorite_place
    repeat = input("continue?(yes/no)")
    if repeat == 'no':
        response = False
    
for name, favorite_place in favorite_places.items():
    print(f"{name.title()}'s favorite place is {favorite_place.title()}.")

