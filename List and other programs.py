

"""
Q) Write a Program to reverse a given list without creating or assigning a new list to a 
different memory location or using {Reverse function.}


L = [ 45 , 85 , 4 , 7, 89 , 23 , 47 , 25 , 57 , 84 , 35 , 59 ]
Output: The Reversed List is [ 45 , 85 , 4 , 7, 89 , 23 , 47 , 25 , 57 , 84 , 35 , 59 ].

"""









# l = [45,85,4,7,89,23,47,25,57,84,35,59]
# index = 0
# while index < len(l):
#     position = l[-1]
#     l.pop(-1)
#     l.insert(index,position)
#     index += 1
    
# print(l)





"""
Q) Write a Program to multiply the given number say (n) with each element of the list, where the list and the 
number (n) is an input by the User, Creation of a new list or any object which uses different memory 
location other than the Primary list is Strictly Prohibited.


Output: 
The List Entered by the user is [1,2,3,4,5]
The Modified LIst is [5,10,15,20,25]

"""








# listIn = eval(input('Enter list elements: '))
# numIn = int(input("Enter the value with which you want to multiply the list elements: "))

# print(f"The List Entered by the user is {listIn} ")


# for i in range(len(listIn)):
#     listIn.append(listIn[0]*numIn)
#     listIn.remove(listIn[0])
# print(f"The Modified LIst is {listIn}")


"""
Q3) Write a Program to display the Maximum and the Minimum values from the specified range of indexes of the List.
L = [ 45, 85, 25, 35, 74, 58, 69, 32, 47, 37, 21, 54 ]

Output: 
Enter the Start Index : 5
Enter the End Index : 10

The Maximum Value of the specified index 5 - 10 is 69.
The Minimum Value of the specified index 5 - 10 is 21.
"""



# l = [ 45, 85, 25, 35, 74, 58, 69, 32, 47, 37, 21, 54 ]

# in1 = int(input("Enter the starting index: "))
# in2 = int(input("Enter the ending index: "))


# maxi = l[in1]
# mini = l[in1]

# for i in range(in1, in2+1):
#     if l[i] < mini:
#         mini = l[i]
#     else:
#         mini = mini
    
#     if l[i] > maxi:
#         maxi = l[i]
#     else:
#         maxi = maxi


# print(f"The maximum value of the specified index {in1}-{in2} is {maxi}")
# print(f"The minimum value of the specified index {in1}-{in2} is {mini}")



"""
Q4) Write a Program to move all the duplicate values of the list to the end of the list.

L = [ 45, 52, 65, 89, 45, 25, 45, 52, 35, 65, 89, 54, 21, 57, 33, 61, 50 ]

Output:
The List before modification is [ 45, 52, 65, 89, 45, 25, 45, 52, 35, 65, 89, 54, 21, 57, 33, 61, 50 ]

The List after modification is [ 25, 35, 54, 21, 57, 33, 61, 50, 45, 45, 45,  52, 52, 65, 65, 89, 89 ]

"""


# l = [ 45, 52, 65, 89, 45, 25, 45, 52, 35, 65, 89, 54, 21, 57, 33, 61, 50 ]
# print(f'The list before modification is {l}')
# l2 =[]
# l3 = []


# for i in l:
#     num_count = l.count(i)
#     if num_count > 1:
#         if i in l3:
#             continue
#         else:
#             for j in range(num_count):
#                 l3.append(i)

#     else:
#         l2.append(i)

# print(f"The list after modification is {l2+l3}")



'''
Q) Write a Program to read two lists Num and Denum which contains the Numerators and Denominators 
of some fractions at the respective indexes. Then Display the Smallest Fraction along with it's index.

num = [12,24,35,32,45,11,7]
denum = [2,5,3,8,9,7,5]

Output: 

Smallest Faction is 7/5 which is at index 6.
'''





# num = [12,24,35,32,45,11,7]
# denum = [2,5,3,8,9,7,5]
# numerator = 0
# denominator = 0
# smallest_frac = num[0]/denum[0]
# for i in range(len(num)):
#     if num[i] / denum[i] < smallest_frac:
#         numerator = num[i]
#         denominator = denum[i]
#         smallest_frac = num[i]/denum[i]
       
        
#     else:
#         smallest_frac = smallest_frac
#         numerator = numerator
#         denominator = denominator
# print(f"Smallest Fraction in the list is {smallest_frac} \
# ({numerator}/{denominator}) at index {i}")












"""
Q) Write a Program to compare two equal sized lists and print the first index where they differ.
l = [12,54,24,75,35,21,65,57,21,34]
l2 = [12,54,24,75,35,21,75,21,35,87]

Output:
The two Lists differ at Index 6.
"""















"""
Q) Write a Python program to find the list of words that are longer than n from a given list of words, where n is the 
length of the specified word by the user.

l = ["Apurba","Raima","Ruhi","Himangshu","Aniruddha","Rupankar","Arunadaya","Pritha","Pronob"]

Output:
Enter the Word: hellog

The List of words which are longer than the Specified word hellog are:-
1) Himangshu
2) Aniruddha
3) Rupankar
4) Arunadaya

"""



















"""
Q) Write a Python program to select an item randomly from a list.

l = ["Python","Java","C++","C","Ruby","Django","Flask","ReactNative","Mern Stack","JavaScript","TypeScript"]

Output:
The Random Choice of the given list is C++.
"""




























