from odoo import models, fields, api
from odoo.tools import amount_to_text_en

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    # spk = fields.Boolean('SPK', select=True, help="It indicates that a surat perintah kerja selected")
    work_order = fields.Boolean('Work Order', select=True, help="It indicates that a work order selected")


    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('temp.value') or '/'
        return super(PurchaseOrder, self).create(vals)

    @api.multi
    def button_approve(self, force=False):
        if self.work_order:
            name = self.env['ir.sequence'].next_by_code('purchase.order.wo')
        else:
            name = self.env['ir.sequence'].next_by_code('purchase.order')
        self.write({'state': 'purchase', 'name': name})
        self._create_picking()
        if self.company_id.po_lock == 'lock':
            self.write({'state': 'done'})
        return {}

    @api.multi
    def amount_to_text(self, amount, currency):
        convert_amount_in_words = amount_to_text_en.amount_to_text(amount, lang='en', currency='')
        convert_amount_in_words = convert_amount_in_words.replace(',', ' ')
        convert_amount_in_words = convert_amount_in_words.replace(' and Zero', ' ')
        convert_amount_in_words += 'Rupiah'
        return convert_amount_in_words

