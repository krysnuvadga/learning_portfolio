def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j] < arr[minimum]:
                minimum = j

        # Place it at the front of the
        # sorted end of the array
        arr[i], arr[minimum] = arr[minimum], arr[i]

    print("The Sorted array is:")
    for i in range(len(arr)):
        print(" %d" %arr[i])

lst = [64, 25, 12, 22, 11]
selection_sort(lst)
