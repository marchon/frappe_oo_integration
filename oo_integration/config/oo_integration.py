from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": _("Pages"),
            "items": [
                {
                    "type": "page",
                    "name": "flow-launcher",
                    "label": _("Flow Launcher")
                }
            ]
        },
        {
               "label": _("Run Management"),
               "items": [
                   {
                       "type": "doctype",
                       "label": _("Run Explorer"),
                       "name": "OO Flow Execution"
                   }
               ]
        },
        {
            "label": _("Setup"),
            "items": [
                {
                    "type": "doctype",
                    "label": _("OO Setup"),
                    "name": "OO Setup"
                },
                {
                    "type": "doctype",
                    "label": _("OO Flow Mapping"),
                    "name": "OO Flow"
                }
            ]
        }
    ]