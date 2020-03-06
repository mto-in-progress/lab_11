from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .forms import LoginForm

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login/index.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            html = f"<html><body>Form is valid: <br> {form.data['email_field']} <br> {form.data['pass_field']}</body></html>"
            return HttpResponse(html)
        else:
            html = f"<html><body>Form is NOT valid</body></html>"
            return HttpResponse(html)

# localhost: 8000/django_admin

# Create your views here.
