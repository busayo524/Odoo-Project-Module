from odoo import models, api


class ProjectProject(models.Model):
    _inherit = 'project.project'

    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        user = self.env.user
        is_admin = user.has_group('base.group_system')
        is_project_manager = user.has_group('project.group_project_manager')

        if not is_admin and not is_project_manager:
            tasks = self.env['project.task'].sudo().search([
                ('user_ids', 'in', [user.id])
            ])
            allowed_project_ids = tasks.mapped('project_id').ids

            if not allowed_project_ids:
                allowed_project_ids = [0]

            args = list(args or []) + [('id', 'in', allowed_project_ids)]

        return super()._search(
            args, offset=offset, limit=limit,
            order=order, count=count,
            access_rights_uid=access_rights_uid
        )


class ProjectTask(models.Model):
    _inherit = 'project.task'

    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        user = self.env.user
        is_admin = user.has_group('base.group_system')
        is_project_manager = user.has_group('project.group_project_manager')

        if not is_admin and not is_project_manager:
            # User can only see tasks assigned to them
            args = list(args or []) + [('user_ids', 'in', [user.id])]

        return super()._search(
            args, offset=offset, limit=limit,
            order=order, count=count,
            access_rights_uid=access_rights_uid
        )