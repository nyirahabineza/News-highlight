class News:
    '''
    New class to define New Objects
    '''

    def __init__(self,title,author,description,url,urlToImage,publishedAt,content):
        self.author =author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content

class Source:
    '''
    Sources class to define Sources Objects
    '''

    def __init__(self,id,name,description):
        self.id=id
        self.name=name
        self.description = description