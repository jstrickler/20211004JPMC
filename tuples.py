
person = 'Bill', 'Gates', 'Microsoft', '1955-10-24'

print(person)
print(type(person))
print(person[0], person[:2])

# not possible:
# person[1] = 'Jones'
# person.append('wombat')

# alternatives to tuples
# 1. namedtuple   person.first_name
# 2. dataclass    person.first_name  (added in 3.7)
# 3. "normal" class

# person[0]  person[1]  person[2] p[3] ...
first_name, last_name, *other = person   # iterable unpacking
print(first_name, last_name, other)

values = ['a', 'b', 'c', 'd', 'e', 'f']
x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)

colors = ['red', 'yellow']
a, *b, c = colors
print(a, b, c)

m = """Melinda O'Brien"""

people = [
    (m, 'Gates', 'Gates Foundation', '1964-08-15'),
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
m = "Michael" # dynamic !!
print(type(people), type(people[0]))
print(people[0])
print(people[0][0])
print(people[0][0][0])
print()
for person in people:
    print(person[0], person[1])
print("-" * 60)

for first_name, last_name, product, dob in people:
    print(first_name, last_name)
print("-" * 60)
print(m)

