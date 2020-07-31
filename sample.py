from newspaper import Article

url = 'https://www.hindutamil.in/news/crime/567214-vijayakumar-arrested.html'
#url="https://tamil.oneindia.com/news/chennai/free-rise-distribution-ration-shop-on-august-5th-2020-392825.html"
#url="https://tamil.indianexpress.com/tamilnadu/sarathkumar-fake-calls-chennai-police-commissioner-chennai-news-210903/"
#url ="https://www.indiatv.in/india/national-karti-chidambaram-on-ram-mandir-no-need-any-new-place-of-worship-729897"
article = Article(url)
article.download()
article.parse()
print(article.text)
