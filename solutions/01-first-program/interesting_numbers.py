"""Generates a random number between 0 and 250,000.
Prints interesting information corresponding with that number."""
import random

number = random.randint(0, 250000)

if number < 6360:
    print(f"{number} is less than the amount of hours in a year, which is 6,360")
elif number < 60000:
    print(f"${number} is less than most people's household income in the United States! Most people make less than $60,000 per year! That's just a depressing figure") 
elif number < 110000:
    print(f"{number} is more than the median US income, but less than the population of Bridgetown, Barbados (around 110,000)")
else:
    print(f"{number} is bigger than all the other thresholds! Damn that's large!")