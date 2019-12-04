import fractions
import math


# Number
# basic arithmatic operation with python

print(11 / 2)  # 5.5

# round down
print(11 // 2)  # 5
print(-11 / 2)  # -6

# square
print(11 ** 2)  # 121

# the rest
print(11 % 2)  # 1

# Fracition
x = fractions.Fraction(1, 3)
y = fractions.Fraction(2, 6)

print(x)  # 1/3

# python automatically reduce a fraction.
print(y)  # 1/3

# Trigonometry
pi = math.pi
print(pi)
print(math.sin(pi / 2))
print(math.tan(pi / 4))

# Boolean
def is_it_true(anything):
    if anything:
        print("True")
    else:
        print("False")


print(is_it_true(0))  # False
print(is_it_true(fractions.Fraction(0, 1)))  # False

# List
a_list = ["junsik", "25", "icheon", "Ubuntu"]
print(a_list[1])  # "25"
print(a_list[-1])  # "Ubuntu"

# Slicing List
print(a_list[1:3])  # ["25", "icheon"]
print(a_list[1:-1])  # ["25", "icheon"]
print(a_list[0:3])  # ['junsik', '25', 'icheon']
print(a_list[:-1])  # ['junsik', '25', 'icheon']
print(a_list[:])  # all

# add item to list
# this method instantly doubles memory usage
a_list = a_list + [2.0, 3]

# add item to end of the list
a_list.append(True)

a_list.extend("junsik2")

# insert item in a fixed position
a_list.insert(0, "first")

# difference between extend & append
b_list = [1, 2, 3]
b_list.extend([4, 5, 6])  # [1,2,3,4,5,6]
b_list.append([7, 8, 9])  # [1,2,3,4,5,6,[7,8,9]]

# search for in list
a_list.count("junsik")  # 1
print("junsik" in a_list)  # True
# if index can't search value you want, error could occur
a_list.index("junsik")  # 1

# delete item in list
del a_list[1]
a_list.remove("junsik2")
# pop method remove last arg in list, if you not enter a args
a_list.pop()  # remove last arg, '2'

# judge whether true or false with list
# empty list is True in this function.
# # because conditional sentence recognize empty list like something
is_it_true(["a"])  # True
is_it_true([False])  # True

# Tuple
# inner item in tuple is immutable
# tuple don't have method to delete or update. no pop(), no remove()
a_tuple = (1, 2, 3, "a", "b")

# When is it approproate to use tuple?
# tuple is faster than list.
# if the tuple have items that are no posibility of change later.
# if item in the tuple must not change.
# tuple is immutable so this can be used for key in dictionary

# tuple can be converted to list. vice versa.
# tuple( ) freezes list, list( ) melts tuple. Very literary!

is_it_true(())  # False

# if you don't write comma after item, python can't recognize your tuple as tuple
is_it_true((False,))  # True

# Assign multiple values at once
v = (1, "a", True)
(x, y, z) = v

print(x)  # 1
print(y)  # "a"
print(z)  # True

(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)

print(MONDAY)  # 0
print(TUESDAY)  # 1

# what is set ?
# make set with curly bracket
a_set = {1}
print(a_set)  # {1}
print(type(a_set))  # <class 'set'>

a_set = {1, 2}
print(a_set)  # 1,2

# convert list to set
# set don't care item order, unordered
c_list = [1, 2, "a", "4", True]
c_set = set(c_list)
print(c_set)  # {1, "a", 2, "4", True}
print(c_list)  # [1, 2, "a", "4", True], the original remains intact.

# change item in set
c_set.add("5")
print(c_set)  # {1, "5", "a", 2, "4", True}

c_set.add("4")
print(c_set)  # {1, "5", "a", 2, "4", True}
# set don't alllow duplicate value

c_set.update({1, 2, 3})
print(c_set)  # {1, "5", "a", 2, 3, "4", True}
c_set.update({1, 2, 3}, {4, 5, 6})
print(c_set)  # {1, 5, "5", "a", 2, 3, "4", 4, 6, True}
c_set.update([1, 2, 3])  # can add list to set
print(c_set)  # {1, 5, "5", "a", 2, 3, "4", 4, 6, True}

# delete item in set
a_set = {1, 3, 6, 10, 15, 21, 28, 36, 45}

print(a_set)  # {1, 3, 36, 6, 10, 45, 15, 21, 28}
a_set.discard(10)
print(a_set)  # {1, 3, 36, 6, 45, 15, 21, 28}

a_set.remove(21)
print(a_set)  # {1, 3, 36, 6, 45, 15, 28}
a_set.remove(21)  # KeyError: 21

# difference between discard & remove is be when error occurred

# pop
# pop method of set return value randomly removed.
print(a_set.pop())  # 1
print(a_set.pop())  # 3
print(a_set.pop())  # 36

a_set.clear()
print(a_set)  # set()
print(a_set.pop())  # KeyError: 'pop from an empty set'

# set operation
a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}

print(30 in a_set)  # True
print(31 in a_set)  # False

print(a_set.union(b_set))  # Symmetric
print(a_set.intersection(b_set))  # Symmetric
print(a_set.difference(b_set))  # not Symmetric
print(a_set.symmetric_difference(b_set))  # Symmetric

a_set = {1, 2, 3}
b_set = {1, 2, 3, 4}

a_set.issubset(b_set)  # True
b_set.issuperset(a_set)  # True

a_set.add(5)
a_set.issubset(b_set)  # False
b_set.issuperset(a_set)  # False

is_it_true(set())  # False
is_it_true({"a"})  # True
is_it_true({False})  # False

