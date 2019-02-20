from flask import render_template,request,redirect,url_for
from app import app
from .request import get_news,search_news, get_sources
from .models import reviews
from .forms import ReviewForm
Review = reviews.Review


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

     # Getting popular news
    title = 'Home - Welcome to The best News Articles Website Online'

    popular_news = get_sources('everything')
   

    
    return render_template('index.html', title = title,popular = popular_news)



@app.route('/news/<id>')
def news(id):

    '''
    View news page function that returns the news details page and its data
    '''
    news = get_news(id)

    title = f'{id}'
   

    return render_template('news.html',title = title,news=news)

@app.route('/search/<news_author>')
def search(news_author):
    '''
    View function to display the search news
    '''
    news_author_list = news_author.split(" ")
    news_author_format = "+".join(news_author_list)
    searched_news = search_news(news_author_format)
    title = f'search news for {news_author}'
    return render_template('search.html',news = searched_news)

@app.route('/news/review/new/<author>', methods = ['GET','POST'])
def new_review(author):
    
    form = ReviewForm()
    news = get_news(author)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(news.author,title,news.urlToImage,review)
        new_review.save_review()
        return redirect(url_for('news',title = news.title ))

    title = f'{news.title} review'
    return render_template('new_review.html',title = title, review_form=form, news=news)
