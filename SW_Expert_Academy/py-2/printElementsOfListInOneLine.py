# using for loop
a = [1,2,3,4]
for x in range(len(a)):
  print(a[x], end=" ") #1 2 3 4
  
# using * operator separated by space
print("\n",*a) #1 2 3 4

# using * operator and sep operator
print(*a, sep=", ") #1, 2, 3, 4

'''
# using join function
print(''.join(a))
'''

# converting into string
print(str(a)[1:-1]) #1, 2, 3, 4

# using map
print(' '.join(map(str, a))) #1 2 3 4
