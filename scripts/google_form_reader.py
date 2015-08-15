#!/bin/python
# This script is used to count up the meeting times
# to determine the best meeting time for our team project
# which is from a google form
import sys

# setting up meeting times
meeting_times = [
    'Tuesday 8/18/15 @ 6pm',
    'Tuesday 8/18/15 @ 8pm',
    'Wednesday 8/19/15 @ 6pm',
    'Wednesday 8/19/15 @ 8pm',
    'Thursday 8/20/15 @ 6pm',
    'Thursday 8/20/15 @ 8pm',
    'Friday 8/21/15 @ 6pm',
    'Friday 8/21/15 @ 8pm',
    'Sunday 8/23/15 @ 6pm',
    'Sunday 8/23/15 @ 8pm',
    'None of these times work for me :( (Let a lead know)',]

# read file
f = open(sys.argv[1], 'r')
#print "Now reading file {}".format(f)

# create map of meeting times and counts
meeting_count = dict()
for time in meeting_times:
    meeting_count[time]=0

# iterate through poll votes and tallys them
for line in f:
    for time in meeting_times:
        if time in line:
            meeting_count[time] += 1

# find best meeting time
max = 0
best_meeting_time = ''
for time in meeting_count:
    if meeting_count[time] > max:
        max = meeting_count[time]
        best_meeting_time = time

print "The best meeting time is {} with a total vote of {}".format(
    best_meeting_time,
    max,
)
