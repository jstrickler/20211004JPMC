cities = ['Glasgow', 'Bangalore', 'Columbus', 'Wilmington']

print(min(cities), max(cities), sorted(cities), len(cities), '\n')

nums = [800,80,1000,32,255,400,5,5000]
print(min(nums), max(nums), sorted(nums), len(nums), sum(nums), '\n')

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date"]

print(sorted(fruits), '\n')

for city in reversed(cities):
    print(city)
print()

for i, city in enumerate(cities):
    print(i, city)
print()
print(list(enumerate(cities)), '\n')

r = reversed(cities)
e = enumerate(cities)
print(r, e, '\n')
for city in r:
    print(city)
print()

for i, city in e:
    print(i, city)
print()

for wombat, naan in enumerate(cities):
    print(wombat, naan)
print()

for i in range(10):
    print(i)
print()
# range(STOP) range(START, STOP)  range(START, STOP, STEP)
for i in range(1, 6):
    print(i, end=' ')
print('\n')

for i in range(5, 101, 5):
    print(i, end=',')
print('\n')

for i in range(3):
    print("Python ROCKS!")
print()

