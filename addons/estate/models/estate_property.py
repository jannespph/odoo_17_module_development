from odoo import fields, models
from dateutil.relativedelta import relativedelta    

class EstateProperty(models.Model):
    _name = "estate.property"           #|
    _description = "Estate Property"    #|  <--- ini adalah private atribut yang digunakan sebagai identitas dari class

    name = fields.Char("Title",required=True)    #<------Di Odoo semua field huruf pertamanya kapital,kalau tidak akan terjadi error
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date("Available From",copy = False, default = lambda self: fields.Datetime.now() + relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer("Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West')
        ]
    )
    active = fields.Boolean(default=False) #<------ gunanya field active di Odoo adalah untuk mengontrol apakah data ditampilkan (aktif) atau disembunyikan (diarsipkan) di UI
    #New, Offer Received, Offer Accepted, Sold and Cancelled.
    state = fields.Selection(
        selection=[
            ('new','New'),  #<----- catatn yang sebelah kiri itu value untuk database kalok yang kanan untuk di tampilkan di UI
            ('offer_received','Offer Received'),
            ('offer_accepted','Offer Accepted'),
            ('cancelled','Cancelled'),
        ],
        required = True,
        copy = False,
        default ='new',
    )

