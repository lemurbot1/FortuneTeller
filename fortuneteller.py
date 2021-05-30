#The purpose of this code is to act as a fortune teller to predict
#where the user will be living in the future.

import random

#determines the color of the home
def HomeColor(color):
    colorpicker = str()
    colorpicker = random.choice(color)
    return colorpicker

#determines the living situation
def HomeType(home):
    living_home = str()
    living_home = random.choice(home)
    return living_home

#determines the location
def NewTown(city):
    location = str()
    location = random.choice(city)
    return location

def main():
    #variables
    color = str()
    home = str()
    city = str()

    picked_color = str()
    picked_home = str()
    picked_city = str()
    
    #lists of colors, homes, and cities to be used for predictions
    color = ["Pink", "White", "Gray", "Blue", "Rainbow", "Brown", "Red"]
    home = ["House", "Mansion", "Apartment", "Penthouse", "Trailer", "Condo"]
    city = ["Warren", "Mexico City", "Beijing", "Portland", "Manhattan", "Tokyo"]

    #values return here
    picked_color = HomeColor(color)
    picked_home = HomeType(home)
    picked_city = NewTown(city)

    #new values assigned to variables plugged into print statement
    #user is given their fortune
    print("My crystal ball sees your future... It shows you living in a", picked_color, picked_home, "in", picked_city, "!")

main()
