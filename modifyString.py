
txt = input("Enter the txt : ")

print("Upper case of the txt is : " + txt.upper())
print("Lower case of the txt is : " + txt.lower())
print("txt without whitespace in begining or end is : " + txt.strip())

re = input("Enter the letter to be replaced : ")
x = input("Enter the which letter to insert : ")

print("Replaced txt is : " + txt.replace(re,x))