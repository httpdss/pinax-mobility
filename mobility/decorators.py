from mobility.conf import settings
from mobility.utils import get_user_agent

try:
    from functools import wraps
except ImportError:
    from django.utils.functional import wraps  # Python 2.3, 2.4 fallback.

def mobile_templates(function):
    """
    Decorator to be used on ``AdminSite`` or ``ModelAdmin`` methods that
    changes the template of that method according to the current user agent
    by using a template mapping.
    """
    func_name = function.__name__

    def _change_templates(self, request, *args, **kwargs):
        if func_name in settings.TEMPLATE_MAPPING:
            path_list = []
            attr_name, template_name = settings.TEMPLATE_MAPPING[func_name]
            user_agent = get_user_agent(request)
            params = dict(template_name=template_name)
            if user_agent:
                params.update(user_agent=user_agent)
                path_list += [
                    'mobility/%(user_agent)s/%(template_name)s',
                    'mobility/%(template_name)s',
                ]
                # if self is a ModelAdmin instance add more of the default
                # templates as fallback
                if getattr(self, 'model', False):
                    opts = self.model._meta
                    params.update(dict(app_label=opts.app_label,
                        object_name=opts.object_name.lower()))
                    path_list = [
                        'mobility/%(user_agent)s/%(app_label)s/%(object_name)s/%(template_name)s',
                        'mobility/%(user_agent)s/%(app_label)s/%(template_name)s',
                    ] + path_list + [
                        'admin/%(app_label)s/%(object_name)s/%(template_name)s',
                        'admin/%(app_label)s/%(template_name)s',
                    ]
                path_list += [
                    'admin/%(template_name)s',
                    '%(template_name)s',
                ]
            else:
                path_list += [
                    'admin/%(template_name)s',
                    '%(template_name)s',
                ]
            setattr(self, attr_name, [path % params for path in path_list])
        return function(self, request, *args, **kwargs)
    return wraps(function)(_change_templates)
