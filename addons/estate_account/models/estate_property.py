from odoo import Command, models

class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def action_sold(self):
        # print("🔴 action_sold method overridden from estate_account module.")
        result = super(EstateProperty, self).action_sold()

        journal = self.env['account.journal'].search([('type', '=', 'sale')], limit=1)
        if not journal:
            raise UserError("No Sales Journal found, please configure one.")

        invoice_vals = {
            'partner_id': self.buyer_id.id,
            'move_type': 'out_invoice',
            'journal_id': journal.id,
            'invoice_line_ids': [
                Command.create({
                    'name': 'Selling Price Commission',
                    'quantity': 1,
                    'price_unit': self.selling_price * 0.06
                }),
                Command.create({
                    'name': 'Administrative Fees',
                    'quantity': 1,
                    'price_unit': 100.00
                })
            ]
        }

        self.env['account.move'].create(invoice_vals)

        return result