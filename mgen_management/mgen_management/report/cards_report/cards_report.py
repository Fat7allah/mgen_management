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
            "label": _("حصة الجامعة "),
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "fieldname": "region_share",
            "label": _("حصة الجهة "),
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "fieldname": "province_share",
            "label": _("حصة الاقليم "),
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

    # Get expense data for cards (total cards and amount)
    expense_data = frappe.db.sql(f"""
        SELECT 
            region,
            province,
            academic_year,
            SUM(quantity) as cards_count,
            SUM(amount) as total_amount
        FROM `tabExpense`
        {conditions}
        GROUP BY region, province, academic_year
    """, as_dict=1)

    # Get income data for cards (paid amount)
    income_data = frappe.db.sql(f"""
        SELECT 
            region,
            province,
            academic_year,
            SUM(amount) as paid_amount
        FROM `tabIncome`
        {conditions}
        GROUP BY region, province, academic_year
    """, as_dict=1)

    # Create a dictionary to easily lookup income data
    income_lookup = {}
    for row in income_data:
        key = (row.region, row.province, row.academic_year)
        income_lookup[key] = row.paid_amount

    # Combine data and calculate derived values
    result = []
    for row in expense_data:
        key = (row.region, row.province, row.academic_year)
        paid_amount = income_lookup.get(key, 0)
        
        # Calculate remaining amount
        remaining_amount = row.total_amount - paid_amount
        
        # Calculate shares based on cards_count
        office_share = row.cards_count * 50  # 50 MAD per card
        region_share = row.cards_count * 20  # 20 MAD per card
        province_share = row.cards_count * 30  # 30 MAD per card

        result.append({
            "region": row.region,
            "province": row.province,
            "academic_year": row.academic_year,
            "cards_count": row.cards_count,
            "total_amount": row.total_amount,
            "paid_amount": paid_amount,
            "remaining_amount": remaining_amount,
            "office_share": office_share,
            "region_share": region_share,
            "province_share": province_share
        })

    return result
