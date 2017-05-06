import frappe
from oo_api import get_run_summary_list


def update_executions():
    frappe.log("Start Updating Executions")
    pending_executions = frappe.get_all("OO Flow Execution",    fields=["name", "status"],
                                                                filters=[["status","in",[
                                                                    "RUNNING",
                                                                    "PAUSED",
                                                                    "PAUSED_USER_PAUSED",
                                                                    "PAUSED_INPUT_REQUIRED",
                                                                    "PAUSED_INPUT_REQUIRED_MANUAL_OP",
                                                                    "PAUSED_DISPLAY",
                                                                    "PAUSED_GATED_TRANSITION",
                                                                    "PAUSED_HAND_OFF",
                                                                    "PAUSED_INTERRUPT",
                                                                    "PAUSED_NO_WORKERS_IN_GROUP",
                                                                    "PAUSED_BRANCH_PAUSED"
                                                                ]]])

    if len(pending_executions)==0:
        return

    executions_dict = {}
    for item in pending_executions:
        name = item['name']
        executions_dict[name] = item["status"]

    executions_id = ",".join(executions_dict.keys())

    results = get_run_summary_list(executions_id)

    for item in results:
        if item["executionId"] in executions_dict and item['status']!=executions_dict[item["executionId"]]:
            execution = frappe.get_doc("OO Flow Execution", item["executionId"])
            execution.status = item['status']
            if execution.status == "COMPLETED":
                execution.update_outputs()
                execution.save()

    frappe.db.commit()

    frappe.log("Finish Updating Executions")