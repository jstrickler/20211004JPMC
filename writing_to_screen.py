a = 123
b = "Dennis Ritchie"
c = 48.3938092

#  sep = ' '   end = '\n'
print(a)    #  print(str(a) + end)
print(a, b, c)  # print(str(a) + sep + str(b) + sep + str(c) + end)
print()

print(a, b, c, sep=";")
print(a, b, c, sep="/")
print(a, b, c, sep="")
print(a, b, c, sep=", ")

print("one", end=' ')
print("two", end=' ')
print("three")

print("a is", a, "b is", b, "c is", c, sep="/")
#  2.7, 3.0+
print("a is {} b is {} c is {:.2f}".format(a, b, c))
# 3.6+ "f string"  "f-string"  "formatted string"   f"...."
sep = ";"
print(f"a is {a}{sep} b is {b}{sep}c is {c:.2f}")
print(f"2 + 2 = {2 + 2}")

x = 18
# newer way, 3.6 and later
print(f"x is {x}")
print(f"x is {x:5d}")    # pad with spaces to 5 chars wide
print(f"x is {x:05d}")   # pad with zeroes to 5 chars wide
print(f"x is {x:08x}")
print(f"x is {x:08b}")

# older way, 3.0 and later
print("x is {:08b}".format(x))


