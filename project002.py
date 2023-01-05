import math
"""Finding The Areas of Plan Shapes"""

print("""This Program is use to find the area of multiple plan shapes.
Press 1 to find the area Triange 
Press 2 to find the area of a Square
Press 3 to find the area of a Rectangle""")
print("")
"""Making use of the if construct"""

a, b ,c = [1, 2, 3]

conditions = input("Select a task to perform: ")
print("")

try:
    conditions = int(conditions)
except:
    print("")

if conditions == a:
    print("Finding the area of a Triangle")
    print("")
    base = input("Enter the value of the base: ")
    height = input("Enter the value of the height: ")

    base = int(base)
    height = int(height)

    area = 1/2 * (base * height)
    print ("The are of the triangle = ",area)
elif conditions == b:
    print("Finding the area of a Square")
    print("")
    lenght = input("Enter the length of the square: ")
    lenght = int(lenght)

    area = math.pow(lenght,2)
    print ("The are of the square = ",area)
elif conditions == c:
    print("Finding the area of a Rectangle")
    print("")
    lenght = input("Enter the length of the rectangle: ")
    lenght = int(lenght)
    breadth = input("Enter the breadth of the rectangle: ")
    breadth = int(breadth)

    area = lenght * breadth
    print ("The are of the rectangle = ",area)

else :
    print("something went wrong, Select the right value")
