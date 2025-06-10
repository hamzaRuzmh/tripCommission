import frappe

def execute():
    if frappe.db.exists("Custom Field", "Employee-custom_employee_trip_commission"):
        frappe.delete_doc("Custom Field", "Employee-custom_employee_trip_commission")