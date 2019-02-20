class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCES_BASE_URL='https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_BASE_URL ='https://newsapi.org/v2/everything?sources={}&apiKey=a478b41d70f14d81a65045db223aeb87'
    NEWs_API_KEY = 'a478b41d70f14d81a65045db223aeb87'

    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True