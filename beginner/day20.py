# Print a right-aligned triangle of *
n = 5

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)


# Print an inverted triangle
n = 5

for i in range(n, 0, -1):
    print("*" * i)

# Print a number pyramid (1, 12, 123...)
n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Print Floyd's triangle
n = 5
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# Print a diamond shape


# Print a hollow square
n = 5

for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Print Pascal's triangle (first 5 rows)
n = 5

for i in range(n):
    num = 1

    for j in range(i+1):
        print(num, end=" ")

        num = num*(i-j)//(j+1)

    print()


# Print a checkerboard pattern
n = 8

for i in range(n):
    for j in range(n):
        if (i+j)%2 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()