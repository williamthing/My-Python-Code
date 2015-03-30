#!/usr/bin/python
# William Thing
#
# This script will print the local time
# and display a calendar based on local time

import time
import calendar

localtime = time.asctime(time.localtime(time.time()))
print "Local current time :", localtime

lst = localtime.split()
month_str = ['Jan', 'Feb', 'Mar', 'Apr', 'May', "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]	

month = month_str.index(lst[1]) + 1
year = int(lst[len(lst)-1])
cal = calendar.month(year, month)
print "Here is the calendar:"
print cal;
