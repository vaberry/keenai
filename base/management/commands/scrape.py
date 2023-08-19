from django.core.management.base import BaseCommand
from selenium import webdriver
from bs4 import BeautifulSoup
from base.models import Newsletters

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            url = 'https://defenseai.beehiiv.com/'
            driver = webdriver.Chrome()
            driver.get(url)
            driver.implicitly_wait(10)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.implicitly_wait(10)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            newsletter_links = soup.find_all('a', class_='group flex h-full w-full border transition-all group-hover:brightness-110 rounded-lg flex-col')
            for newsletter_link in newsletter_links:
                newsletter_soup = BeautifulSoup(str(newsletter_link), 'html.parser')
                full_url = f"https://defenseai.beehiiv.com{newsletter_link['href']}"
                image = newsletter_soup.find('img')['src']
                title = newsletter_soup.find('h2', class_='break-words line-clamp-4 text-lg sm:text-xl font-bold font-open_sans').text
                subtitle = newsletter_soup.find('p', class_='break-words line-clamp-2 text-sm font-regular font-open_sans').text
                author = newsletter_soup.find('span', class_='text-xs font-semibold').text
                datetime = newsletter_soup.find('time')['datetime']
            
                newsletters = Newsletters.objects.all()
                for newsletter in newsletters:
                    newsletter.delete()
                new_newsletter = Newsletters.objects.create(
                    newsletter_url=full_url,
                    image_url=image,
                    title=title,
                    subtitle=subtitle,
                    author=author,
                    datetime=datetime
                )
                new_newsletter.save()
        except Exception as e:
            print(e)
