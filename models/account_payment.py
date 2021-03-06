from odoo import models, fields, api
from odoo.tools import amount_to_text_en

class account_payment(models.Model):
    _inherit = "account.payment"

    def _get_move_vals(self, journal=None):
        """ Return dict to create the payment move
        """
        journal = journal or self.journal_id
        if not journal.sequence_id:
            raise UserError(_('Configuration Error !'),
                            _('The journal %s does not have a sequence, please specify one.') % journal.name)
        if not journal.sequence_id.active:
            raise UserError(_('Configuration Error !'), _('The sequence of journal %s is deactivated.') % journal.name)

        # Check If outbound type then use sequence out ID
        name = self.move_name or journal.with_context(ir_sequence_date=self.payment_date).sequence_id.next_by_id()
        if self.payment_type == 'outbound':
            name = self.move_name or journal.with_context(ir_sequence_date=self.payment_date).sequence_out_id.next_by_id()
        return {
            'name': name,
            'date': self.payment_date,
            'ref': self.communication or '',
            'company_id': self.company_id.id,
            'journal_id': journal.id,
        }

    @api.multi
    def amount_to_text(self, amount, currency):
        convert_amount_in_words = amount_to_text_en.amount_to_text(amount, lang='en', currency='')
        convert_amount_in_words = convert_amount_in_words.replace(',', ' ')
        convert_amount_in_words = convert_amount_in_words.replace(' and Zero', ' ')
        convert_amount_in_words += 'Rupiah'
        return convert_amount_in_words


