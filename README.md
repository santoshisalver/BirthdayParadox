# Random Birthday Generator (Birthday Paradox)

This Python script simulates the famous **Birthday Paradox** by generating a list of 50 random birthdays and determining how many people share the same birthday.
The program generates each birthday as a "day of the year" (a number between 1 and 366) while accounting for leap years. 
## Features:
- Generates random birthdays for 50 people, each represented as the "day of the year" (1-366).
- Handles leap years, ensuring February has 29 days in leap years and 28 days in non-leap years.
- Correctly generates valid days for each month (28-31 days).
- Sorts the "days of the year" in ascending order.
- Calculates and prints how many people in the group share the same birthday, illustrating the **Birthday Paradox**.

## How It Works:
1. The script generates random birthdays for 50 people by randomly selecting a year, month, and day.
2. For each birthday, the script determines the corresponding "day of the year" (1-366).
3. The birthdays are then sorted in ascending order.
4. The script counts how many people share the same birthday and prints out the results.

## Example Output:
The program outputs:
- A sorted list of "days of the year" corresponding to the random birthdays.


