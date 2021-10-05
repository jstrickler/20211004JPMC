s1 = "spam\n"     # single-delimited (" or ')
s2 = 'spam\n'
# syntactic sugar
s3 = """spam\n"""  # triple-delimited  (" or ')
s4 = '''spam\n'''
s5 = r"spam\n"  # raw string -- does not interpret \

print(len(s1), len(s2))

print("Guido's the former BDFL of Python")
print("""Guido is the former "BDFL" of Python""")
print('''"""Guido is the former "BDFL" of Python"""''')
print("Guido is the former \"BDFL\" of Python")
print("""Guido's the former "BDFL" of Python""")
print("""Use an empty string "" for that""")

query = """
select *
from customers
where lastname = "Jones" and state = "NC"
"""

x = 5
print("x is", x)



