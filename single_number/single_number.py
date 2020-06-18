'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # create a list of all values, if value is already in list then delete it from the list
    #vals = []
    #vals2 = []
    #i = 0
    for i in range(0,len(arr)-1):
        if arr[i+1] == arr[i]:
            arr.pop(i)

        elif arr[i+1] != arr[i]:
            return arr[i]

        


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")