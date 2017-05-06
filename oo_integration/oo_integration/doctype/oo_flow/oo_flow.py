# -*- coding: utf-8 -*-
# Copyright (c) 2017, Pau Rosello and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from oo_integration.oo_api import run_flow_frappe

class OOFlow(Document):
	def run_flow(self,inputs):
		return run_flow_frappe(self.uuid, inputs, self.flow_name)