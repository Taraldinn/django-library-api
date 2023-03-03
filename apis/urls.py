from django.urls import path

from apis.views import BookApiView

urlpatterns = [
    path("", BookApiView.as_view(), name="book_list")   
]
