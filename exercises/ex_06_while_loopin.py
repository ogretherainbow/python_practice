#!/usr/bin/env python3.8

# Part 1
num = float(200)
i = 0

while num > 1:
    i = i + 1
    num = num / 2
    #print(i)
    #print(num)
print(i)

# Part 2
num_1 = 1
num_2 = 3
high_num = max(num_1,num_2)
low_num = min(num_1,num_2)
count = high_num
#print(high_num)
#print(low_num)
print("")

while count >= low_num:
    print(count)
    count = count - 1
print("Blast Off!")
