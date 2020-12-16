#Q2Display the even number elements of tuple
T2 = (0,1,2,3,4,5,6,7,8,9)
n = len(T2)
print("The tuple is")
print(T2)
print()
print("Displaying the numbers which are multiples of 2:")
for i in range(0,n,1):
    if T2[i]%2 == 0:
        
        print(T2[i], end = ' ')

