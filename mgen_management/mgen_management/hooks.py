app_name = "mgen_management"
app_title = "Mgen Management"
app_publisher = "Fat7allah"
app_description = "Mgen Management"
app_email = "fat7allah.habbani@gmail.com"
app_license = "MIT"

fixtures = [
    {
        "doctype": "Profession",
        "filters": [["doctype", "=", "Profession"]]
    },
    {
        "doctype": "Specialization",
        "filters": [["doctype", "=", "Specialization"]]
    },
    {
        "doctype": "Structure",
        "filters": [["doctype", "=", "Structure"]]
    },
    {
        "doctype": "Region",
        "filters": [["doctype", "=", "Region"]]
    },
    {
        "doctype": "Province",
        "filters": [["doctype", "=", "Province"]]
    }
]
