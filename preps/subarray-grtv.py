# Python3 implementation of the approach

# Function that returns the sub-array
def findSubarray(a, k, n):

    # Data-structure to store all
    # the sub-arrays of size K
    vec=[]

    # Iterate to find all the sub-arrays
    for i in range(n-k+1):
        temp=[]

        # Store the sub-array elements in the array
        for j in range(i,i+k):
            temp.append(a[j])

        # Push the vector in the container
        vec.append(temp)

    # Sort the vector of elements
    vec=sorted(vec)

    # The last sub-array in the sorted order
    # will be the answer
    return vec[len(vec) - 1]

# Driver code

a =[ 1, 4, 3, 2, 5 ]
k = 4
n = len(a)

# Get the sub-array
ans = findSubarray(a, k, n)

for it in ans:
    print(it,end=" ")

# This code is contributed by mohit kumar 29 
