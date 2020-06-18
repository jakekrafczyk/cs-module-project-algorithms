'''
Input: a List of integers
Returns: a List of integers

Write a function that takes an array of integers and moves each non-zero integer to the
left side of the array, then returns the altered array. The order of the non-zero integers
does not matter in the mutated array.
'''
def moving_zeroes(arr):
    # Your code here
    # move through the array and identify zeroes, then swap them

    a = 0

    for i in range(0,len(arr)):
        if arr[i] != 0:
            #place at index a
            arr[a] = arr[i]
            a += 1

    #fill in rest of array with 0s
    while a < len(arr):
        arr[a] = 0
        a += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")