"""
Matthew Darley
"""


def main():
    name = get_name()
    print_steps(name, 2)


def get_name():
    name = str(input("Enter your name: "))
    while name == '':
        print("Invalid name")
        name = str(input("Enter your name: "))
    return name


def print_steps(name,step=2):
    print(name[1::step])


main()
