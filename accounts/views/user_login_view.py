from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from accounts.forms import UserLoginForm


class LoginView(FormView):
    form_class = UserLoginForm
    template_name = 'account/login.html'
    success_url = '/'  # reverse_lazy('tour_list')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return self.form_valid(form)
        form.add_error('username', 'Неправильный логин или пароль')
        form.add_error('password', '')
        return self.form_invalid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)


def logout_view(request):
    logout(request)
    return redirect('login')
