from django.http import HttpResponse
from django.views.generic import View

__author__ = 'amucci'

class AastraView(View):


    def dispatch(self,request, *args, **kwargs):
        user_agent = request.META['HTTP_USER_AGENT']
        splitted_agent = user_agent.split()
        self.phone_model = splitted_agent[0]
        self.phone_mac = splitted_agent[1].split(":")[1]
        return super(AastraView, self).dispatch(request,*args, **kwargs)

class AastraResponseMixin(object):

    def render_to_response(self, context, **response_kwargs):
        """
        Returns a response, using the `response_class` for this
        view, with a template rendered with the given context.

        If any keyword arguments are provided, they will be
        passed to the constructor of the response class.
        """
        return HttpResponse(context,content_type="text/xml; charset=ISO-8859-1")