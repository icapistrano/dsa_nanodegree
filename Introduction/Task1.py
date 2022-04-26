"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."

Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def unique_nums(numbers):
    unique_nums = set()
    for row in numbers:
        unique_nums.add(row[0])
        unique_nums.add(row[1])

    return unique_nums


if __name__ == "__main__":
    nums = set()

    text_nums = unique_nums(texts)
    nums.update(text_nums)

    call_nums = unique_nums(calls)
    nums.update(call_nums)

    total_nums = "There are {} different telephone numbers in the records.".format(len(nums))
    print(total_nums)
