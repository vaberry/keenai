from django.shortcuts import render
from django.views.generic.base import View
import requests
from dotenv import load_dotenv
import os
load_dotenv()

class Home(View):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            return render(request, 'home.html')
        
class Projects(View):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            return render(request, 'projects.html')
        
class About(View):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            return render(request, 'about.html')
        
class Newsletters(View):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            industry_subscribe_dict ={
                'defense': {
                    'link': 'https://embeds.beehiiv.com/eefc8670-7f04-4285-9250-5230991622cc?slim=true',
                    'image': 'base/img/defenseai.png'
                }
            }
            industry = kwargs.get('industry')
            industry_dict = industry_subscribe_dict.get(industry)
            print(industry_dict)
            context = {
                'industry_dict': industry_dict
            }

            # beehiiv_api_key = os.getenv("BEEHIIV_API_KEY")
            # url = "https://api.beehiiv.com/v2/publications"
            # headers = {
            #     "Accept": "application/json",
            #     "Authorization": f"Bearer {beehiiv_api_key}"
            # }

            # response = requests.get(url, headers=headers)

            # if response.status_code == 200:
            #     data = response.json()
            #     # Process the JSON data here
            #     print(data)
            # else:
            #     print("Request failed with status code:", response.status_code)


            return render(request, 'newsletters.html', context=context)
        
class Articles(View):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            return render(request, 'articles.html')