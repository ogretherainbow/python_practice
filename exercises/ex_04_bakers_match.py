#!/usr/bin/env python3.8

# Part 1
num_people = 1

# Part 2,3
num_cookie = 0
if num_people >= 10:
    num_cookie = num_people * 2
elif num_people < 10:
    num_cookie = num_people * 3
else:
    print("Error")

# Part 4
print("Plan to cook " + str(num_cookie) + " cookies.")
