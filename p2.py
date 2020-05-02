# initializing the list
size = int(input("enter the size of the list : "))
l = []

# taking elements from the user 
print("enter " + str(size) + " Elements in the list")
for i in range(1,size+1):
    a = int(input("Enter element number " + str(i) + " : "))
    l.append(a)
print("The list you entered is  : " +str(l)) 

# taking out negative numbers from the list 
for i in l :
    if i < 0:
        l.remove(i)
print("The answer list is : " +str(l))
