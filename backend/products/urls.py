from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.ProductListCreateView.as_view(), name="test_rest"),


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

    path('shop/all-skincare', views.Skincare, name="all-skincare"),
    path('shop/moisturizing-cream-oil-mists', views.Moisturizer, name="all-moisturizer"),
    path('shop/moisturizing-everyday', views.EverydayMoisturizers, name="everyday-moisturizers"),
    path('shop/night-cream', views.NightCreams, name="night-creams"),
    path('shop/face-oils', views.FaceOils, name="face-oils"),
    path('shop/face-mist-face-essences', views.FaceMistsFaceEssences, name="face-mist-face-essences"),

    path('shop/all-cleansers', views.Cleansers, name="all-cleansers"),
    path('shop/face-wash', views.FaceWash, name="face-wash"),
    path('shop/exfoliators', views.Exfoliator, name="exfoliators"),
    path('shop/makeup-remover', views.MakeupRemover, name="makeup-remover"),

    path('shop/all-treatments', views.Treatments, name="all-treatments"),
    path('shop/face-serum', views.FaceSerum, name="face-serum"),
    path('shop/acne-treatments', views.AcneTreatments, name="acne-treatments"),
    path('shop/eye-creams-eye-treatments', views.EyeCreamsEyeTreatments, name="eye-cream-eye-treatments"),
    #path('shop/lip-balm-lip-treatments', views.LipBalmLipTreatment, name="all-fragrance"), just put a link to the origial lip balm lip treatments

    path('shop/all-mask', views.Masks, name="masks"),
    path('shop/face-mask', views.FaceMasks, name="face-masks"),
    path('shop/eye-mask', views.EyeMasks, name="eye-masks"),

    path('shop/all-sunscreen', views.Sunscreen, name="all-sunscreen"),
    path('shop/face-sunscreen', views.FaceSunscreen, name="face-sunscreen"),
    path('shop/body-sunscreen', views.BodySunscreen, name="body-sunscreen"),

    path('shop/skincare-tools', views.SkincareTools, name="skincare-tools"),

]

