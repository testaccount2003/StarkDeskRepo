#Q.4Display only odd position elements of tuple
T4 = ("a", 1,"b",2,"c",3)
n = len(T4)
print("The tuple is")
print(T4)
print()
print("Displaying the elements of even position index:")
for i in range(0,n,1):
    if i%2 == 0:
        print(T4[i], end = ' ')
