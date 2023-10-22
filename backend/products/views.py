from django.shortcuts import render
import requests

url = "https://sephora.p.rapidapi.com/us/products/v2/list"

querystring = {"categoryId":"cat1080037","pageSize":"60","currentPage":"1"}

headers = {
	"X-RapidAPI-Key": "0a2db9998emshf122785976886e8p10b055jsnb3c36e679120",
	"X-RapidAPI-Host": "sephora.p.rapidapi.com"
}

def Products(request):
    response = requests.get(url, headers=headers, params=querystring).json()

    return render(request, 'products/product_list.html', {'response': response})

# Create your views here.
