#!/usr/bin/env python3.8


# Part 1
def first_letter(string):
    return string[0]
print(first_letter("test"))


# Part 2
def last_three(string):
    return string[-3:]
print(last_three("test"))


# Part 3
def char_count(char, string):
    string = string.lower()
    total = 0
    for i in string:
        if i == char:
            total = total + 1
    return total
print(char_count("e","cheesE"))


# Part 4
def remove_vowels(string):
    vowels = "aeiou"
    new_string = ""
    print(vowels[-1])
    for letter in string:
        for vowel in vowels:
            if letter == vowel:
                break
            elif vowel == vowels[-1]:
                new_string = new_string + letter
            else:
                pass
    return new_string
print(remove_vowels("cheese"))


# Part 5
def hello_goodbye(name, num):
    if num == 1:
        thing = "Hello, "
    elif num == 2:
        thing = "Goodbye, "
    else:
        thing = "This error is for you, "
    return thing + name
print(hello_goodbye("John",1))


# Part 6
def spooky(string):
    length = len(string)
    new = ""
    #print(length)
    for i in range(0, length):
        if i % 2 == 0:
            new = new + string[i].lower()
        else:
            new = new + string[i].upper()
    return new
print(spooky("Treat yo self"))


# Part 7
def initials(string):
    thing = string[0]
    i = 0
    for letter in string:
        if letter == " ":
            thing = thing + string[(i+1)]
        i = i + 1
    return thing
print(initials("Rocket League"))


# Part 8
def mixup(string1,string2):
    return string2[0] + string1[1:] + " " + string1[0] + string2[1:]
print(mixup("hi","bye"))

def mixup_extended(string1,string2,num):
    return string2[0:num] + string1[num:] + " " + string1[0:num] + string2[num:]
print(mixup_extended("hello","goodbye",4))


# Part 9
def not_bad(string):
    i = 0
    first = 0
    last = 0
    for letter in string:
        if letter == "n":
            thing1 = string[i:(i+3)]
            if thing1 == "not":
                first = i
        elif letter == "b":
            thing2 = string[i:(i+3)]
            if thing2 == "bad":
                last = i + 3
        i = i + 1
    return string[0:first] + "good" + string[last:]
print(not_bad("this is not super bad tuna"))


# Part 10
def h4ck3r_sp33k(string):
    new_char = ""
    for char in string:
        if char == "a" or char == "A":
            new_char = new_char + "4"
        elif char == "e" or char == "E":
            new_char = new_char + "3"
        elif char == "l" or char == "L":
            new_char = new_char + "1"
        elif char == "t" or char == "T":
            new_char = new_char + "+"
        else:
            new_char = new_char + char
    return new_char
print(h4ck3r_sp33k("Big Cat Rescue"))


# Part 11
def same_x_and_o(string):
    x_count = 0
    o_count = 0
    for char in string:
        if char == "x":
            x_count = x_count + 1
        elif char == "o":
            o_count = o_count + 1
        else:
            pass
    if x_count == o_count:
        return True
    else:
        return False
print(same_x_and_o("xxx ooo"))

