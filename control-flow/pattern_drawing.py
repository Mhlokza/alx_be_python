integer = int(input("Enter the size of the pattern: "))
i=1
while i<=integer:
    for ans in range(0,integer):
        print("*"*integer, end="")
        i=i+1
        print()