'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):

    if len(arr) == 0:
        return arr
    
    for number in arr:
        if number == 0:
            arr.remove(number)
            arr.append(number)
 
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")