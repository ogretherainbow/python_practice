#!/usr/bin/env python3.8

stuff = ["thing1", "thing2", "beef", "ham", 123, 7]
string = "This is a string with a couple of numbers: 123 and 7"

slice(string)
stuff.append(8)

if 123 in stuff:
    print("Yes!")
else:
    print("No!")

for item in stuff:
    #print(item)
    #print(type(item))
    try:
        item.isdigit()
        print(item)
    except:
        pass

#print(type(stuff))

#print(stuff)
#print("thing1 is at index " + str(stuff.index("thing1")))
#print("123 is at index " + str(stuff.index(123)) + " and the value of that index is " + str(stuff[stuff.index(123)]))

#print(str(stuff[stuff.index(123)]))
