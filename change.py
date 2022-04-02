# Author: Derrick Macaranas
# GitHub username: DerrickMac
# Date: 3/31/2022
# Description: Write a program that asks the user for a (integer) number of cents, from 0 to 99,
#              and outputs how many of each type of coin would represent that
#              amount with the fewest total number of coins.

print("Please enter an amount in cents less than a dollar.")
cents = int(input())
print("Your change will be:")
remainder_after_quarters = cents % 25
num_of_quarters = cents // 25

remainder_after_dimes = remainder_after_quarters % 10
num_of_dimes = remainder_after_quarters // 10

remainder_after_nickels = remainder_after_dimes % 5
num_of_nickels = remainder_after_dimes // 5

num_of_pennies = remainder_after_nickels

print(f"Q: {num_of_quarters}")
print(f"D: {num_of_dimes}")
print(f"N: {num_of_nickels}")
print(f"P: {num_of_pennies}")
