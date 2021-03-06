'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# runtime = 0(n)
def sliding_window_max(nums, k):
    # Your code here

    y = []
    a = 0
    while (k+a) <= len(nums):
        x = max(nums[a:(k+a)])
        y.append(x)
        a+=1

    return y


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
