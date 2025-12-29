pet1 = {
    'type':'cat',
    'owner':'shi',
}
pet2 = {
    'type':'dog',
    'owner':'li',
}
pet3 ={
    'type':'bird',
    'owner':'wang'
}
pets = [pet1,pet2,pet3]

for pet in pets:
    pet_type = pet['type']
    pet_owner = pet['owner']
    print(f"This pet is a {pet_type.title()}, its owner is {pet_owner.title()}.")
    