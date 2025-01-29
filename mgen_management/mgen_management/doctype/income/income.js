// Copyright (c) 2025, Fat7allah and contributors
// For license information, please see license.txt

frappe.ui.form.on('Income', {
	refresh: function(frm) {

	},
	
	region: function(frm) {
		// Clear province when region changes
		frm.set_value('province', '');
		
		// Update province filter based on selected region
		frm.set_query('province', function() {
			return {
				filters: {
					'region': frm.doc.region
				}
			};
		});
	}
});
