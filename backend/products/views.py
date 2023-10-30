from django.shortcuts import render
from . import apis

def Makeup(request):
    response = apis.fetch_makeup_data()
    return render(request, "products/index.html", {'response': response})

def Foundation(request):
    response = apis.fetch_foundation_data()
    return render(request, "products/index.html", {'response': response})

def BBCreamCCCream(request):
    response = apis.fetch_bb_cc_cream_data()
    return render(request, "products/index.html", {'response': response})

def Concealer(request):
    response = apis.fetch_concealer_data()
    return render(request, "products/index.html", {'response': response})

def Primer(request):
    response = apis.fetch_primer_data()
    return render(request, "products/index.html", {'response': response})

def SettingSpraySettingPowder(request):
    response = apis.fetch_setting_spray_setting_powder_data()
    return render(request, "products/index.html", {'response': response})


def Eyeshadow(request):
    response = apis.fetch_eyeshadow_data()
    return render(request, "products/index.html", {'response': response})

def Mascara(request):
    response = apis.fetch_mascara_data()
    return render(request, "products/index.html", {'response': response})

def Eyeliner(request):
    response = apis.fetch_eyeliner_data()
    return render(request, "products/index.html", {'response': response})

def Eyebrow(request):
    response = apis.fetch_eyebrow_data()
    return render(request, "products/index.html", {'response': response})

def FalseEyelashes(request):
    response = apis.fetch_false_eyelashes_data()
    return render(request, "products/index.html", {'response': response})

def LashSerumsBrowSerums(request):
    response = apis.fetch_lash_serums_brow_serums_data()
    return render(request, "products/index.html", {'response': response})


def LipGloss(request):
    response = apis.fetch_lip_gloss_data()
    return render(request, "products/index.html", {'response': response})

def Lipstick(request):
    response = apis.fetch_lipstick_data()
    return render(request, "products/index.html", {'response': response})

def LipPlumper(request):
    response = apis.fetch_lip_plumper_data()
    return render(request, "products/index.html", {'response': response})

def LipBalmLipTreatment(request):
    response = apis.fetch_lip_balm_lip_treatments_data()
    return render(request, "products/index.html", {'response': response})

def LipLiner(request):
    response = apis.fetch_lip_liner_data()
    return render(request, "products/index.html", {'response': response})


def Blush(request):
    response = apis.fetch_blush_data()
    return render(request, "products/index.html", {'response': response})

def Highlighter(request):
    response = apis.fetch_highlighter_data()
    return render(request, "products/index.html", {'response': response})

def Contour(request):
    response = apis.fetch_contour_data()
    return render(request, "products/index.html", {'response': response})


def Fragrance(request):
    response = apis.fetch_fragrance_data()
    return render(request, "products/index.html", {'response': response})

def Perfume(request):
    response = apis.fetch_perfume_data()
    return render(request, "products/index.html", {'response': response})


def PerfumeOils(request):
    response = apis.fetch_perfume_oil_data()
    return render(request, "products/index.html", {'response': response})


def BodyMistHairMist(request):
    response = apis.fetch_body_mist_hair_mist_data()
    return render(request, "products/index.html", {'response': response})


def Cologne(request):
    response = apis.fetch_cologne_data()
    return render(request, "products/index.html", {'response': response})

def Bestsellers(request):
    response = apis.fetch_fragrance_bestsellers_data()
    return render(request, "products/index.html", {'response': response})

def NicheFragrance(request):
    response1, response2, response3, response4 = apis.fetch_niche_fragrances_data()
    return render(request, 'products/niche_fragrances.html', {'response1': response1, 
                                                              'response2': response2, 
                                                              'response3': response3,
                                                              'response4': response4,})

def CleanFragrance(request):
    response = apis.fetch_clean_fragrances_data()
    return render(request, "products/index.html", {'response': response})

def AffordableFragrance(request):
    response = apis.fetch_affordable_fragrances_data()
    return render(request, "products/index.html", {'response': response})

#def fragrance_notes_guide():

#def find_signature_scent():