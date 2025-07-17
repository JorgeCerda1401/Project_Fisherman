import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

import joblib

df = pd.read_csv('backend/spam.csv')

df['Category'] = df['Category'].apply(lambda x: 1 if x == 'spam' else 0)

X_train, X_test, Y_train, Y_test = train_test_split(df['Message'], 
                                                    df['Category'], 
                                                    random_state=0)

# Vectorizing text data
vectorizer = CountVectorizer(ngram_range=(1, 2)).fit(X_train)
X_train_vectorized = vectorizer.transform(X_train)
X_train_vectorized.toarray().shape

# Training with Support Vector Machine
model = SVC(kernel='linear') 
model.fit(X_train_vectorized, Y_train)

predictions = model.predict(vectorizer.transform(X_test))

# Save model
joblib.dump(model, "backend/FisherMan.pkl") 