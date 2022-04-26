def get_min_max(ints):
   low, high = ints[0], ints[0]

   for num in ints:
      if num < low:
         low = num
      elif num > high:
         high = num

   return low, high

def test_case(num_array):
   if len(num_array) == 0:
      print("ValueError: array is empty")
      return
   
   elif False in [isinstance(i, int) for i in num_array]:
      print("TypeError: invalid array")
      return

   if get_min_max(num_array) == (min(num_array), max(num_array)):
      print("Pass")
   else:
      print("Fail")


test_case([9, 2, 7, 3, 0])
# output (0, 9)

test_case([-2, 0, 10, 7, 11, 3, 2, 5])
# output (-2, 11)

test_case([17, 0, 2, 11, 19, 100, 4])
# output (0, 100)

test_case([5])
# output (5, 5)

test_case([])
# ValueError handled by test case for empty array

test_case([None])
# TypeError handled by test case for invalid item in array