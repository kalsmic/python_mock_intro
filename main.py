# main.py
def double(x):
    return 2 * x


def add_two_doubled_values():
    x = double(2)
    y = double(3)
    return x + y


def get_two_doubled_values():
    x = double(2)
    y = double(3)
    return [x, y]


def add_two():
    x = input("Provide first number to add : ")
    y = input("Provide Second number to add : ")
    return x + y


if __name__ == "__main__":
    print("double 3: ", double(3))
    print("Add doubled values 2 and 3 : ", add_two_doubled_values())
