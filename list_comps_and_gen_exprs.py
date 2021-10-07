fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

#   thing-to-add   var   iterable
f1 = [f.upper() for f in fruits]  # list comprehension
print("f1:", f1, '\n')

# [EXPR for VAR in ITERABLE]
# [EXPR for VAR in ITERABLE if CONDITION]
f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2:", f2, '\n')

def half(x):
    return x / 2

nums = [800,80,1000,32,255,400,5,5000]

n1 = [half(n) for n in nums]
print("n1:", n1, '\n')

f3 = [len(f) for f in fruits]
print("f3:", f3, '\n')

f4 = [(f.upper(), len(f)) for f in fruits]
print("f4:", f4, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

last_names = [p[1] for p in people]
print("last_names:", last_names, '\n')

f5 = [f[:4] for f in fruits if len(f) > 6]
print("f5:", f5, '\n')

items = 5, 18, "wombat", "dairy cow"
x = [thing for thing in items if len(str(thing)) > 2]
print("x:", x, '\n')

fgen = (f.upper() for f in fruits)
fruits.append('durian')
print("fgen:", fgen, '\n')
print("First time:")
for fruit in fgen:
    print(fruit)
print()

print("Second time:")
for fruit in fgen:
    print(fruit)
print()







