from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/dw/login/"
    template_name = "datawiz/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm
    success_url = "/dw/"
    template_name = "datawiz/login.html"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

def logout_view(request):
    logout(request)
    return redirect('/dw/')

# Create your views here.
def index(request):
    if not request.user.is_authenticated():
        return render(request, 'datawiz/choice.html')
    else:
        
        return render(request, 'datawiz/base.html')
