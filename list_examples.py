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


