frappe.ui.form.on('Expense', {
    refresh: function(frm) {
        // Initial setup of the field based on current value
        if (frm.doc.type === 'بطائق') {
            frm.set_df_property('amount', 'read_only', 1);
            calculate_amount(frm);
        }
    },
    
    type: function(frm) {
        // When type changes
        if (frm.doc.type === 'بطائق') {
            frm.set_df_property('amount', 'read_only', 1);
            calculate_amount(frm);
        } else {
            frm.set_df_property('amount', 'read_only', 0);
        }
    },
    
    quantity: function(frm) {
        // When quantity changes and type is بطائق
        if (frm.doc.type === 'بطائق') {
            calculate_amount(frm);
        }
    }
});

function calculate_amount(frm) {
    // Calculate amount as quantity × 100
    let amount = (frm.doc.quantity || 0) * 100;
    frm.set_value('amount', amount);
}
