colors1 = ['red', 'purple', 'red', 'red', 'green', 'ecru', 'purple']
print(colors1)
colors2 = ['green', 'blue', 'red', 'ecru', 'blue', 'blue', 'blue', 'white']
print(colors2)
c1 = set(colors1)
c2 = set(colors2)
c1.add('black')
c1.add('pink')
for i in range(100):
    c2.add('orange')
print()
print(c1)
print(c2)

print("lavender" in c1)
print('orange' in c2)
print('brown' in c2)
print()

print("COMMON:", c1 & c2)  # intersection
print("NOT COMMON:", c1 ^ c2)  # xor  (non-common)
print("COMBO:", c1 | c2)  # union
print("c1 only:", c1 - c2)
print("c2 only:", c2 - c1)

all_food = ["spam", "spam", "spam", "spam", "eggs", "spam"]
food = set(all_food)
print(food)




