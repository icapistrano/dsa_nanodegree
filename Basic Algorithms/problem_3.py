def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    sorted_left = mergesort(arr[:mid])
    sorted_right = mergesort(arr[mid:])

    return merge(sorted_left, sorted_right)

def merge(left_arr, right_arr):
    merged = []
    i, j = 0, 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] > right_arr[j]:
            merged.append(left_arr[i])
            i += 1
        
        else:
            merged.append(right_arr[j])
            j += 1

    merged += left_arr[i:]
    merged += right_arr[j:]

    return merged

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    # edge case 1: 
    if len(input_list) <= 1:
        return input_list

    sorted_arr = mergesort(input_list)

    i, j = 0, 1
    first, second = [], []

    while i < len(sorted_arr):
        first.append(str(sorted_arr[i]))

        if j < len(sorted_arr):
            second.append(str(sorted_arr[j]))

        i += 2
        j += 2
    
    return [int("".join(first)), int("".join(second))]


def test_function(input_arr, solution):
    for item in input_arr:
        if not isinstance(item, int):
            print(f"TypeError: expected <class int>, got {type(item)}")
            return 

    output = rearrange_digits(input_arr)
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

    return output

test_case1 = test_function([1, 2, 3, 4, 5], [542, 31])
# returns [531, 42], but sum equal to [542, 31]

test_case2 = test_function([4, 6, 2, 5, 9, 8], [964, 852])
# returns [964, 852]

test_case3 = test_function([], [])
# returns []

test_case3 = test_function([1], [1])
# returns [1]

test_case4 = test_function([None], [])
# prints TypeError handled by test function
