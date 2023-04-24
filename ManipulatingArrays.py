import numpy as np

#Generating a random 2 dimensional 5x5 array
array = np.random.randint(1,26, size=(5,5), dtype=int)

#Printing the entire array
print(array)



#print the item in row 2 column 3
print(array[1][2])

#sum and then print the sum of entire array
summer = np.sum(array)
print(summer)

#printing the mean of the array
mean = np.mean(array, axis=1)
print(mean)

#Printing Maximum value in each column
max = np.max(array, axis=0)
print(max)