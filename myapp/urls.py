from django.urls import path
from django.urls.conf import include
from myapp import views
from myapp.views import ContactViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('contact', ContactViewSet, basename='contact')

urlpatterns=[
    path('',include(router.urls))
]


# from myapp import views
# from rest_framework.urlpatterns import format_suffix_patterns

# urlpatterns = format_suffix_patterns([
#     path('myapi/', views.BlogList.as_view()),
#     path('detail/<int:pk>/', views.ApiDetail.as_view()),
#     path('gav/', views.ContactList.as_view(), name='contact-list'),
#     path('gavdetail/<int:pk>/', views.ContactDetail.as_view()),
#     path('', views.api_root),
# ])