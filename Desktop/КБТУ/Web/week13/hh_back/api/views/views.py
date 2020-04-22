from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer


@api_view(['GET', 'POST'])
def companies(request):
    if request.method == 'GET':
        c = Company.objects.all()
        serializer = CompanySerializer(c, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def company(request, company_id):
    try:
        c = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = CompanySerializer(c)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CompanySerializer(instance=c, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        c.delete()
        return Response({'deleted': True})


@api_view(["GET"])
def company_vacancies(request, company_id):
    try:
        c = Company.objects.get(id=company_id)
        serializer = VacancySerializer(
            Vacancy.objects.filter(company=c),
            many=True
        )
        return Response(serializer.data)
    except Company.DoesNotExist as e:
        return Response({'error': str(e)})
    except Vacancy.DoesNotExist as e:
        return Response({'error': str(e)})


class VacancyListAPIView(APIView):
    def get(self, request):
        v = Vacancy.objects.all()
        serializer = VacancySerializer(v, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VacancyDetailAPIView(APIView):
    def get_object(self, vacancy_id):
        try:
            return Vacancy.objects.get(id=vacancy_id)
        except Company.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, vacancy_id):
        v = self.get_object(vacancy_id)
        serializer = VacancySerializer(v)
        return Response(serializer.data)

    def put(self, request, vacancy_id):
        v = self.get_object(vacancy_id)
        serializer = VacancySerializer(instance=v, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, vacancy_id):
        v = self.get_object(vacancy_id)
        v.delete()
        return Response({'deleted': True})


class VacancyTopTenAPIView(APIView):
    def get(self, request):
        serializer = VacancySerializer(
            Vacancy.objects.order_by('-salary', 'name')[:10],
            many=True
        )
        return Response(serializer.data)
