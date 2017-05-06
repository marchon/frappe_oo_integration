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
							flow_doc = r.message;
							flow_name.set_value(flow_doc.flow_name);

							frappe.pages['flow-launcher'].inputs = [];
							$(".inputs").html("");

							$.each(flow_doc.inputs, function( index, item ) {
								var input = frappe.ui.form.make_control({
									parent: $(".inputs"),
									df: {
										fieldtype: item.input_type,
										fieldname: item.input_name,
										label: item.label,
										reqd: item.mandatory
									}
								});
								input.refresh();
								frappe.pages['flow-launcher'].inputs.push(input);
							});
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
		args = {
			uuid: flow.get_value(),
			run_name: flow_name.value
		};

		inputs = {};

		$.each(frappe.pages['flow-launcher'].inputs, function( index, input ) {
			  debugger;
			  if(input.df.fieldtype==="Link"){
			  	value = input.get_value();
			  }
			  else if(input.df.fieldtype==="Int"){
			  	value = String(input.get_value())
			  }
			  else{
			  	value = input.get_value();
			  }
			  inputs[input.df.fieldname]=value;
		});

		if(inputs!=={}){
			args["inputs"]=inputs;
		}

		frappe.call({
			method: "oo_integration.oo_api.run_flow_frappe",
			args: args,
			callback: function(r) {
				if(r) {
					frappe.set_route("Form", "OO Flow Execution", r.message);
				}
			}
		});
	})
};