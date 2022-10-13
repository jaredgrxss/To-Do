from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "index.html"

class SignUpConfirm(generic.TemplateView):
    template_name = 'signin_confirm.html'

class SignOutConfirm(generic.TemplateView):
    template_name = 'signout_confirm.html'


class AboutPage(generic.TemplateView):
    template_name = 'about.html'