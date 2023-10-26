from django.shortcuts import render
from . import apis


def Perfume(request):
    response = apis.fetch_perfume_data()
    return render(request, 'products/fragrances.html', {'response': response})


def PerfumeOils(request):
    response = apis.fetch_perfume_oil_data()
    return render(request, "products/fragrances.html", {'response': response})


def BodyMistHairMist(request):
    response = apis.fetch_body_mist_hair_mist_data()
    return render(request, "products/fragrances.html", {'response': response})


def Cologne(request):
    response = apis.fetch_cologne_data()
    return render(request, 'products/fragrances.html', {'response': response})

def Bestsellers(request):
    response = apis.fetch_fragrance_bestsellers_data()
    return render(request, 'products/fragrances.html', {'response': response})

def NicheFragrance(request):
    response1, response2, response3, response4 = apis.fetch_niche_fragrances_data()
    return render(request, 'products/niche_fragrances.html', {'response1': response1, 
                                                              'response2': response2, 
                                                              'response3': response3,
                                                              'response4': response4,})

def CleanFragrance(request):
    response = apis.fetch_clean_fragrances_data()
    return render(request, 'products/fragrances.html', {'response': response})

def AffordableFragrance(request):
    response = apis.fetch_affordable_fragrances_data()
    return render(request, 'products/fragrances.html', {'response': response})

#def fragrance_notes_guide():

#def find_signature_scent():