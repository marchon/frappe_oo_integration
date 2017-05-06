frappe.pages['flow-launcher'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Flow Launcher',
		single_column: true
	});

	$(frappe.render_template('flow_launcher')).appendTo(page.body);
	page.content = $(page.body).find('.filter-area');

	var flow = frappe.ui.form.make_control({
		parent: $(".flow"),
		df: {
			fieldtype: "Link",
			options: "OO Flow",
			fieldname: "flow",
			placeholder: __("OO Flow"),
            label: __("OO Flow"),
            reqd:1,
			change: function(){
				frappe.call({
					method: "frappe.client.get",
					args: {
						doctype: "OO Flow",
						name: flow.get_value()
					},
					callback: function(r) {
						if(r.message) {
							flow_doc = r.message
							flow_name.set_value(flow_doc.flow_name)
						}
					}
				});
			}
		}
	});
	flow.refresh();
	frappe.pages['flow-launcher'].flow = flow;

	var flow_name = frappe.ui.form.make_control({
		parent: $(".flow-name"),
		df: {
			fieldtype: "Data",
			fieldname: "flow_name",
			placeholder: __("OO Flow Name"),
            label: __("OO Flow Name"),
            read_only: 1
		}
	});
	flow_name.refresh();
	frappe.pages['flow-launcher'].flow_name = flow_name;

	page.set_primary_action(__("Launch Flow"), function(){
		frappe.call({
			method: "oo_integration.oo_api.run_flow_frappe",
			args: {
				uuid: flow.get_value(),
				run_name: flow_name.value
			},
			callback: function(r) {
				if(r) {
					console.log(r)
				}
			}
		});
	})
};