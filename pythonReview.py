#Start here

print("Hi Greg's students in IR")

message = "Hi Greg's students in IR"
print(len(message))
print(message[0])
print(type(message))
print(type(3))
print(type("3"))
print(3*3)
print(3*"3")
print(len("greg")==4)

a = 10
b = 3

print(a+b) #addition
print(a-b) #substraction
print(a*b) #multiplication
print(a/b) #division
print(10/2)  #always returns floats bc it returns the same type
print(a//b) #this is called floor division
print(a**b) #a to the power of b
print(a%b) #modulo


#python allows multiple types of values inside a list
professors = ["greg", "kianoosh", "richard", "patricia", "debra"]
print(professors[0])
print(professors[-1]) #this is how we start backwards on a list

professors.append("leo")
print(professors)

#below is how we extend a list, increment an already existing list
professors.extend(["heather", "kevin", "jason"])

print(professors)

professors.insert(2, "trevor")

print(professors)

professors[3] = "mark"
print(professors)

#this is how python uses ranges
#this is going through 3 to 4 below, 5 is not including
print(professors[3:5]) #accessing here professor in positions 3 and 4

#you can run the program everytime and check what is happening

print(professors[5:]) # this will print starting in 5 to the end
print(professors[:3]) # this will print from zero to 2

print(professors[:])  #this will print the entire list however the important thing is here that you create a copy of
#that list somewhere else, this way you can safely remove or add to that new list

print(professors.remove("kianoosh"))
print(professors)
print(professors.index("mark"))
#print(professors)
x = professors.pop(6)
print(professors)
print(x)
print(len(professors))
print(type(professors))
professors.sort()
print(professors)
professors.sort(reverse=True)
print(professors)

for i in professors: #indentation is the headache on python so be careful
    print(i.title())
print("FIU")

#below is a dictionary
water_data = {
    "temperature": [78,89,92],
    "pH": [6.5, 6.7, 6.3],
    "oxygen": [7.2, 5.6, 3.5],
}

print(water_data["oxygen"])
print(water_data.values())

import pandas as pd

df = pd.DataFrame(water_data)
print(df)













