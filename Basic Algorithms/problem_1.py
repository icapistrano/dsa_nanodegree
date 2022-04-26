def sqrt(number):
    if not isinstance(number, int):
        print(f"TypeError: expected <class int>, got {type(number)}")
        return number

    left, right = 0, number

    while left <= right:
        mid = (left + right) // 2
        mid_sum = mid * mid

        if mid_sum > number:
            right = mid - 1

        elif mid_sum < number:
            left = mid + 1

        else:
            return mid

    return right


def test_case(test_num, expected):
    if sqrt(test_num) == expected:
        print("Pass")
    else:
        print("Fail")


test_case(9, 3)
# Expected output: 3

test_case(0, 0)
# Expected output: 0

test_case(1, 1)
# Expected output: 1

test_case(27, 5)
# Expected output: 5

test_case(None, None)
# prints TypeError message, expected None