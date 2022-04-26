def rotated_array_search(arr, target):
    if not isinstance(arr, list):
        return -1

    if len(arr) == 0:
        return -1

    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        # left portion
        if arr[left] <= arr[mid]:

            # search right half
            if arr[mid] < target or target < arr[left]:
                left = mid + 1

            # search left half
            else:
                right = mid - 1

        # right portion
        else:

            # search left half
            if arr[mid] > target or target > arr[right]:
                right = mid - 1

            # search right half
            else:
                left = mid + 1

    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(arr, target):
    if linear_search(arr, target) == rotated_array_search(arr, target):
        print("Pass")
    else:
        print("Fail")




test_function([6, 7, 8, 9, 10, 1, 2, 3, 4], 6)
# Expected output: 0

test_function([6, 7, 8, 9, 10, 1, 2, 3, 4], 1)
# Expected output: 5

test_function([6, 7, 8, 1, 2, 3, 4], 5)
# Expected output: -1

test_function([1], 100)
# Expected output: -1

test_function([], 1)
# Expected output: -1
