mary_in = open('DATA/mary.txt')
# read file here ...
mary_in.close()

file_path = 'DATA/mary.txt'

with open(file_path) as mary_in:
    for raw_line in mary_in:   # mary_in.readline()
        line = raw_line.rstrip()
        print(line)
print('-' * 60)

with open(file_path) as mary_in:
    contents = mary_in.read()
    print("raw")
    print(repr(contents))
    print("normal")
    print(contents)
print('-' * 60)

with open(file_path) as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

with open(file_path) as mary_in:
    all_lines_without_nl = mary_in.read().splitlines()
    print(all_lines_without_nl)
print('-' * 60)

search_letter = 'z'
with open('DATA/words.txt') as words_in:  # reading
    with open('words.txt', 'w') as words_out:  # writing
        for raw_line in words_in:
            if raw_line.startswith(search_letter):
                words_out.write(raw_line)
            words_out.flush()  # force writing buffer to media
                               # very inefficent

#  "r" "w" "a"


x = open('mydata.txt', "w")
x.write('line one\n')
x.write('line two\n')





