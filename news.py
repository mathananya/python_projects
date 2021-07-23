import flask
import requests
appx = flask.Flask(__name__)
appx.debug = True



@appx.route('/')
def start():
	var1 = 5
	var2 = "Hi .. this is content that is being created in python."
	return flask.render_template("file2.html", content = var2, var1 = var1)

@appx.route('/next')
def next():
	var1 = "200300"
	return flask.render_template("file1.html", var9 = var1)

@appx.route('/go')
def go():
	main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=cf4be1526e7b4fcf9e5fddbf5ae685a2"
	open_bbc_page = requests.get(main_url).json()
	article_list = open_bbc_page["articles"]
	
	link_list = []
	title_list = []
	snippet_list = []
	img_list = []
	for article in article_list:
		link_list.append(article["url"])
		title_list.append(article["title"])
		snippet_list.append(article["description"])
		img_list.append(article["urlToImage"])
	return flask.render_template("bbc_news.html", link_list=link_list, title_list=title_list,
			snippet_list=snippet_list, img_list=img_list)
	
	
	

appx.run()