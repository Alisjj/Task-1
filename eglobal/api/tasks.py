import frappe
from frappe import _


@frappe.whitelist(allow_guest=False)
def create_task(title, description, status="Open", due_date=None):
    task = frappe.get_doc({
        "doctype": "Task",
        "title": title,
        "description": description,
        "status": status,
        "due_date": due_date
    })
    task.insert()
    return task.as_dict()


@frappe.whitelist(allow_guest=False)
def get_tasks(task_id):
    task = frappe.get_doc("Task", task_id)
    return task.as_dict()


@frappe.whitelist(allow_guest=False)
def update_task(task_id, title=None, description=None, status=None, due_date=None):
    task = frappe.get_doc("Task", task_id)
    if title:
        task.title = title
    if description:
        task.description = description
    if status:
        task.status = status
    if due_date:
        task.due_date = due_date
    task.save()
    return task.as_dict()

@frappe.whitelist(allow_guest=False)
def delete_task(task_id):
    frappe.delete_doc("Task", task_id)
    return {"message": f"Task {task_id} deleted"}