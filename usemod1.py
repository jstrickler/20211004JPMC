from john.math import geometry
#  find geometry.py in john/math folders
import sys

print(geometry.circle_area(14))
result = geometry.square_area(100)
print(result)
print()
print(dir(geometry), '\n')

# how to find modules
# 1. current folder
# 2. folders in PYTHONPATH
# 3. built-in list
for path in sys.path:
    print(path)


