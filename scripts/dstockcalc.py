#!/usr/bin/python

# Script takes in 2 args stock value and dividends value
# calculates the APR with a 2k investment over a course of a year
import sys

def calcAPR(stock, div):
    shares = int(int(sys.argv[1]) / stock)
    apr = shares * div * 4
    print "${0:.2f}".format(apr)
    print "APY {0:.2f}".format((apr/int(sys.argv[1])*100.0))

stock = float(sys.argv[2])
div = float(sys.argv[3])
calcAPR(stock, div)
