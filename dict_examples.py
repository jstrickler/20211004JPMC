from pprint import pprint

d1 = dict()  # empty dict
d2 = {'a': 18, 'm': 6, 'z': 42}
d3 = {}

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}
airports["IAH"] = "Houston"
airports['JFK'] = "NY - Kennedy"
airports['''IAH'''] = "Houston International"
pprint(airports, sort_dicts=False)
print(len(airports))
more_airports = {
    'LGA': 'La Guardia', 'LAX': 'Los Angeles', 'MIA': 'Miami'
}
airports.update(more_airports)
pprint(airports, sort_dicts=False)
print()

print(airports['RDU'])
# print(airports['XYZ'])
print(airports.get('XYZ'))
print(airports.get('RDU'))
print(airports.get('XYZ', 42))

new_data = [('CMH', 'Columbus', 'Xyz'), ('ORD', 'Chicago'),
            ('GLA', 'Glasgow', 5, 98), ('RDU', 'Durham'),
            ]

for new_key, new_value, *_ in new_data:
    print(airports.setdefault(new_key, new_value))

print(airports, '\n')

for code in 'LAX', 'ABC', 'MNO', 'RDU', 'LGA':
    print(code, (code in airports))

print(airports.keys())
print(airports.values())
print()

# loop through key:value pairs
for code, airport in airports.items():
    print(code, airport)
print()

for code, airport in sorted(airports.items()):
    print(code, airport)
print()



