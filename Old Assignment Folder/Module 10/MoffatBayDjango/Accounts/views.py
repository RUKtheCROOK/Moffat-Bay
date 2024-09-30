from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, View, TemplateView
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm, CustomUserLoginForm
from .models import CustomUser
from django.shortcuts import render
from django.contrib.auth import logout

# Group Names: Taylor Mommer, John Garcia, Andrew Bach, Somsak Bounchareune, Torren Davis

# This is the sign up view. It is a CreateView that uses the CustomUser model and CustomUserCreationForm.
class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Sign Up'
        context['page_type'] = 'signup/login'
        return context
    
# This is the login view. It is a FormView that uses the CustomUserLoginForm.
class LoginView(FormView):
    form_class = CustomUserLoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.cleaned_data['user']
        auth_login(self.request, user)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Login'
        context['page_type'] = 'signup/login'
        return context

# This is the logout view. It is a View that logs the user out.    
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'registration/logged_out.html')