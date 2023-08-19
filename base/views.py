from django.shortcuts import render
from django.views.generic.base import View
import requests
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

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
            context = {
                'industry_dict': industry_dict
            }

            return render(request, 'newsletters.html', context=context)
        
class Articles(View):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            return render(request, 'articles.html')