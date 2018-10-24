#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:
 @author: david
 @date: 2018/10/24 0024
"""
from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the res.partner model, by default partners are not
    # instructors
    instructor = fields.Boolean("Instructor", default=False)

    session_ids = fields.Many2many('openacademy.session',
                                   string="Attended Sessions", readonly=True)
