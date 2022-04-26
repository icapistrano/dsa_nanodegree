"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".

Read file into texts and calls.
It's ok if you don't understand how to read files
"""

import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def update_total(num, duration):
    if num not in total:
        total[num] = duration
    
    else:
        total[num] += duration

if __name__ == "__main__":
    total = {}
    max_num, max_duration = "", 0

    for outgoing_num, recv_num, start_time, duration in calls:
        duration = int(duration)

        update_total(outgoing_num, duration)
        update_total(recv_num, duration)

        if total[outgoing_num] > total[recv_num] and total[outgoing_num] > max_duration:
            max_duration = total[outgoing_num]
            max_num = outgoing_num

        elif total[recv_num] > total[outgoing_num] and total[recv_num] > max_duration:
            max_duration = total[recv_num]
            max_num = recv_num

    longest_msg = "{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_num, max_duration)
    print(longest_msg)


