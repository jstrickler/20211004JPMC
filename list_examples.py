import sys

list1 = list()  # empty list
# x = list(any-iterable)
list2 = ['a', 'b', 'c', 'd']
list3 = []
s = "Python is wonderful"
list4 = s.split()
print(list1, list2, list3, list4, '\n')

cities = ['Glasgow', 'Bangalore', 'Columbus', 'Wilmington']
print(cities[0])
print(cities[2])
print(cities[-1])  # cities[len(cities) - 1]

cities.append('Houston')
cities.append('Jersey City')

print(cities)
cities.insert(0, 'Durham')
print(cities)
cities.insert(4, 'New York')
cities.insert(6, 'Paris')
print(cities)

more_cities = ['Dakar', 'Mumbai', 'London']

cities.extend(more_cities)
print(cities)

#  LIST.append(obj)  LIST.insert(pos, obj) LIST.extend(iterable)

del cities[8]
print(cities)

cities.remove('Wilmington')  # raises error if value not found
print(cities)

for city in 'Glasgow', 'Bangalore', 'Goa', 'Edinburgh':
    print(city, city in cities)
print()

c = cities.pop()  # remove and return item -1
print(c, cities)
c = cities.pop(3) # remove element [3] and return it
print(c, cities)

#  del LIST[pos]     LIST.pop(pos)   LIST.remove(value)
print(cities, '\n')

print(cities[0:4])
print(cities[1:5])
print(cities[2:6])
#  LIST[START:STOP]  LIST[:STOP]  LIST[START:]
# LIST[START:STOP:STEP]

print(cities[-2:])
print(cities[:3])
print(cities[1:])

print(sys.argv)
for file_name in sys.argv[1:]:
    print("processing", file_name)
print()

cap = "Captain America"
print(cap[:3])
print(cap[5:7])
print(cap[-7:-3])
print()
print(cities, '\n')

for city in cities:
    # city = <next-value-of> cities
    print(city, city.upper())
print()
# for VAR in ITERABLE:
#    code ....

for letter in cap:
    print(letter.upper())
print()






