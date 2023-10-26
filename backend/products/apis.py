import requests

base_url = "https://sephora.p.rapidapi.com/us/products/v2/search"
base_header = {
        "X-RapidAPI-Key": "0a2db9998emshf122785976886e8p10b055jsnb3c36e679120",
        "X-RapidAPI-Host": "sephora.p.rapidapi.com"
    }

def fetch_perfume_data():
    querystring = {"q":"Womens perfume","pageSize":"60","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()


def fetch_perfume_oil_data():
    querystring = {"q":"perfume oil","pageSize":"30","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()


def fetch_body_mist_hair_mist_data():
    querystring = {"q":"body mist","pageSize":"29","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()


def fetch_cologne_data():
    querystring = {"q":"men's cologne","pageSize":"60","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_fragrance_bestsellers_data():
    querystring = {"q":"most popular fragrances","pageSize":"60","currentPage":"1"}
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
    querystring = {"q":"perfume clean fragrance","pageSize":"60","currentPage":"1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()

def fetch_affordable_fragrances_data():
    querystring = {"q":"affordable perfume","pageSize":"60","currentPage":"1","pl":"200","sortBy":"P_BEST_SELLING:1"}
    return requests.get(base_url, headers=base_header, params=querystring).json()


#def fragrance_notes_guide():

#def find_signature_scent():



