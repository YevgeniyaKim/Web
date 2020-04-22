from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=500)
    city = models.CharField(max_length=200)
    address = models.TextField(max_length=250)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class Vacancy(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=500)
    salary = models.FloatField(default=100000)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = 'Vacancies'
