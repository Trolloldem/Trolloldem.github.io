import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Read data and shuffle
df = pd.read_table("data.txt", sep="\t", header=None)
df = df.reindex(np.random.permutation(df.index))

df.reset_index(inplace=True, drop=True)

# See some elements of the dataset
print(df.head())

# Replace string labels with numerical ones
df[0] = df[0].replace('ham', 0)
df[0] = df[0].replace('spam', 1)

# Create the BoW model
count_vector = CountVectorizer(ngram_range=(1,1), lowercase=True, stop_words="english")

# Split the data between training and test 75 - 25 %
X_train_msg, X_test_msg, y_train, y_test = train_test_split(df[1], df[0])

# Get the features from the train, calculate them over the test
X_train = count_vector.fit_transform(X_train_msg)
X_test = count_vector.transform(X_test_msg)

# Get the words found in your BoW model
X_train_feature_list = count_vector.get_feature_names_out()
print(X_train_feature_list)

# Create a simple classifier and train it on train dataset
naive_bayes = MultinomialNB()
naive_bayes.fit(X_train, y_train)

# Classify the test elements
predictions = naive_bayes.predict(X_test)

# Calculate quality against real labels
print("Accuracy:", accuracy_score(predictions, y_test))
print("Precision:", precision_score(predictions, y_test))
print("Recall:", recall_score(predictions, y_test))
print("F1:", f1_score(predictions, y_test))


