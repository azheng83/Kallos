from django.urls import path

from . import views

urlpatterns = [
    path('shop/perfume', views.Perfume, name="perfume"),
    path('shop/perfume-formulation-oils', views.PerfumeOils, name='perfume_oils'),
    path('shop/body-mist-hair-mist', views.BodyMistHairMist, name='body_mist_hair_mist'),
    path('shop/cologne', views.Cologne, name='cologne'),
    path('beauty/best-selling-perfume', views.Bestsellers, name="bestsellers"),
    path('shop/clean-fragrance', views.CleanFragrance, name="clean_fragrances"),
    path('beauty/niche-perfume', views.NicheFragrance, name="niche_fragrances"),
    path('beauty/affordable-fragrance', views.AffordableFragrance, name="affordable_fragrances"),
]