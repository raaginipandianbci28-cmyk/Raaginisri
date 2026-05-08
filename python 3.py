n1, n2 = map(int, input().split())
for i in range(n2, n1 - 1, -1):
    for j in range(n1, i + 1):
        print(j, end="")
    print()
