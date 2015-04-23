from openerp.osv import osv, fields

class CrmClaim(osv.osv):
    _inherit = 'crm.claim'
    _columns = {
        'payment_profile': fields.many2one('payment.profile', 'Payment Profile', \
                domain="[('partner', '=', partner_id)]"
        ),
    }
