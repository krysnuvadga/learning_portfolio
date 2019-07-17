# Returns true if the
# there is a subarray
# of arr[] with sum
# equal to 'sum'
# otherwise returns
# false. Also, prints
# the result
def subArraySum(arr, n, sum):

    # Pick a starting
    # point
    for i in range(n):
        curr_sum = arr[i]

        # try all subarrays
        # starting with 'i'
        j = i+1
        while j <= n:

            if curr_sum == sum:
                print ("Sum found in the sub subarray")
                print(arr[i:j])

                return 1

            if curr_sum > sum or j == n:
                break

            curr_sum = curr_sum + arr[j]
            j += 1

    print ("No subarray found")
    return 0

arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum = 2000

subArraySum(arr, n, sum)
