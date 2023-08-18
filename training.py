import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import time
import joblib
from sklearn.linear_model import LogisticRegression


starting_time = time.time()
# IMDb veri kümesini yükleyin
df = pd.read_csv("dataset/IMDB Dataset.csv")

# Veri kümesini olumlu ve olumsuz olarak etiketleyin (1: Olumlu, 0: Olumsuz)
df['sentiment'] = np.where(df['sentiment'] == 'positive', 1, 0)

# Metin verilerini ön işleyin
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def preprocess_text(text):
    words = text.split()
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return ' '.join(words)


df['review'] = df['review'].apply(preprocess_text)
print("ne kadar sürüyo", time.time() - starting_time)
# Metin verilerini sayısal özelliklere dönüştürmek için CountVectorizer kullanın
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X = vectorizer.fit_transform(df['review'])
y = df['sentiment']

# Verileri eğitim ve test kümelerine ayırın
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("ne kadar sürüyo 2", time.time() - starting_time)
# Naive Bayes sınıflandırıcısını eğitin
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

model_filename = "logistic_regression_model.pkl"
joblib.dump(classifier, model_filename)
print("Model saved as", model_filename)
# Test verilerini kullanarak modeli değerlendirin
y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

end_time = time.time()
print("Elapsed time is", end_time - starting_time)
ö