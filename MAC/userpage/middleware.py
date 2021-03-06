from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect
class LoginRequiredMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        return (response)

    def process_view(self,request,view_func,view_args,view_kwargs):
        url = request.path
        authenticated = request.user.is_authenticated
        if authenticated and url == settings.BLOG_URL:
            logout(request)

        # if not authenticated and (url != settings.BLOG_URL):
        #     return redirect(settings.BLOG_URL)
