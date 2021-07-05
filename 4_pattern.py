n = 5

spaces = (4 * (n - 1)) - 1

for i in range(1, n + 1):
    # printing the first pattern
    for j in range(1, i + 1):
        print(j, end=" ")

    # printing the second pattern
    k = 1
    while k < spaces:
        print(" ", end = "")
        k += 1
    spaces -= 4

    # printing the third pattern
    if n == i:
        start = i - 1
    else:
        start = i
    end = 1
    while start >= end:
        print(start, end = " ")
        start -= 1
    print()
