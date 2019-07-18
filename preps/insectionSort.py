def insectionSort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        position = i

        while position > 0 and arr[position-1] > cursor:

            # Swap the number down the list
            arr[position] = arr[position-1]
            position = position-1

        # Break and do the final swap
        arr[position] = cursor
    print("Sorted array is:")
    for i in range(len(arr)):
        print("%d" %arr[i])

lst = [64, 25, 12, 22, 11]
insectionSort(lst)
