from django.urls import path
from review.views.review import IndexView, ReviewCreateView, ReviewDetailView, SendReviewView
from review.views.review_excel import export_to_excel
from review.views.review_title import ReviewTitleCreateView, ReviewTitleIndexView, ReviewTitleDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('review/', ReviewCreateView.as_view(), name='review_create'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
    path('review/<int:pk>/sending/', SendReviewView.as_view(), name='send_review'),

    path('review-title/', ReviewTitleIndexView.as_view(), name='review_title_index'),
    path('review-title/create/', ReviewTitleCreateView.as_view(), name='review_title_create'),
    path('review-title/<int:pk>/delete/', ReviewTitleDeleteView.as_view(), name='review_title_delete'),

    path('review/<int:pk>/excel/', export_to_excel, name='export-excel'),
]
