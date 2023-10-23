from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import DetailView


class UserDetailView(UserPassesTestMixin, DetailView):
    model = get_user_model()
    template_name = 'account/profile.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = self.model.objects.all().order_by('department')
        context['all_users'] = users
        return context

    def test_func(self):
        return self.request.user.is_authenticated
