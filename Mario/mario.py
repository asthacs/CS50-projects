from cs50 import get_int

while True:
    n= get_int("Height: ")
    if n>=1 and n<=8:
        break

for i in range(n):
    for k in range(n-i-1):
        print(" ", end="")
    for j in range(i+1):
        print("#", end="")
    print("  ", end="")
    for j in range(i+1):
        print("#", end="")
    print()