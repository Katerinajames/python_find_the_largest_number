print("Find the largest number")
L=[]

n=1
k=int(input("Enter a number\n"))
while(k!=-1):		 
		 L.append(k)
		 n=n+1
		 k=int(input("Enter a number\n"))     
         
       
         


print("------------------")
if(len(L)==0):
      print("There are no numbers to compare")
else:    
    print("Our largest number is  ",max(L))
    print("Our smallest number is  ",min(L))
