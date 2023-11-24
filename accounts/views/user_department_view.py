from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView

from accounts.models import Department

from accounts.forms.user_depatment_form import DepartmentForm


class DepartmentView(SuccessMessageMixin, UserPassesTestMixin, CreateView):
    template_name = 'account/add_department.html'
    model = Department
    form_class = DepartmentForm
    success_url = '/'
    success_message = 'Департамент успешно добавлен!'
    permission_denied_message = 'Отказано в доступе!'

    def test_func(self):
        return self.request.user.is_superuser
