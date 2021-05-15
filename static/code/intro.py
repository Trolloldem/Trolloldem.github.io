# Example of class definition
class example:

    # Class constructor
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    # Class method definition
    def get_full_name(self):

        # Usage of parametrized string
        return "{} {}".format(self.name, self.surname)

# Python loop examples
def cycle():

    # Loop using the range() built-in function
    for i in range(0,15):
        print(i)
    print("=========")

    # List definition
    x = ["addf", 1, 0.5, ["l"]]

    # Loop using range() + len(list)
    for i in range(0, len(x)):
        print(x[i])
    print("=========")
    x.append(4)

    # Loop using for-each
    for elem in x:
        print(elem)
    print("=========")


def power_2(x):
    # This is called list List Comprehension: fast way to create a list
    return [i*i for i in x]

def collections():

    # This is a dictionary: assign a key to every value stored
    dict = {"food": ["apple", "bread"], "integers": [1,2]}

    # In this way you can iterate over both keys and values at the same time
    for key, value in dict.items():
        print(key, value)

    # Access a specific value using its key
    print(dict["food"])

    # A tuple is defined using (). It can be unpacked in multiple variables
    a, elem, elem2 = ("a", 1, 3)

    # Example of usage of the zip() built-in function
    names = ["Dario", "Gianluca", "Matthew"]
    surnames = ["Facchinetti", "Oldani"]

    # Unpack similarly to what we have done with dict.items()
    for name, surname in zip(names, surnames): #  [("Dario", "Facchinetti"), ("Gianluca", "Oldani")]
        to_print = f"Name: {name} Surname: {surname}" # works from python3.6
        print(to_print)

    # If we want to print every value we have to do some checks
    for i in range(0, max(len(names), len(surnames))):
        # Ternary expression
        name = names[i] if i < len(names) else "" # value_true if condition else default_value
        surname = surnames[i] if i < len(surnames) else ""
        to_print = f"Name: {name} Surname: {surname}"
        print(to_print)

# Function used with filter()
def filter_elems(x):
    return x != 2

# Define a simple main() function
def main():
    x = 5
    y = 10
    print(x + y)

# This code will not run if this file is used as a module
if __name__ == "__main__":
    main()
    cycle()
    collections()
    user = example("name", "surname")
    x = [2,3,4]
    print(power_2(x))
    for i in filter(filter_elems, x):
        print(i)
