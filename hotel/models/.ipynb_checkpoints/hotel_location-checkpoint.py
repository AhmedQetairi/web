from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from odoo.osv import expression


class HotelLocation(models.Model):

    _name = "hotel.location"
    _description = "Hotel Location"

   
    city = fields.Char("City", required=True)
    street = fields.Char("Street", required=True)