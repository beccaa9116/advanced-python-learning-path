# Demonstrate the usage of Counter objects

from collections import Counter


# list of students in class 1
class1 = ["Bob", "James", "Chad", "Darcy", "Penny", "Hannah",
          "Kevin", "James", "Melanie", "Becky", "Steve", "Frank"]

# list of students in class 2
class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
          "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

# TODO: Create a Counter for class1 and class2
c1 = Counter(class1)
c2 = Counter(class2)

# TODO: How many students in class 1 named James?
print("\nHow many students in class 1 are named James?")
print(c1["James"],"\n")

# TODO: How many students are in class 1?
print("How many students are there in class 1?")
print(sum(c1.values()))

# TODO: Combine the two classes
print("\nHow many students are there in total?")
c1.update(class2)
print(sum(c1.values()))

# TODO: What's the most common name in the two classes?
print("\nWhat is the most common name in these classes?")
print(c1.most_common(1))

# TODO: Separate the classes again
print("\nJust checking... how many students are in class 1?")
c1.subtract(class2)
print(sum(c1.values()))

# TODO: What's common between the two classes?
print("\nWhat names are common in class 1 and class 2?")
print(c1 & c2)

print("\nThat's it!")
