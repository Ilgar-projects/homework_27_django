from django.urls import path
from ads.views import AdDetailView, AdListCreateView

urlpatterns = [
    path('', AdListCreateView.as_view()),
    path('<int:pk>/', AdDetailView.as_view(), name="ad_detail")
]
# name="ad_detail" это просто название урла, сами придумываем название
# это алиас, то есть это название самого пути-path
