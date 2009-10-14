"""


page_not_found and server_error functions where taken from mobileadmin!
"""


from django.http import HttpResponseNotFound, HttpResponseServerError
from django.views import defaults
from django.template import RequestContext, loader

from mobility import utils

def page_not_found(request, template_name = '404.html'):
    """
    Mobile 404 handler.

    Templates: `404.html`
    Context:
        request_path
            The path of the requested URL (e.g., '/app/pages/bad_page/')
    """
    user_agent = utils.get_user_agent(request)
    if user_agent:
        template_list = (
            'mobility/%s/404.html' % user_agent,
            template_name,
        )
        return HttpResponseNotFound(loader.render_to_string(template_list, {
            'request_path': request.path,
        }, context_instance = RequestContext(request)))
    return defaults.page_not_found(request, template_name)

def server_error(request, template_name = '500.html'):
    """
    Mobile 500 error handler.

    Templates: `500.html`
    Context: None
    """
    user_agent = utils.get_user_agent(request)
    if user_agent:
        template_list = (
            'mobility/%s/500.html' % user_agent,
            template_name,
        )
        return HttpResponseServerError(loader.render_to_string(template_list))
    return defaults.server_error(request, template_name)
