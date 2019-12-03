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
