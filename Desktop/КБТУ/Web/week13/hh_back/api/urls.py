from django.urls import path
from .views.views import *

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('companies/', companies),
    path('companies/<int:company_id>/', company),
    path('companies/<int:company_id>/vacancies/', company_vacancies),
    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:vacancy_id>/', VacancyDetailAPIView.as_view()),
    path('vacancies/top_ten/', VacancyTopTenAPIView.as_view())
]
