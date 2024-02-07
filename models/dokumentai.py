from odoo import models, fields, api


class Dokumentai(models.Model):
    _name = "dokumentu_tvarkymas.dokumentai"
    _decription = "Dokumentas"

    name = fields.Char(string="Pavadinimas", required=True)
    description = fields.Text(string="Aprašymas")
    company = fields.Char(string="Įmonė", required=True)
 #   company_id = fields.Many2one('res.company,')
 # created_by = fields.Many2one('res.users', string='Created by', default=lambda self: self.env.user, readonly=True)
#     responsible_users = fields.Many2many('res.users', string='Responsible workers')