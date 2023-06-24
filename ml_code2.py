import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
spam_df = pd.read_csv("Youtube01-Psy.csv")
spam_df['spam'] = spam_df['CLASS'].apply(lambda x: 1 if x==1 else 0)
# create train/test split
x_train, x_test, y_train, y_test = train_test_split(spam_df.CONTENT, spam_df.spam, test_size = 0.75)
# find word count and store data as a matrix
cv =  CountVectorizer()
x_train_count = cv.fit_transform(x_train.values)
x_train_count.toarray()
# train model
model=MultinomialNB()
model.fit(x_train_count, y_train)
# pre test ham comment
comment_ham = ["hey wanna be up for the game?"]
comment_ham_count = cv.transform(comment_ham)
model.predict(comment_ham_count)
# pre-test spam comment
comment_spam = ["hey wanna be up for the game?"]
comment_spam_count = cv.transform(comment_spam)
model.predict(comment_spam_count)
# test model
x_test_count = cv.transform(x_test)
model.score(x_test_count, y_test)
model.predict(comment_spam_count)
if(model.predict(comment_spam_count)==1):
  print("Spam comment ")
else:
  print("Not spam comment")