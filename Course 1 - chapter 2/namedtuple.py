# Demonstrate the usage of namdtuple objects

import collections

# TODO: create a Point namedtuple
print("\nIn this code we are creating a Point namedtuple\n")
Point = collections.namedtuple("Point", "x y")
p1 = Point(10,20)
p2 = Point(30,40)
print(p1)
print(p2,"\n")
print(p1.x,p1.y,"\n")

# TODO: use _replace to create a new instance
p1 = p1._replace(x=100)
print(p1,"\n")
