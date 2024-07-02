from odoo import models, fields, api

class Leads(models.Model):
    _name = 'leads.leads'
    _description = 'Leads'

    name = fields.Char(string='Nombre')
    apellidos = fields.Char(string='Apellidos')
    movil = fields.Char(string='Teléfono Personal')
    correo = fields.Char(string='Correo Electrónico')
    fecha_contacto = fields.Date(string='Fecha de Contacto') 
    via = fields.Selection([
        ('public', 'Correo Gmail'),
        ('social', 'Redes Sociales'),
        ('friend', 'Personas o amigos'),
    ], string='Vía de Contacto')