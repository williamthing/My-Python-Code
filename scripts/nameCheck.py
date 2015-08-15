name.endswith("zyx"):#!/usr/bin/python

import sys
from orders.models import Order

"""
This script will see if a order contains a "ALERT" in it's name and if it does
then it will auto-approve if it ends in "xyz" and auto-deny if it ends in "zyx".
"""

def run(order, job=None, logger=None):
    name = order.name
    if "ALERT" in name:
        if "xyz" in name:
            order.approve()
        elif "zyx" in name:
            order.deny()

    return "", "", ""

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("usage: {} <CloudBolt order id>\n".format(sys.argv[0]))
    order_id = sys.argv[1]
    order = Order.objects.get(pk=order_id)
    status, msg, err = run(order)
