from accounts.models import User
from accounts.models.user import DepartmentChoice, ActivateChoice
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView, ListView, DetailView
from review.forms import ReviewForm
from review.models import Review
from review.models import ReviewTitle


class IndexView(ListView):
    template_name = 'index.html'
    model = Review
    context_object_name = 'reviews'

    def get(self, request, *args, **kwargs):
        reviews = Review.objects.all()
        department_filter = request.GET.get('department')
        title_filter = request.GET.get('title')

        if department_filter:
            reviews = reviews.filter(author__department=department_filter)

        elif title_filter:
            reviews = reviews.filter(title=title_filter)

        elif department_filter and title_filter:
            reviews = reviews.filter(author__department=department_filter, title=title_filter)

        counter = 0
        authors = []

        for review in reviews:
            authors.append(review.author)
            counter += (review.block_a_sum + review.block_b_sum + review.block_c_sum + review.block_d_sum) / 4

        try:
            total = round(counter / len(authors), 2)
        except ZeroDivisionError:
            total = 0

        return render(request, template_name=self.template_name, context={
            'reviews': reviews,
            'DepartmentChoice': DepartmentChoice.choices,
            'titles': ReviewTitle.objects.all(),
            'total': total,
        })

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()
    #     counter = 0
    #     authors = []
    #     total = 0
    #
    #     for review in reviews:
    #         authors.append(review.author)
    #         counter += (review.block_a_sum + review.block_b_sum + review.block_c_sum + review.block_d_sum) / 4
    #
    #     try:
    #         total = round(counter / len(authors), 2)
    #     except ZeroDivisionError:
    #         context['total'] = 0
    #     context['total'] = total
    #
    #     return context


class ReviewCreateView(SuccessMessageMixin, UserPassesTestMixin, CreateView):
    template_name = 'review/review_create.html'
    model = Review
    form_class = ReviewForm
    success_url = '/'
    success_message = 'Ваш отзыв успешно отправлен. Спасибо!'
    permission_denied_message = 'Отказано в доступе!'

    def form_valid(self, form):
        form.instance.author = self.request.user
        # titles = get_object_or_404(ReviewTitle, author=self.request.user.pk)
        titles = ReviewTitle.objects.filter(author=self.request.user.pk).order_by('-created_at')[0]
        if titles:
            form.instance.title = titles.name
            titles.delete()
        self.request.user.update_active()
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.activating == ActivateChoice.ACTIVE


class ReviewDetailView(DetailView):
    template_name = 'review/review_detail.html'
    model = Review
    context_object_name = 'review'


class SendReviewView(SuccessMessageMixin, View):
    success_message = 'Опросник успешно отправлен!'
    permission_denied_message = 'Отказано в доступе!'

    def post(self, request, pk):
        users = get_object_or_404(User, pk=pk)
        if users.activating == ActivateChoice.NOT_ACTIVE:
            users.activating = ActivateChoice.ACTIVE
        users.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))
