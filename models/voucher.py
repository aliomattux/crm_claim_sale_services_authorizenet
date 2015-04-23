from openerp.osv import osv, fields



class AuthorizeNetAPI(osv.osv_memory):
    _inherit = 'authorizenet.api'


    def find_sale_reference(self, cr, uid, voucher, context=None):
	res = super(AuthorizeNetAPI, self).find_sale_reference(cr, uid, voucher, context=context)
	if voucher.invoice.claim:
	    return voucher.invoice.claim.sale
	else:
	    return res
