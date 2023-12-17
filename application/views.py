from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http.response import JsonResponse


class PersonView(View):

    def get(self, request, *args, **kwargs):
        return JsonResponse(status=200, data={})

    def post(self, request):
        return JsonResponse(status=200, data={})
