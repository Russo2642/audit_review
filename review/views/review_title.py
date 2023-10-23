from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import CreateView, ListView, DeleteView
from review.forms import ReviewTitleForm
from review.models import ReviewTitle


class ReviewTitleIndexView(UserPassesTestMixin, ListView):
    model = ReviewTitle
    template_name = 'review/review_title_index.html'
    context_object_name = 'review_title'
    ordering = '-created_at'

    def get_context_data(self, **kwargs):
        kwargs["review_title_form"] = ReviewTitleForm(instance=self.request.user)
        return super().get_context_data(**kwargs)

    def test_func(self):
        return self.request.user.is_superuser


class ReviewTitleCreateView(SuccessMessageMixin, UserPassesTestMixin, CreateView):
    template_name = 'review/review_title_create.html'
    model = ReviewTitle
    form_class = ReviewTitleForm
    success_message = 'Наименование проверки успешно добавлено!'
    permission_denied_message = 'Отказано в доступе!'

    def get_success_url(self):
        return reverse('review_title_index')

    def test_func(self):
        return self.request.user.is_superuser


class ReviewTitleDeleteView(UserPassesTestMixin, DeleteView):
    model = ReviewTitle

    def get_success_url(self):
        return reverse('review_title_index')

    def test_func(self):
        return self.request.user.is_superuser
