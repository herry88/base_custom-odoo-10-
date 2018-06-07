from odoo import models, fields, api


class AccountJournal(models.Model):
    _inherit = "account.journal"
    _description = 'Field Pembayaran untuk Menandakan Journal Uang Masuk atau Keluar yang digunakan pada saat payment'

    sequence_out_id = fields.Many2one('ir.sequence', string='Sequence Payment Out',
                                      help="This field contains the information related to the numbering of the journal entries of this journal.")