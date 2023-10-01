
char = input("Enter a character for the pattern : ")
n = int(input("Enter the limit : "))

for i in range(n):
    for j in range(i):
        print(char , end="\t")
    print("\n")