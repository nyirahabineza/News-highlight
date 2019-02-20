import urllib.request,json
from app.models import news
from app import app

News = news.News
Source = news.Source
#     global api_key,source_base_url,articles_base_url
api_key = app.config['NEWS_API_KEY']
source_base_url = app.config['NEWS_SOURCES_BASE_URL']
news_base_url = app.config['NEWS_API_BASE_URL']


def get_sources(category):
    '''Function that gets json response to our url request'''
    get_sources_url = source_base_url.format(api_key)
    print(get_sources_url)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)
    # print(source_results)
    return source_results

def process_results(source_list):
    '''
    Function that processes the source result and transform to a list of objects
    Args:
        source_list: A list of dictionaries that contain news sources
    Returns:
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')

        source_object = Source(id,name,description)
        source_results.append(source_object)

    return source_results

def get_news(id):
    '''Function thet gets the json response to our url request'''
    get_news_url = news_base_url.format(id)
    print(get_news_url)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        print

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            print(news_results_list)
            news_results = process_articles(news_results_list)

    return news_results

def process_articles(news_list):
    '''
    Function that processes the news result and transforms them to a list of objects
    Args:
        news_list: a list of dictionaries that contain articles
    Returns:
        news_results: a list of news objects
    '''
    news_results = []
    for news_item in news_list:
        title = news_item.get('title')
        author= news_item.get('author')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')
        if urlToImage:
            news_object = News(title,author,description,url,urlToImage,publishedAt,content)
            news_results.append(news_object)

    return news_results


def search_news(news_id):
    search_news_url = 'https://newsapi.org/v2/everything?api_key={}&query={}'.format(api_key,news_id)
   
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_articles = None

        if  search_news_response['articles']:
            search_news_list = search_news_response['articles']
            search_news_articles = process_articles(search_news_list)


    return search_news_articles