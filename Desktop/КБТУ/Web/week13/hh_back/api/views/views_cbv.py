from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Company, Vacancy
from api.serializers import CompanySerializer2, VacancySerializer


class CompanyListAPIView(APIView):
    def get(self, request):
        c = Company.objects.all()
        serializer = CompanySerializer2(c, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CompanyDetailAPIView(APIView):
    def get_object(self, company_id):
        try:
            return Company.objects.get(id=company_id)
        except Company.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, company_id):
        c = self.get_object(company_id)
        serializer = CompanySerializer2(c)
        return Response(serializer.data)

    def put(self, request, company_id):
        c = self.get_object(company_id)
        serializer = CompanySerializer2(instance=c, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response({'error': serializer.errors})

    def delete(self, request, company_id):
        c = self.get_object(company_id)
        c.delete()

        return Response({'deleted': True})


class CompanyWithVacanciesListAPView(APIView):
    def get(self, request, company_id):
        v = Vacancy.objects.filter(id=company_id)
        serializer = VacancySerializer(v, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
