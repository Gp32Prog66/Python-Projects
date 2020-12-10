#coffee Calculations

#module
import math


numDrinks = int(input("Enter the amount of caffeine in milliligrams "))

caffiene = 10000;

#calculations
drinkInput = caffiene / numDrinks;

print("This is how many drinks you need to drink in order to die");

print(math.ceil(drinkInput));
