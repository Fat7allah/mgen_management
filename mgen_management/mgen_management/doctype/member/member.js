frappe.ui.form.on('Member', {
    refresh: function(frm) {
        // Clear province when region is cleared
        frm.set_query('province', function() {
            if (frm.doc.region) {
                return {
                    filters: {
                        'region': frm.doc.region
                    }
                };
            }
        });
    },

    region: function(frm) {
        // Clear province when region changes
        if (frm.doc.province) {
            frm.set_value('province', '');
        }
    }
});
