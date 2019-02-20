class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCES_BASE_URL='https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=faade62770d94f14a4c24e115dc25bc2'
    NEW_API_BASE_URL ='https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=faade62770d94f14a4c24e115dc25bc2'
    NEW_API_KEY = 'faade62770d94f14a4c24e115dc25bc2'
    
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