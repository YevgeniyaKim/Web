from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from api.models import Company, Vacancy


def companies(request):
    return JsonResponse(
        [c.to_json() for c in Company.objects.all()], safe=False
    )


def company(request, company_id):
    try:
        c = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(c.to_json())


def company_vacancies(request, company_id):
    try:
        comp = Company.objects.get(id=company_id)
        return JsonResponse(
            [v.to_json() for v in Vacancy.objects.filter(company=comp)],
            safe=False
        )
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})


def vacancies(request):
    return JsonResponse(
        [v.to_json() for v in Vacancy.objects.all()], safe=False
    )


def vacancy(request, vacancy_id):
    try:
        c = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(c.to_json())


def vacancies_top10(request):
    return JsonResponse(
        [v.to_json() for v in Vacancy.objects.order_by('-salary', 'name')[:10]], safe=False
    )
