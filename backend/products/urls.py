from django.urls import path

from . import views

urlpatterns = [
    path('shop/all-makeup', views.Makeup, name="all-makeup"),
    path('shop/foundation-makeup', views.Foundation, name="foundation"),
    path('shop/bb-cream-cc-cream', views.BBCreamCCCream, name="bb_cream_cc_cream"),
    path('shop/concealer', views.Concealer, name="concealer"),
    path('shop/face-primer', views.Primer, name="primer"),
    path('shop/setting-spray-setting-powder', views.SettingSpraySettingPowder, name="setting-spray-setting-powder"),

    path('shop/eyeshadow', views.Eyeshadow, name="eyeshadow"),
    path('shop/mascara', views.Mascara, name="mascara"),
    path('shop/eyeliner', views.Eyeliner, name="eyeliner"),
    path('shop/eyebrow-makeup-pencils', views.Eyebrow, name="eyebrows"),
    path('shop/false-eyelashes', views.FalseEyelashes, name="false-eyelashes"),
    path('shop/eyes-formulation=serum', views.LashSerumsBrowSerums, name="eye-serums"),

    path('shop/lip-gloss', views.LipGloss, name="lip-gloss"),
    path('shop/lipstick', views.Lipstick, name="lipstick"),
    path('shop/lip-plumper', views.LipPlumper, name="lip-plumper"),
    path('shop/lip-balm-lip-treatments', views.LipBalmLipTreatment, name="balm-and-treatment-lips"),
    path('shop/lip-liner', views.LipLiner, name="lip-liner"),

    path('shop/blush', views.Blush, name="blush"),
    path('shop/highlighter', views.Highlighter, name="highlighter"),
    path('shop/contour', views.Contour, name="contour"),

    path('shop/all-fragrance', views.Fragrance, name="all-fragrance"),
    path('shop/perfume', views.Perfume, name="perfume"),
    path('shop/perfume-formulation-oils', views.PerfumeOils, name='perfume_oils'),
    path('shop/body-mist-hair-mist', views.BodyMistHairMist, name='body_mist_hair_mist'),
    path('shop/cologne', views.Cologne, name='cologne'),
    path('beauty/best-selling-perfume', views.Bestsellers, name="bestsellers"),
    path('shop/clean-fragrance', views.CleanFragrance, name="clean_fragrances"),
    path('beauty/niche-perfume', views.NicheFragrance, name="niche_fragrances"),
    path('beauty/affordable-fragrance', views.AffordableFragrance, name="affordable_fragrances"),
]

