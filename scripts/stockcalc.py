#!/usr/bin/python

# Script takes in 2 args stock value and dividends value
# calculates the APR with a 2k investment over a course of a year
import sys

def calcAPR(stock, div):
    shares = int(2000 / stock)
    apr = shares * div * 4
    print "${0:.2f}".format(apr)

stock = float(sys.argv[1])
div = float(sys.argv[2])
calcAPR(stock, div)
