#!/usr/bin/env python3.8

# Part 1

def largest_num(list):
    lastnum = list[0]
    #print(lastnum)
    for i in list:
        #print(i)
        num = i
        if num > lastnum:
            lastnum = num
    return lastnum
print(largest_num([1,5,3,-7,0]))


# Part 2

def includes(list, num):
    if num in list:
        return True
    else:
        return False
print(includes([1,2,3,4],2))


# Part 3

def average(list):
    num = 0
    for i in list:
        num = num + i
    return float(num / len(list))
print(average([1,2,3,4,5]))


# Part 4

def median(list):
    s_list = sorted(list)
    half = int(len(list) / 2)
    return float(s_list[half])
print(median([3,15,4,7,11,9,44]))


# Part 5

def only_a(list):
    newlist = []
    for i in list:
        if "a" in i:
            newlist.append(i)
    return newlist
print(only_a(['ooga','booga','dog','expert','puppy','cactus']))


# Part 6

def odd_couple(list):
    oddlist = []
    for i in list:
        if (i % 2) != 0:
            oddlist.append(i)
    return oddlist[0:2]
print(odd_couple([1,6,8]))


# Part 7

students = [
  ['Maria', 91.5],
  ['George', 47.3],
  ['Anquan', 94.0],
  ['Lucia', 89.2]
]
def overachiever(lists):
    grades = []
    person = ""
    for list in lists:
        grades.append(list[1])
    high = max(grades)
    for list in lists:
        if list[1] == high:
            person = list[0]
    return person
print(overachiever(students))


# Part 8

def absolute_total(list):
    total = 0
    for i in list:
        if i < 0:
            total = total + (i * -1)
        else:
            total = total + i
    return total
print(absolute_total([1,-50,4,-120,460,-612,90]))


# Part 9

def sum_of_cubes(list):
    total = 0
    for i in list:
        total += i**3
    return total
print(sum_of_cubes([7, -3, -4]))


# Part 10

def multipy_by_index(list):
    index = 0
    total = 0
    for i in list:
        total += i * index
        index += 1
    return total
print(multipy_by_index([1,2,3]))
