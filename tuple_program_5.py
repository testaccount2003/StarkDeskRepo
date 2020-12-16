#Q.5Display the odd number elements of tuple
T5 = (0,1,2,3,4,5,6,7,8,9)
n = len(T5)
print("The tuple is")
print(T5)
print()
print("Displaying the numbers which are odd:")
for i in range(0,n,1):
    if T5[i]%2 != 0:
        
        print(T5[i], end = ' ')
