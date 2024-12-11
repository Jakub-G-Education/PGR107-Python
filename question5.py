zeroes = []
positive_numbers = []
negative_numbers = []

while True:
    user_number = input("Enter an integer (blank to quit): ")

    if user_number == "":
        break

    value = int(user_number)
    try:
        if value == 0:
            zeroes.append(value)
        elif value > 0:
            positive_numbers.append(value)
        else:
            negative_numbers.append(value)
    except ValueError:
        print("Something went wrong...")

print()

print("The numbers were:")
for i in positive_numbers, zeroes, negative_numbers:
    print(" ".join(map(str, i)), end=" ")


