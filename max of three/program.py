n1=int(input("ennter n1:"))
n2=int(input("ennter n2:"))
n3=int(input("ennter n3:"))


# Finding the Largest of Three Numbers
if n1 == n2 == n3:
    print("all numbers are equal")
elif n1>=n2 and n1>=n3:
    print("largest number is ",n1)
elif n2>=n1 and n2>=n3:
    print("largest number is ",n2)
# elif n3>=n1 and n3>=n2:
else:
    print("largest number is ",n3)
