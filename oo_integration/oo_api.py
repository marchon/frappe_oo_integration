import requests
from base64 import encodestring
import json
import frappe
from frappe import _
from requests.auth import HTTPBasicAuth


@frappe.whitelist()
def run_flow_frappe(uuid,inputs=None,run_name=None):
    oo_config = frappe.get_doc("OO Setup")
    url = oo_config.url
    username = oo_config.username
    password = oo_config.get_password()

    executionId =  run_flow(url, uuid, username, password, inputs, run_name)

    doc = frappe.new_doc("OO Flow Execution")

    print run_name
    doc.update({
        "oo_flow": uuid,
        "run_name": run_name,
        "execution_id": executionId
    })

    inputs = json.loads(inputs)
    for input in inputs.keys():
        doc.append("inputs", {
            "input_name": input,
            "value": inputs[input]
        })

    doc.save()

    return executionId


def run_flow(oo_url, uuid, user, password, inputs,run_name=None):
    post_data = {}
    post_data['uuid'] = uuid
    post_data['runName'] = run_name
    post_data['logLevel'] = 'DEBUG'
    if (inputs is not None):
        post_data['inputs'] = json.loads(inputs)

    json_post = json.dumps(post_data)

    # run the flow
    url = oo_url+'/rest/v1/executions'
    headers = {
        'Content-type': 'application/json',
    }
    r = requests.post(url, data=json_post, verify=False, headers=headers, auth=HTTPBasicAuth(user, password))

    if (r.reason != 'Created'):
        frappe.throw(_("Error Runnning Flow"), r.reason)

    else:
        response = json.loads(r.text)
        frappe.log(response)
        return response['executionId']

def get_run_summary(execution_id):
    results = get_run_summary_list(execution_id)
    return results[0]

def get_run_summary_list(executions_id):
    # run the flow
    oo_config = frappe.get_doc("OO Setup")
    oo_url = oo_config.url
    username = oo_config.username
    password = oo_config.get_password()

    url = oo_url+'/rest/v1/executions/'+executions_id+'/summary'
    headers = {
        'Content-type': 'application/json',
    }
    r = requests.get(url, verify=False, headers=headers, auth=HTTPBasicAuth(username, password))

    if r.status_code != 200:
        frappe.throw(title=_("Error Getting Status Flow"), msg=r.text)

    else:
        response = json.loads(r.text)
        return response

def get_flow_inputs(uuid):
    # run the flow
    oo_config = frappe.get_doc("OO Setup")
    oo_url = oo_config.url
    username = oo_config.username
    password = oo_config.get_password()

    url = oo_url + '/rest/v1/flows/' + uuid + '/inputs'
    headers = {
        'Content-type': 'application/json',
    }
    r = requests.get(url, verify=False, headers=headers, auth=HTTPBasicAuth(username, password))

    if r.status_code != 200:
        frappe.throw(title=_("Error Getting Status Flow"), msg=r.text)

    else:
        response = json.loads(r.text)
        return response

def get_flow_execution_log(execution_id):
    # run the flow
    oo_config = frappe.get_doc("OO Setup")
    oo_url = oo_config.url
    username = oo_config.username
    password = oo_config.get_password()

    url = oo_url + '/rest/v1/executions/' + execution_id + '/execution-log'
    headers = {
        'Content-type': 'application/json',
    }
    r = requests.get(url, verify=False, headers=headers, auth=HTTPBasicAuth(username, password))

    if r.status_code != 200:
        frappe.throw(title=_("Error Getting Status Flow"), msg=r.text)

    else:
        response = json.loads(r.text)
        return response