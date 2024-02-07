# Importing the operator module
import operator

print("Using operator xor() function with integer values ->")
# Initializing two integers x and y
x = 12
y = 13

# Finding XOR of two integers x and y using the xor() function
z = operator.xor(x, y)

# Printing x ⊕ y
print(x, "XOR", y, "=", z)

print()

print("Using operator xor() function with boolean values ->")
# Initializing the boolean values
a = True
b = False

# Finding XOR of boolean values using the xor() function
p = operator.xor(a, a)
q = operator.xor(a, b)
r = operator.xor(b, a)
s = operator.xor(b, b)

# Printing the XOR values
print(a, "XOR", a, "=", p)
print(a, "XOR", b, "=", q)
print(b, "XOR", a, "=", r)
print(b, "XOR", b, "=", s)
