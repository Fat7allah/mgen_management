// Copyright (c) 2025, Fat7allah and contributors
// For license information, please see license.txt

frappe.query_reports["Cards Report"] = {
    "filters": [
        {
            "fieldname": "region",
            "label": __("الجهة"),
            "fieldtype": "Link",
            "options": "Region"
        },
        {
            "fieldname": "province",
            "label": __("الإقليم"),
            "fieldtype": "Link",
            "options": "Province",
            "get_query": function() {
                var region = frappe.query_report.get_filter_value('region');
                if(region) {
                    return {
                        filters: {
                            'region': region
                        }
                    };
                }
            }
        },
        {
            "fieldname": "academic_year",
            "label": __("الموسم الدراسي"),
            "fieldtype": "Data"
        }
    ]
};
