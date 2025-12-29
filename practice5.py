#5.1-5.5 alien color
alien_color = "red"
if alien_color == "green":
    print("The alien's color is green,so you gain 5")
elif alien_color == "yellow":
    print("The alien's color is yellow,so you gain 10")
else:
    print("The alien's color is red,so you gain 15")
#5.6 stages of life
age = 10
if age < 2:
    print(f"You are {age} old,you are baby.")
elif age <4:
    print(f"You are {age} old,you are infant.")
elif age <18:
    print(f"You are {age} old,you are teenage.")
elif age <65:
    print(f"You are {age} old,you are adult.")
else:
    print(f"You are {age} old,you are old man.")
#5.7 favorite fruits 
favorite_fruits = ["apple","banana","orange","peach","watermelon","grape"]
if "apple" in favorite_fruits:
    print("You really like apple")
if "banana" in favorite_fruits:
    print("You really like banana")
if "papaya" in favorite_fruits:
    print("You really like papaya")