# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 07:10:21 2024

@author: santo
"""

import random  # Importing the random module to generate random numbers
import datetime  # Importing the datetime module to work with dates

birthday = []  # Initialize an empty list to store the "day of the year" values for the birthdays

# Generate 50 random birthdays
for i in range(50):
    # Randomly select a year between 1902 and 2024 (oldest person  ever lived was 122 years old)
    year = random.randint(1902, 2024)
    
    # Check if the selected year is a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = 1  # Leap year
    else:
        leap = 0  # Not a leap year
    
    # Randomly choose a month between 1 (January) and 12 (December)
    month = random.randint(1, 12)
    
    # Handle the number of days in each month, considering leap years for February
    if month == 2:  # February
        if leap == 1:  # Leap year
            day = random.randint(1, 29)  # February has 29 days in a leap year
        else:  # Non-leap year
            day = random.randint(1, 28)  # February has 28 days in a non-leap year
    elif month in [4, 6, 9, 11]:  # Months with 30 days (April, June, September, November)
        day = random.randint(1, 30)
    else:  # Months with 31 days (January, March, May, July, August, October, December)
        day = random.randint(1, 31)
    
    # Create a date object using the randomly selected year, month, and day
    dd = datetime.date(year, month, day)
    
    # Get the day of the year (1-366) for the selected date
    day_of_year = dd.timetuple().tm_yday
    
    # Append the day of the year to the 'birthday' list
    birthday.append(day_of_year)

# Sort the 'birthday' list to arrange the days in ascending order
birthday.sort()

# Print each day of the year in the sorted 'birthday' list
for day in birthday:
    print(day)
