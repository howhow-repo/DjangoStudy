from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from enum import Enum

month_challenges_table = {
    'january':'This is january challenge',
    'february':'This is february challenge',
    'march':'This is march challenge',
    'april':'This is april challenge',
    'may':'This is may challenge',
    'june':'This is june challenge',
    'july':'This is july challenge',
    'august':'This is august challenge',
    'september':'This is september challenge',
    'october':'This is october challenge',
    'november':'This is november challenge',
    'december':'This is december challenge',

}

def index(request):
    list_item = ''
    months = list(month_challenges_table.keys())
    for month in months:
        month_path = reverse("month-challenges",args = [month])
        list_item += f"<li><a href=\"{month_path}\">{month}</a></li>"
    response_data = f"<ul>{list_item}</ul>"
    return HttpResponse(response_data)

def int_month_rederict(request,month):
    months = list(month_challenges_table.keys())
    try:
        month -= 1
        redirect_path = reverse("month-challenges",args = [months[month]])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("invalid month")

def month_challenges(request,month):
    challenge = None
    try:
        challenge = month_challenges_table[month]

        return render(request,"challenges/challenge.html",{
            "this_month":month,
            "the_challenge":challenge,
        })
    except:
        return HttpResponseNotFound("no such month support!")
