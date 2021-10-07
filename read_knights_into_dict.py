from pprint import pp

def main():
    d = read_data()
    pretty_print(d)
    print(get_field(d, 'Arthur', 1))
    print_names_and_titles(d)

def read_data():
    data = {}

    with open('DATA/knights.txt') as knights_in:
        for raw_line in knights_in:
            row = raw_line.rstrip()
            name, title, color, quest, comment = row.split(':')
            data[name] = title, color, quest, comment
    return data

def pretty_print(knight_data):
    pp(knight_data)

def get_field(knight_data, knight_name, field_index):
    return knight_data[knight_name][field_index]

def print_names_and_titles(knight_data):
    for name, data in knight_data.items():
        print(data[0], name)

# if run directly, __name__ is '__main__'
# if imported, __name__ is 'module_name'
if __name__ == '__main__':
    main()
