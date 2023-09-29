from django.shortcuts import render
from django.http import HttpResponse

tax_rate = 1.15


def index(request):
    return HttpResponse("this is a site to calculate tax.")


def anyNumber(request, number):
    numberTaxed = int(number) * tax_rate
    return HttpResponse(f"your number is {number} and after tax is {numberTaxed}")
