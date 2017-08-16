"""
Matthew Darley
"""

name = str(input("Enter your name: "))
while name == '':
    print("Please enter your name")
    name = str(input("Enter your name: "))
print(name[1::2])
