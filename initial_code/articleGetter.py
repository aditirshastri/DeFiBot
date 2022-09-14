from newspaper import Article

# Testing the fine tuning
# pulling an article from our github repo
# and parsing all the data to train the model

url = 'https://incentivized.substack.com/p/this-is-why-the-curve-wars-are-being'
article = Article(url)

article.download()

article.parse()

print(article.text)
