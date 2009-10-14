from django.conf import settings

# PLEASE: Don't change anything here, use your site settings.py

USER_AGENTS = {
    'jqtouch': r'AppleWebKit/.*Mobile/',
}
USER_AGENTS.update(getattr(settings, 'MOBILITY_USER_AGENTS', {}))

TEMPLATE_MAPPING = {
    'index': ('index_template', 'index.html'),
    'display_login_form': ('login_template', 'login.html'),
    'app_index': ('app_index_template', 'app_index.html'),
    'render_change_form': ('change_form_template', 'change_form.html'),
    'changelist_view': ('change_list_template', 'change_list.html'),
    'delete_view': ('delete_confirmation_template', 'delete_confirmation.html'),
    'history_view': ('object_history_template', 'object_history.html'),
    'logout': ('logout_template', 'registration/logged_out.html'),
    'password_change': ('password_change_template', 'registration/password_change_form.html'),
    'password_change_done': ('password_change_done_template', 'registration/password_change_done.html'),
}
TEMPLATE_MAPPING.update(getattr(settings, 'MOBILITY_TEMPLATE_MAPPING', {}))
