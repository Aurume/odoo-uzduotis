from odoo import models, fields, api


class Dokumentai(models.Model):
    _name = "dokumentu_tvarkymas.dokumentai"
    _decription = "Dokumentas"

    name = fields.Char(string="Pavadinimas", required=True)
    description = fields.Text(string="Aprašymas")
    company = fields.Char(string="Įmonė", required=True)
 #   company_id = fields.Many2one('res.company,')
