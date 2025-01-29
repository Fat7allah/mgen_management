# Copyright (c) 2025, Fat7allah and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Expense(Document):
    def validate(self):
        # Validate that province belongs to selected region
        if self.region and self.province:
            province_doc = frappe.get_doc("Province", self.province)
            if province_doc.region != self.region:
                frappe.throw(f"الإقليم {self.province} لا ينتمي إلى الجهة {self.region}")
