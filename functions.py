import os

def get_message():
    return "Hello, JPMC world"

m = get_message()
print(m)

def say_hello():  # returns None
    print("HELLO HELLO")
    # return None

say_hello()

print(get_message())
print()

def hello(whom="world"):
    print("Hello,", whom)

hello('world')
hello("Mom")
hello("sailor")
hello()
print()


def find_lines(term, file_path):
    with open(file_path) as file_in:
        for raw_line in file_in:
            if term in raw_line:
                print(raw_line.rstrip())

find_lines('bird', 'DATA/parrot.txt')
print()

find_lines('Lizard', 'DATA/alice.txt')
print()

def find_lines(term, *file_paths):
    for file_path in file_paths:
        with open(file_path) as file_in:
            for raw_line in file_in:
                if term in raw_line:
                    print(os.path.basename(file_path), raw_line.rstrip())

find_lines('bird', 'DATA/alice.txt', 'DATA/parrot.txt', 'DATA/words.txt')

colors = ['red', 'white', 'blue']

def add_color(my_list):
    my_list.append('purple')

print(colors)
add_color(colors)
print(colors)




