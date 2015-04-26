from openerp.osv import osv, fields
from openerp.tools.translate import _


class AccountInvoice(osv.osv):
    _inherit = 'account.invoice'

    def get_cc_payment_journal(self, cr, uid, invoice, context=None):
	res = super(AccountInvoice, self).get_cc_payment_journal(cr, uid, invoice, context=context)

        if not invoice.claim.sale:
            return res

        sale = invoice.claim.sale

        if sale.card_type:
            journal = sale.payment_method[sale.card_type + '_journal']
            return journal.id

        return res


    def get_payment_profile(self, cr, uid, invoice, context=None):
	res = super(AccountInvoice, self).get_payment_profile(cr, uid, invoice, context=context)
	if invoice.claim and invoice.claim.payment_profile:
	    return invoice.claim.payment_profile

        return res

