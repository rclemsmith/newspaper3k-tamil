
import newspaper
from newspaper import Article
from newspaper import fulltext
from quart import Quart
from quart import request
from quart_cors import cors
import json
app = Quart(__name__)
app = cors(app, allow_origin="*")
# CORS(app)

@app.route("/extract")
async def article_extract():
    url = request.args.get('url')
    print(url)
    article = Article(url)
    article.download()
    article.parse()
    print(article.text)
    return json.dumps({
        "text" : article.text,
        "image" : article.top_image
        
    })

@app.route("/")
async def test_root():
    return "Hello from Newstuck Newspaper API. This API makes use of the python's Newspaper3K library to extract the main text content and the image source of the article, given the article's url. To retrieve the text and image, '/extract?url=<article_url_here>' "

if __name__ == "__main__":
    app.run(host='127.0.0.1',port="80",threaded=True)


