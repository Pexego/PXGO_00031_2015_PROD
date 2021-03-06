# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Pexego All Rights Reserved
#    $Omar Castiñeira Saavedra <omar@pexego.es>$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, api


class PurchaseOrder(models.Model):

    _inherit = "purchase.order"

    @api.multi
    def wkf_confirm_order(self):
        for purchase in self:
            if (purchase.picking_type_id and
                    purchase.picking_type_id.force_purchase_dest):
                purchase.write({'location_id': purchase.picking_type_id.
                                default_location_dest_id.id})
        return super(PurchaseOrder, self).wkf_confirm_order()
