import smtplib
import ssl
from email.message import EmailMessage

from accounts.forms import UserRegisterForm
from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.views.generic import CreateView


class RegisterView(SuccessMessageMixin, UserPassesTestMixin, CreateView):
    template_name = 'account/register.html'
    form_class = UserRegisterForm
    success_url = '/'
    context = dict()
    success_message = 'Пользователь успешно зарегестрирован!'
    permission_denied_message = 'Отказано в доступе!'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)

            msg = EmailMessage()
            msg.set_content(f'Ваш логин: {user.username}\nВаш пароль: {user.username}')
            msg['Subject'] = 'ЛОГИН И ПАРОЛЬ. КОМАНДА СВА.'
            msg['From'] = settings.EMAIL_HOST_USER
            msg['To'] = user.email

            _context = ssl.create_default_context()

            with smtplib.SMTP('smtp.gmail.com', port=587) as smtp:
                smtp.starttls(context=_context)
                smtp.login(msg['From'], settings.EMAIL_HOST_PASSWORD)
                smtp.send_message(msg)

            # with get_connection(
            #         host=settings.EMAIL_HOST,
            #         port=settings.EMAIL_PORT,
            #         username=settings.EMAIL_HOST_USER,
            #         password=settings.EMAIL_HOST_PASSWORD,
            #         use_tls=settings.EMAIL_USE_TLS
            # ) as connection:
            #     EmailMessage(
            #         'Тест',
            #         'Тестовое письмо',
            #         'gothiq2302@gmail.com',
            #         ['stucci@mail.ru'],
            #         connection=connection,
            #     ).send()

            return redirect('/')
        self.context['form'] = form
        form.add_error('password', '')
        form.add_error('password_confirm', 'Пароли не совпадают')
        return self.render_to_response(self.context)

    def test_func(self):
        return self.request.user.is_superuser
