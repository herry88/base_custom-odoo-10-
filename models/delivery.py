from odoo import models, fields, api
from odoo.tools import amount_to_text_en

class PickingSlip (models.Model):
    _inherit = "stock.picking"

    partner_ref = fields.Char(sting='Vendor Ref', compute='_compute_partner_ref')

    def _compute_partner_ref(self):
        # define obj purchase order
        # find purchase order based on name and stock picking origin
        # get requisition ID in purchase order save to self.partner_ref

        print self.origin
        purchase_order_data = self.env['purchase.order'].search([('name','=',self.origin)])
        for data in purchase_order_data:
            self.partner_ref = data.requisition_id.name
            # print data

    @api.multi
    def amount_to_text(self, amount, currency):
        convert_amount_in_words = amount_to_text_en.amount_to_text(amount, lang='en', currency='')
        convert_amount_in_words = convert_amount_in_words.replace(' and Zero', ' ')
        convert_amount_in_words = convert_amount_in_words.replace(',', ' ')
        convert_amount_in_words = convert_amount_in_words.replace('Rupiah', 'Rupiah ')
        return convert_amount_in_words

