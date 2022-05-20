print("Find the largest number")
L=[]

n=1
while n<=5:
 k=int(input("Enter a number\n"))
 L.append(k)
 n=n+1


print("------------------")

print("Our largest number is  ",max(L))
print("Our smallest number is  ",min(L))
