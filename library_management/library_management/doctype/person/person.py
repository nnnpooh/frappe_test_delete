# Copyright (c) 2025, CMU and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class person(Document):
    def before_save(self):
        frappe.msgprint("Hello")
        a = 10
        doc = frappe.get_doc(
            {
                "doctype": "Item",
                "item_code": "NEW-ITEM-002",
                "item_group": "Products",  # Replace with your item group
                "item_name": "Sample Item",
                "stock_uom": "Nos",  # Replace with your UoM
                # Add more fields as needed
            }
        )

        doc.save(ignore_permissions=True)
