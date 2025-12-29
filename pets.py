pets = ['dog','cat','goldfish','cat','rabbit','cat','dog']
now_pet = []
for pet in pets:
    if pet not in now_pet:
        now_pet.append(pet)
print(f"now_pet are {now_pet}")
while 'cat' in pets:
    pets.remove('cat')
print(pets)