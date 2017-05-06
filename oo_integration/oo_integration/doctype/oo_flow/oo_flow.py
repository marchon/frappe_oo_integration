# -*- coding: utf-8 -*-
# Copyright (c) 2017, Pau Rosello and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from oo_integration.oo_api import run_flow_frappe, get_flow_inputs

class OOFlow(Document):

	def before_save(self):
		self.get_flow_inputs_from_oo()

	def run_flow(self,inputs):
		return run_flow_frappe(self.name, inputs, self.flow_name)

	def get_flow_inputs(self):
		self.get_flow_inputs_from_oo()
		self.save()

	def get_flow_inputs_from_oo(self):
		inputs_oo =  get_flow_inputs(self.name)
		defined_inputs = [i.input_name for i in self.inputs]

		for input in inputs_oo:
			if input["name"] not in defined_inputs:
				mandatory=0
				if input["mandatory"]:
					mandatory=1

				self.append("inputs",{
					"input_name": input["name"],
					"label": input["name"],
					"mandatory": mandatory,
					"input_type": "Data"
				})