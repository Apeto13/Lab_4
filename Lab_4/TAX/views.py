from django.shortcuts import render
from django.http import HttpResponse

tax_rate = 1.15


def index(request):
    return HttpResponse("this is a site to calculate tax.")


def anyNumber(request, number):
    try:
        number = int(number)
        numberTaxed = int(number) * tax_rate
    except ValueError:
        numberTaxed = 0
    return HttpResponse(f"your number is {number} and after tax is {numberTaxed}")


def taxRate(request):
    return render(request, 'TAX/taxRate.html', {'tax_rate': round((tax_rate-1)*100)})
