#!/usr/bin/python

import sys
from orders.models import Order

"""
Always Approve Order hook

This hook will approve all orders.
"""

def run(order, job=None, logger=None):
    order.approve()
    return "", "", ""

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("usage: {} <CloudBolt order id>\n".format(sys.argv[0]))
    order_id = sys.argv[1]
    order = Order.objects.get(pk=order_id)
    status, msg, err = run(order)
