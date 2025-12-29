today_is_opposite_day = False

#Set say_it_is_opposite_day based on today_is_opposite_day:
if today_is_opposite_day == True:
    say_it_is_oppsite_day = True
else:
    say_it_is_oppsite_day = False

#If it is opposite day, toggle say_it_is_opposite_day:
if today_is_opposite_day == True:
    say_it_is_oppsite_day = not say_it_is_oppsite_day

#Say what day it is:
if say_it_is_oppsite_day == True:
    print('Today is Opposite day')
else:
    print('Today is not opposite Day.')