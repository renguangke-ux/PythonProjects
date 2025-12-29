alien_0 = {"x_position":0,"y_position":25,"speed":"medium"}
print(f"original position: {alien_0["x_position"]}")
#move alien to right
#make sure how far the alien move to right by the speed now
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3
alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"new position:{alien_0['x_position']}")
del alien_0["speed"]
print(alien_0)