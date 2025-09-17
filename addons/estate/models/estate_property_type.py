from odoo import fields,models


class EstatePropertyType(models.Model):
    _name = "estate.property.type" #<----- ini dipakai sebagai nama modelnya untuk mewakili class dari estate property type
    _description = "Estate Property Type"

    name = fields.Char(required=True)
    