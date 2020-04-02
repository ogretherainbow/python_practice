#!/usr/bin/env python3.8

# Part 1
num_1 = 5
num_2 = 10
total = 0

for i in range((num_1),(num_2 + 1)):
    total = total + i
    #print(i)
print(total)

# Part 2
long_str = "Pneumonoultramicroscopicsilicovolcanoconiosis"
vowels = "aeiou"

for i in long_str:
    for k in vowels:
        if i == k:
            print(i)
