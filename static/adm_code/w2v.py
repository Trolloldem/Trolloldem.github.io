import gensim.downloader # remember to "pip install gensim"

print(list(gensim.downloader.info()["models"].keys()))

glove_vector = gensim.downloader.load("glove-wiki-gigaword-300")

print(glove_vector.most_similar("computers"))
