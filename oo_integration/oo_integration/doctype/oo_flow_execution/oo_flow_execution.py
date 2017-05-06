# -*- coding: utf-8 -*-
# Copyright (c) 2017, Pau Rosello and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from oo_integration.oo_api import get_run_summary, get_flow_execution_log
import json

class OOFlowExecution(Document):
	def update_status(self):
		status = get_run_summary(self.execution_id)
		self.status = status["status"]
		self.save()

	def update_outputs(self):
		outputs = self.get_outputs()
		output_keys_frappe = [x.output_name for x in self.outputs]
		for output_name in outputs.keys():
			if output_name not in output_keys_frappe and outputs[output_name]!='':
				self.append("outputs", {
					"output_name": output_name,
					"value": outputs[output_name]
				})
		self.save()

	def get_outputs(self):
		execution_log = get_flow_execution_log(self.execution_id)
		return execution_log["flowOutput"]