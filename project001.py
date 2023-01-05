print("Project 001 ")
print('Working with string and basic artimetic operators')

c = 10

print(type(c))

"""Making use of comment and trying out mutiple declearations"""

a, b, c = ["a1","b2","c3"]

print("a = " + a, "b = " + b + "\n", "c = " + c)

"""String Format """

lists = ["quality","good","5000"]
txt = "The {} of the shirt is very {} but it cost {} Naira"

print(txt.format(lists[0],lists[1],lists[2]))

a = "banana"
b = "apple"

txt = 'I Love {0}, and {1}'

print(txt.format(b,a))


print("The {carname} is {color} in color".format(carname = "Toyoto", color = "black"))


for x in lists:
	print(x)

for x in "banana":
	print(x)


