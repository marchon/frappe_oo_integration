# -*- coding: utf-8 -*-
# Copyright (c) 2017, Pau Rosello and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from oo_integration.oo_api import get_run_status

class OOFlowExecution(Document):
	def update_status(self):
		oo_config = frappe.get_doc("OO Setup")
		url = oo_config.url
		username = oo_config.username
		password = oo_config.password

		status = get_run_status(url, username, password, self.execution_id)

		self.status = status["status"]
		self.save()
