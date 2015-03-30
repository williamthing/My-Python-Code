#!/usr/bin/python
# William Thing
#
# This script will print the local time
# and display a calendar. Currently set print
# March 2015 Calendar.

import time
import calendar

localtime = time.asctime(time.localtime(time.time()))
print "Local current time :", localtime

cal = calendar.month(2015, 3)
print "Here is the calendar:"
print cal;
