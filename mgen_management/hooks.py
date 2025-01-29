# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "mgen_management"
app_title = "Mgen Management"
app_publisher = "Fat7allah"
app_description = "Mgen Management"
app_email = "fat7allah.habbani@gmail.com"
app_license = "MIT"

fixtures = [
    {"dt": "DocType", "filters": [
        [
            "name", "in", [
                "Profession",
                "Specialization",
                "Structure",
                "Region",
                "Province",
                "Education Level"
            ]
        ]
    ]}
]
