import random


def generate_random_list():
    return [random.randint(1, 50) for _ in range(10)]


def substitute(lst):
    for i in range(len(lst)):
        if lst[i] % 5 == 0:
            lst[i] = lst[i] ** 2
    return lst


def main():
    random_list = generate_random_list()
    print("Before substitution, the list is:", random_list)
    substituted_list = substitute(random_list)
    print("After substitution, the list is:", substituted_list)


main()
