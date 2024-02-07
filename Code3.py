# Initializing the boolean values
a = True
b = False

# Finding XOR of boolean values using ^ operator
p = a ^ a
q = a ^ b
r = b ^ a
s = b ^ b

# Printing the XOR value of every boolean combination
print(a, "XOR", a, "=", p)
print(a, "XOR", b, "=", q)
print(b, "XOR", a, "=", r)
print(b, "XOR", b, "=", s)
