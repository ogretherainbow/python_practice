#!/usr/bin/env python3.8

# Part 1
def sum_of_two_nums(num1, num2):
    total = num1 + num2
    return total
print(sum_of_two_nums(1, 3))

# Part 2
def greater_than_ten(num):
    if num > 10:
        return True
    else:
        return False
print(greater_than_ten(11))

# Part 3
def odd_or_even(num):
    if (num % 2) == 0:
        print("even")
    else:
        print("odd")
odd_or_even(12)

# Part 4
def how_many_legs(num_cows, num_chickens, num_spiders):
    return (num_cows * 4) + (num_chickens * 2) + (num_spiders * 8)
print(how_many_legs(1,2,3))

# Part 5
def multiple_of_3(num):
    if num % 3 == 0:
        return True
    else:
        return False
print(multiple_of_3(12))

# Part 6
def area_of_a_triangle(base, height):
    return (base * height) / 2
print(area_of_a_triangle(2,2))
