#Q.3Display only odd position elements of tuple
T3 = ("a", 1,"b",2,"c",3)
n = len(T3)
print("The tuple is")
print(T3)
print()
print("Displaying the elements of odd position index:")
for i in range(0,n,1):
    if i%2 != 0:
        print(T3[i], end = ' ')
