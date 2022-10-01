from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import News
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@shared_task(serializer='json')
def save_function(article_list):
    source = article_list[0]['source']
    new_count = 0
    error = True
    try: 
        latest_article = News.objects.filter(source=source).order_by('-id')[0]
        print(latest_article.published)
        print('var TestTest: ', latest_article, 'type: ', type(latest_article))
    except Exception as e:
        print('Exception at latest_article: ')
        print(e)
        error = False
        pass
    finally:
        if error is not True:
            latest_article = None
    for article in article_list:
        if latest_article is None:
            try:
                News.objects.create(
                    title=article['title'],
                    link=article['link'],
                    published=article['published'],
                    source=article['source']
                )
                new_count += 1
            except Exception as e:
                print('failed at latest_article is none')
                print(e)
                break
        elif latest_article.published < article['published']:
            try:
                News.objects.create(
                    title=article['title'],
                    link=article['link'],
                    published=article['published'],
                    source=article['source']
                )
                new_count += 1
            finally:
                print('failed at latest_article.published < j[published]')
                break
        else:
            return print('news scraping failed')
    logger.info(f'New articles: {new_count} articles(s) added.')
    return print('finished')


@shared_task
def hackernews_rss():
    article_list = []
    try:
        print('Starting the scraping tool')
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
        print('Finished scraping the articles')
        return save_function(article_list)
    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)
        
        
@shared_task
def sport_rss():
    article_list = []
    try:
        print('Starting the scraping tool')
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
        print('Finished scraping the articles')
        return save_function(article_list)
    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)
        
        
@shared_task
def politic_rss():
    article_list = []
    try:
        print('Starting the scraping tool')
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
        print('Finished scraping the articles')
        return save_function(article_list)
    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)                


@shared_task
def film_rss():
    article_list = []
    try:
        print('Starting the scraping tool')
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
        print('Finished scraping the articles')
        return save_function(article_list)
    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)
        
        
@shared_task
def economic_rss():
    article_list = []
    try:
        print('Starting the scraping tool')
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
        print('Finished scraping the articles')
        return save_function(article_list)
    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)
        