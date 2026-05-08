def print_repeated_twice(L):
    counts = {}
    for num in L:
        counts[num] = counts.get(num, 0) + 1
        printed = set()
    for num in L:
        if counts[num] == 2 and num not in printed:
            print(num)
            printed.add(num)
L = [2, 2, 3, 4, 5, 6, 6, 7, 8, 8, 8, 1, 0, 3]
print_repeated_twice(L)
