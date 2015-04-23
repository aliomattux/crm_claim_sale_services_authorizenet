from openerp.osv import osv, fields
from openerp.tools.translate import _

class SaleOrder(osv.osv):
    _inherit = 'sale.order'



    def get_default_claim_vals(self, cr, uid, sale, items, context=None):
	vals = super(SaleOrder, self).get_default_claim_vals(cr, uid, sale, items, context=context)

	#Copy the card token to the claim for use in any charge/invoice
	if sale.payment_profile:
	    vals['payment_profile'] = sale.payment_profile.id

	return vals


#    def find_eligible_refund_vouchers(self, cr, uid, context=None)
#	    for invoice in sale.invoice_ids:
#		voucher_ids = voucher_obj.search(cr, uid, [
#			('state', '=', 'posted'),
#			('type', '=', 'receipt'),
#			('refunded', '!=', True),
#			('invoice', '=', invoice.id)
#		])
#		if voucher_ids:
#		    eligible_refund_vouchers
