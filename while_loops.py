i = 0
# while EXPR:
while i < 3:
    print(i)
    i += 1
print()

while True:
    user_name = input("Enter name (or q to quit): ")
    user_name = user_name.strip()  # clean leading/trailing spaces
    if user_name == 'q':
        break  # quit
    if user_name == '':
        print("Please enter a name")
        continue  # go back to top
    print(f"Adding {user_name}")
