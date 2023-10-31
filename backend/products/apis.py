import requests

base_url = "https://sephora.p.rapidapi.com/us/products/v2/search"
base_header = {
        "X-RapidAPI-Key": "0a2db9998emshf122785976886e8p10b055jsnb3c36e679120",
        "X-RapidAPI-Host": "sephora.p.rapidapi.com"
    }

def fetch_makeup_data():
    querystring = {"q":"makeup","pageSize":"30","currentPage":"1","pl":"200","sortBy":"P_BEST_SELLING:1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_foundation_data():
    querystring = {"q":"foundation","pageSize":"20","currentPage":"1","pl":"200","sortBy":"P_BEST_SELLING:1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_bb_cc_cream_data():
    querystring = {"q":"BB & CC Cream","pageSize":"20","currentPage":"1","pl":"200","sortBy":"P_BEST_SELLING:1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_concealer_data():
    querystring = {"q":"Concealer","pageSize":"20","currentPage":"1","pl":"200","sortBy":"P_BEST_SELLING:1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_primer_data():
    querystring = {"q":"Face Primer","pageSize":"20","currentPage":"1","pl":"200","sortBy":"P_BEST_SELLING:1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_setting_spray_setting_powder_data():
    querystring = {"q":"Setting Spray & Powder","pageSize":"20","currentPage":"1","pl":"200","sortBy":"P_BEST_SELLING:1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()



def fetch_eyeshadow_data():
    querystring = {"q":"eyeshadow","pageSize":"20","currentPage":"1","pl":"200","sortBy":"P_BEST_SELLING:1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_mascara_data():
    querystring = {"q":"Mascara","pageSize":"20","currentPage":"1","pl":"200","sortBy":"P_BEST_SELLING:1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_eyeliner_data():
    querystring = {"q":"Eyeliner","pageSize":"20","currentPage":"1","pl":"200","sortBy":"P_BEST_SELLING:1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_eyebrow_data():
    querystring = {"q":"eyebrow","pageSize":"20","currentPage":"1","pl":"200","sortBy":"P_BEST_SELLING:1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_false_eyelashes_data():
    querystring = {"q":"false eyelashes","pageSize":"20","currentPage":"1","pl":"200","sortBy":"P_BEST_SELLING:1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_lash_serums_brow_serums_data():
    querystring = {"q":"Eyelash & Eyebrow Serums","pageSize":"20","currentPage":"1","pl":"200","sortBy":"P_BEST_SELLING:1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()




def fetch_lip_gloss_data():
    querystring = {"q":"lip gloss","pageSize":"20","currentPage":"1","pl":"200","sortBy":"P_BEST_SELLING:1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_lipstick_data():
    querystring = {"q":"lipstick","pageSize":"20","currentPage":"1","pl":"200","sortBy":"P_BEST_SELLING:1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_lip_plumper_data():
    querystring = {"q":"lip plumper","pageSize":"20","currentPage":"1","pl":"200","sortBy":"P_BEST_SELLING:1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_lip_balm_lip_treatments_data():
    querystring = {"q":"lip balms & treatments","pageSize":"20","currentPage":"1","pl":"200","sortBy":"P_BEST_SELLING:1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_lip_liner_data():
    querystring = {"q":"lip liner","pageSize":"20","currentPage":"1","pl":"200","sortBy":"P_BEST_SELLING:1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()




def fetch_blush_data():
    querystring = {"q":"blush","pageSize":"20","currentPage":"1","pl":"200","sortBy":"P_BEST_SELLING:1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_highlighter_data():
    querystring = {"q":"highlighter","pageSize":"20","currentPage":"1","pl":"200","sortBy":"P_BEST_SELLING:1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_contour_data():
    querystring = {"q":"contour","pageSize":"20","currentPage":"1","pl":"200","sortBy":"P_BEST_SELLING:1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()



def fetch_fragrance_data():
    querystring = {"q":"perfume fragrance","pageSize":"30","currentPage":"1","pl":"200","sortBy":"P_BEST_SELLING:1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_perfume_data():
    querystring = {"q":"Womens perfume","pageSize":"20","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()
    

def fetch_perfume_oil_data():
    querystring = {"q":"perfume oil","pageSize":"20","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()


def fetch_body_mist_hair_mist_data():
    querystring = {"q":"body mist","pageSize":"20","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()


def fetch_cologne_data():
    querystring = {"q":"men's cologne","pageSize":"20","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_fragrance_bestsellers_data():
    querystring = {"q":"most popular fragrances","pageSize":"20","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()


def fetch_niche_fragrances_data():

    querystring1 = {"q":"'REPLICA' perfume","pageSize":"5","currentPage":"1","pl":"200","sortBy":"P_PROD_NAME:1"}
    querystring2 = {"q":"Nest Perfume","pageSize":"5","currentPage":"1","pl":"200","sortBy":"P_RATING:0"}
    querystring3 = {"q":"Jo Malone Fragrance","pageSize":"5","currentPage":"1","pl":"200","sortBy":"P_RATING:0"}
    querystring4 = {"q":"Killian","pageSize":"5","currentPage":"1","pl":"200","sortBy":"P_BEST_SELLING:1"}

    response1 = requests.get(base_url, headers=base_header, params=querystring1).json()
    response2 = requests.get(base_url, headers=base_header, params=querystring2).json()
    response3 = requests.get(base_url, headers=base_header, params=querystring3).json()
    response4 = requests.get(base_url, headers=base_header, params=querystring4).json()

    return response1, response2, response3, response4


def fetch_clean_fragrances_data():
    querystring = {"q":"perfume clean fragrance","pageSize":"20","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_affordable_fragrances_data():
    querystring = {"q":"affordable perfume","pageSize":"20","currentPage":"1","pl":"200","sortBy":"P_BEST_SELLING:1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()



def fetch_skincare_data():
    querystring = {"q":"skincare","pageSize":"30","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_moisturizer_data():
    querystring = {"q":"moisturizers","pageSize":"30","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_everyday_moisturizers_data():
    querystring = {"q":"everyday face moisturizers","pageSize":"30","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_night_creams_data():
    querystring = {"q":"night creams","pageSize":"30","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_face_oils_data():
    querystring = {"q":"face oils","pageSize":"30","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_face_mists_face_essences_data():
    querystring = {"q":"mists and essences","pageSize":"30","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()



def fetch_cleansers_data():
    querystring = {"q":"cleansers","pageSize":"30","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_face_wash_data():
    querystring = {"q":"face wash","pageSize":"30","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_exfoliators_data():
    querystring = {"q":"face exfoliators","pageSize":"30","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_makeup_remover_data():
    querystring = {"q":"makeup removers","pageSize":"30","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()



def fetch_treatments_data():
    querystring = {"q":"facial treatments","pageSize":"30","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_face_serums_data():
    querystring = {"q":"face serums","pageSize":"30","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_acne_treatments_data():
    querystring = {"q":"acne treatments","pageSize":"30","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_eye_creams_eye_treatments_data():
    querystring = {"q":"eye creams & treatments","pageSize":"30","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_lip_balms_lip_treatments_data():
    querystring = {"q":"lip balms & treatments","pageSize":"30","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()



def fetch_masks_data():
    querystring = {"q":"masks","pageSize":"30","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_face_masks_data():
    querystring = {"q":"face masks","pageSize":"30","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_eye_masks_data():
    querystring = {"q":"eye masks","pageSize":"30","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()


def fetch_sunscreen_data():
    querystring = {"q":"sunscreen","pageSize":"30","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_face_sunscreen_data():
    querystring = {"q":"face sunscreen","pageSize":"30","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_body_sunscreen_data():
    querystring = {"q":"body sunscreen","pageSize":"30","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_skincare_tools_data():
    querystring = {"q":"skincare tools","pageSize":"30","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

