from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

# Example data
texts = ["Free money", "Work from home", "Meet singles", "Earn $5000 now", "This is not spam"]
labels = [1, 1, 1, 1, 0]  # 1: spam, 0: not spam

# Transform texts to feature vectors
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train SVM classifier
clf = SVC(kernel='linear')
clf.fit(X, labels)