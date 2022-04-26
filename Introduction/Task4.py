"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.

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


if __name__ == "__main__":
    callers = set([row[0] for row in calls])

    recv_call_nums = set([row[1] for row in calls])
    send_text_nums = set([row[0] for row in texts])
    recv_text_nums = set([row[1] for row in texts])

    nums_to_avoid = set()
    for nums in [recv_call_nums, send_text_nums, recv_text_nums]:
        nums_to_avoid.update(nums)

    telemarketers = callers.difference(nums_to_avoid)

    print("These numbers could be telemarketers: ")
    for num in sorted(telemarketers):
        print(num)
    