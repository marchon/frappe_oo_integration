# -*- coding: utf-8 -*-
# Copyright (c) 2017, Pau Rosello and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils.scheduler import enable_scheduler
from frappe import _

class OOSetup(Document):
	def enable_scheduler(self):
		enable_scheduler()
		frappe.msgprint(_("Scheduler Enabled"))