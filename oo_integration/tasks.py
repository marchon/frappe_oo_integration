import frappe

def update_executions():
    frappe.log("Start Updating Executions")
    frappe.get_all("OO Flow Execution", fields=["name", "status"],filters=[["status","in",[   "RUNNING",
                                                                    "PAUSED",
                                                                    "PAUSED_USER_PAUSED",
                                                                    "PAUSED_INPUT_REQUIRED",
                                                                    "PAUSED_INPUT_REQUIRED_MANUAL_OP",
                                                                    "PAUSED_DISPLAY",
                                                                    "PAUSED_GATED_TRANSITION",
                                                                    "PAUSED_HAND_OFF",
                                                                    "PAUSED_INTERRUPT",
                                                                    "PAUSED_NO_WORKERS_IN_GROUP",
                                                                    "PAUSED_BRANCH_PAUSED"]]])

    frappe.log("Finish Updating Executions")