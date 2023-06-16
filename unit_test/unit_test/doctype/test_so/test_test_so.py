# Copyright (c) 2023, Nihantra C. Patel and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


def create_so():
    for i in range(350):
        new_so = frappe.new_doc("Sales Order")
        new_so.customer = "Customer 2"
        new_so.delivery_date = "2023-06-30"
        new_so.append('items', {
            'item_code': "Item 1",
            'item_name': "Item 1",
            'qty': 1,
            'rate': 100
        })
        new_so.docstatus = 1
        new_so.save()


class TestTestSO(FrappeTestCase):
    create_so()