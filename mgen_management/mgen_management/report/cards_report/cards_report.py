# Copyright (c) 2025, Fat7allah and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {
            "fieldname": "region",
            "label": _("الجهة"),
            "fieldtype": "Link",
            "options": "Region",
            "width": 200
        },
        {
            "fieldname": "province",
            "label": _("الإقليم"),
            "fieldtype": "Link",
            "options": "Province",
            "width": 200
        },
        {
            "fieldname": "academic_year",
            "label": _("الموسم الدراسي"),
            "fieldtype": "Data",
            "width": 120
        },
        {
            "fieldname": "cards_count",
            "label": _("عدد البطاقات"),
            "fieldtype": "Int",
            "width": 120
        },
        {
            "fieldname": "total_amount",
            "label": _("المجموع"),
            "fieldtype": "Currency",
            "width": 120
        },
        {
            "fieldname": "paid_amount",
            "label": _("الأداء"),
            "fieldtype": "Currency",
            "width": 120
        },
        {
            "fieldname": "remaining_amount",
            "label": _("الباقي"),
            "fieldtype": "Currency",
            "width": 120
        },
        {
            "fieldname": "office_share",
            "label": _("حصة المكتب (50%)"),
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "fieldname": "region_share",
            "label": _("حصة الجهة (20%)"),
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "fieldname": "province_share",
            "label": _("حصة الاقليم (30%)"),
            "fieldtype": "Currency",
            "width": 150
        }
    ]

def get_data(filters):
    conditions = " WHERE type = 'بطائق'"
    if filters:
        if filters.get("region"):
            conditions += f" AND region = '{filters.get('region')}'"
        if filters.get("province"):
            conditions += f" AND province = '{filters.get('province')}'"
        if filters.get("academic_year"):
            conditions += f" AND academic_year = '{filters.get('academic_year')}'"

    # Get income data for cards
    income_data = frappe.db.sql(f"""
        SELECT 
            region,
            province,
            academic_year,
            SUM(quantity) as cards_count,
            SUM(amount) as paid_amount
        FROM `tabIncome`
        {conditions}
        GROUP BY region, province, academic_year
    """, as_dict=1)

    # Calculate derived values
    for row in income_data:
        # Total amount (cards_count * 100 MAD)
        row.total_amount = row.cards_count * 100
        
        # Remaining amount
        row.remaining_amount = row.total_amount - row.paid_amount
        
        # Share calculations
        row.office_share = row.total_amount * 0.5  # 50%
        row.region_share = row.total_amount * 0.2  # 20%
        row.province_share = row.total_amount * 0.3  # 30%

    return income_data
