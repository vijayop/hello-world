# fibonacci seris 

lim = int(input("Enter how much steps you want in your fibonacci series : "))
# fibonaccci logic
a = 0 
b = 1
print("fibonacci numbers in your given range are : ")
print(a)
print(b)
for i in range(1, lim-1):
    c = a + b 
    print(c)
    a = b
    b = c
