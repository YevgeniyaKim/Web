from django.urls import path, re_path
# from .views.views_fbv import *
from .views.views_cbv import *

urlpatterns = [
    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:company_id>/', CompanyDetailAPIView.as_view()),
    path('companies/<int:company_id>/vacancies/', CompanyWithVacanciesListAPView.as_view()),
    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:vacancy_id>/', VacancyDetailAPIView.as_view()),
    # path('vacancies/top_ten/', vacancies_top10)
]
