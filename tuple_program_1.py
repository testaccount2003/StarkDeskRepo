#Q1. Display the elements of tuple those are divisible by 5
T = (1,2,3,4,5,6,7,8,9,10)
n = len(T)
print("The tuple is")
print(T)
print()
print("Displaying the numbers which are multiples of 5:")
for i in range(0,n,1):
    if T[i]%5 == 0:
        
        print(T[i], end = ' ')
