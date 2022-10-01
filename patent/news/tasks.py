from datetime import datetime

import requests
from bs4 import BeautifulSoup
from celery import shared_task

from .models import News


@shared_task(serializer='json')
def save_function(article_list):
    new_count = 0
    for article in article_list:
        try:
            News.objects.create(
                title = article['title'],
                link = article['link'],
                published = article['published'],
                source = article['source']
            )
            new_count += 1
        except Exception as e:
            print(e)
            break
    return print('finished')
    


@shared_task
def hackernews_rss():
    article_list = []
    r = requests.get('https://news.ycombinator.com/rss')
    soup = BeautifulSoup(r.content, features='xml')
    articles = soup.findAll('item')
    for a in articles:
        title = a.find('title').text
        link = a.find('link').text
        published_wrong = a.find('pubDate').text
        published = datetime.strptime(published_wrong, '%a, %d %b %Y %H:%M:%S %z')
        article = {
            'title': title,
            'link': link,
            'published': published,
            'source': 'Хакер RSS'
        }
        article_list.append(article)
    return save_function(article_list)
    
        
        
@shared_task
def sport_rss():
    article_list = []
    r = requests.get('http://stadium.ru/rss')
    soup = BeautifulSoup(r.content, features='xml')
    articles = soup.findAll('item')
    for a in articles:
        title = a.find('title').text
        link = a.find('link').text
        published_wrong = a.find('pubDate').text
        published = datetime.strptime(published_wrong, '%a, %d %b %Y %H:%M:%S %z')
        article = {
            'title': title,
            'link': link,
            'published': published,
            'source': 'Спорт RSS'
        }
        article_list.append(article)
    return save_function(article_list)
    
        
        
@shared_task
def politic_rss():
    article_list = []
    r = requests.get('https://news.mail.ru/rss/politics/91/')
    soup = BeautifulSoup(r.content, features='xml')
    articles = soup.findAll('item')
    for a in articles:
        title = a.find('title').text
        link = a.find('link').text
        published_wrong = a.find('pubDate').text
        published = datetime.strptime(published_wrong, '%a, %d %b %Y %H:%M:%S %z')
        article = {
            'title': title,
            'link': link,
            'published': published,
            'source': 'Политика RSS'
        }
        article_list.append(article)
    return save_function(article_list)
                   


@shared_task
def film_rss():
    article_list = []
    r = requests.get('https://xoppop.ru/index.php?mod=rss')
    soup = BeautifulSoup(r.content, features='xml')
    articles = soup.findAll('item')
    for a in articles:
        title = a.find('title').text
        link = a.find('link').text
        published_wrong = a.find('pubDate').text
        published = datetime.strptime(published_wrong, '%a, %d %b %Y %H:%M:%S %z')
        article = {
            'title': title,
            'link': link,
            'published': published,
            'source': 'Фильм RSS'
        }
        article_list.append(article)
    return save_function(article_list)
    
        
        
@shared_task
def economic_rss():
    article_list = []
    r = requests.get('http://news.mail.ru/rss/economics/')
    soup = BeautifulSoup(r.content, features='xml')
    articles = soup.findAll('item')
    for a in articles:
        title = a.find('title').text
        link = a.find('link').text
        published_wrong = a.find('pubDate').text
        published = datetime.strptime(published_wrong, '%a, %d %b %Y %H:%M:%S %z')
        article = {
            'title': title,
            'link': link,
            'published': published,
            'source': 'Экономика RSS'
        }
        article_list.append(article)
    return save_function(article_list)
        