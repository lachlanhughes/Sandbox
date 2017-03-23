"""
example docstring
"""


name = input("Enter your name: ")

while not name:
    print("Name cannot be blank")
    name = input("Enter your name: ")

print(name)

for i in range(len(name)):
    if i%2 == 1:
        print(name[i])