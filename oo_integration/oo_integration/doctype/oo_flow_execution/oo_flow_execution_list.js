/**
 * Created by pau on 06/05/2017.
 */

frappe.listview_settings['OO Flow Execution'] = {
    colwidths: {"indicator": 1, "subject": 2},
    add_fields: ["status"],
    get_indicator: function (doc) {
        if(["RUNNING"].includes(doc.status)){
            return [doc.status, "grey", "status,=," + doc.status];
        }
        else if([   "SYSTEM_FAILURE",
                    "COMPLETED_ERROR",
                    "CANCELED"].includes(doc.status)){
            return [doc.status, "red", "status,=," + doc.status];
        }
        else if([   "COMPLETED",
                    "COMPLETED_RESOLVED",
                    "COMPLETED_DIAGNOSED",
                    "COMPLETED_NO_ACTION_TAKEN",
                    "COMPLETED_CUSTOM"].includes(doc.status)){
            return [doc.status, "green", "status,=," + doc.status];
        }
        else if(    ["PAUSED",
                    "PAUSED_USER_PAUSED",
                    "PAUSED_INPUT_REQUIRED",
                    "PAUSED_INPUT_REQUIRED_MANUAL_OP",
                    "PAUSED_DISPLAY",
                    "PAUSED_GATED_TRANSITION",
                    "PAUSED_HAND_OFF",
                    "PAUSED_INTERRUPT",
                    "PAUSED_NO_WORKERS_IN_GROUP",
                    "PAUSED_BRANCH_PAUSED"].includes(doc.status)){
            return [doc.status, "blue", "status,=," + doc.status];
        }
    }
};