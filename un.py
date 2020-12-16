'''a = int(input("Enter a number: "))
#Here x variable changes with resp to i
fact  = 1
for i in range(1,a+1):
    fact = fact * i
    x = i
    p = pow(x,i)
    print(p,'/',fact, end = ', ')
#print('The factorial of',a,'is',fact)
'''
a = int(input('Enter a number: '))
count = 0
new = 0
temp = a
run = a
while temp!=0:
    count = count+1
    temp = temp//10
    
#print(count, a, temp, run)
while run!=0:
    n = run%10
    new = new + pow(n,count)
    run = run // 10
#print(new, run)
if new == a:
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')


