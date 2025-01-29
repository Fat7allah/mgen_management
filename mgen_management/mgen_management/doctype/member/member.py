# Copyright (c) 2025, Fat7allah and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Member(Document):
    def validate(self):
        """Validate member data before saving"""
        self.validate_email()
        self.validate_phone()
        self.validate_province_region()

    def validate_email(self):
        """Ensure email is in valid format"""
        if not self.email:
            return
        
        import re
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            frappe.throw("البريد الإلكتروني غير صالح")

    def validate_phone(self):
        """Ensure phone number is in valid format"""
        if not self.phone:
            return
        
        import re
        if not re.match(r"^[+]?[\d\s-]{8,}$", self.phone):
            frappe.throw("رقم الهاتف غير صالح")

    def validate_province_region(self):
        """Ensure province belongs to selected region"""
        if not self.province or not self.region:
            return
            
        province_doc = frappe.get_doc("Province", self.province)
        if province_doc.region != self.region:
            frappe.throw("الإقليم لا ينتمي إلى الجهة المختارة")
