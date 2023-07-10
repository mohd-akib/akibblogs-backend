from chalice import Chalice
from chalicelib.articles import article_list

app = Chalice(app_name='akibblogs-backend')


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/articles')
def articles():
    return article_list


@app.route('/articles/{article_id}')
def get_one_article(article_id):
    for article in article_list:
        if article.get('id') == article_id:
            return article

    raise Exception("Something went wrong")
