from django.http import JsonResponse
from .models import Product
from .serializers import ProductSerializer

#from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework import generics

from django.shortcuts import render
from . import apis
    
class ProductListCreateView(generics.ListAPIView):
    queryset = Product.objects.all() # if request.method == 'GET' needed?
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category', 'displayName']

    def Post(self, request): # add functions for DELETE and PUT
        if request.method == 'POST':
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
#@api_view(['GET', 'PUT', 'DELETE'])

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



def Skincare(request):
    response = apis.fetch_skincare_data()
    return render(request, "products/index.html", {'response': response})

def Moisturizer(request):
    response = apis.fetch_moisturizer_data()
    return render(request, "products/index.html", {'response': response})

def EverydayMoisturizers(request):
    response = apis.fetch_everyday_moisturizers_data()
    return render(request, "products/index.html", {'response': response})

def NightCreams(request):
    response = apis.fetch_night_creams_data()
    return render(request, "products/index.html", {'response': response})

def FaceOils(request):
    response = apis.fetch_face_oils_data()
    return render(request, "products/index.html", {'response': response})

def FaceMistsFaceEssences(request):
    response = apis.fetch_face_mists_face_essences_data()
    return render(request, "products/index.html", {'response': response})



def Cleansers(request):
    response = apis.fetch_cleansers_data()
    return render(request, "products/index.html", {'response': response})

def FaceWash(request):
    response = apis.fetch_face_wash_data()
    return render(request, "products/index.html", {'response': response})

def Exfoliator(request):
    response = apis.fetch_exfoliators_data()
    return render(request, "products/index.html", {'response': response})

def MakeupRemover(request):
    response = apis.fetch_makeup_remover_data()
    return render(request, "products/index.html", {'response': response})



def Treatments(request):
    response = apis.fetch_treatments_data()
    return render(request, "products/index.html", {'response': response})

def FaceSerum(request):
    response = apis.fetch_face_serums_data()
    return render(request, "products/index.html", {'response': response})

def AcneTreatments(request):
    response = apis.fetch_acne_treatments_data()
    return render(request, "products/index.html", {'response': response})

def EyeCreamsEyeTreatments(request):
    response = apis.fetch_eye_creams_eye_treatments_data()
    return render(request, "products/index.html", {'response': response})



def Masks(request):
    response = apis.fetch_masks_data()
    return render(request, "products/index.html", {'response': response})

def FaceMasks(request):
    response = apis.fetch_face_masks_data()
    return render(request, "products/index.html", {'response': response})

def EyeMasks(request):
    response = apis.fetch_eye_masks_data()
    return render(request, "products/index.html", {'response': response})



def Sunscreen(request):
    response = apis.fetch_sunscreen_data()
    return render(request, "products/index.html", {'response': response})

def FaceSunscreen(request):
    response = apis.fetch_face_sunscreen_data()
    return render(request, "products/index.html", {'response': response})

def BodySunscreen(request):
    response = apis.fetch_body_sunscreen_data()
    return render(request, "products/index.html", {'response': response})



def SkincareTools(request):
    response = apis.fetch_skincare_tools_data()
    return render(request, "products/index.html", {'response': response})

#def SkincareRoutineBuilderQuiz

#def ShopProductsByConcernQuiz
