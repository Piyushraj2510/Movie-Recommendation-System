from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommenderr:
    def __init__(self, data):
        self.data = data
        self.vectorizer = CountVectorizer(max_features=5000, stop_words='english')
        self.vectors = self.vectorizer.fit_transform(data['tags']).toarray()
        self.similarity = cosine_similarity(self.vectors)

    def recommend(self, title, top_n=5):
        if title not in self.data['title'].values:
            return f"Movie '{title}' not found."
        index = self.data[self.data['title'] == title].index[0]
        distances = sorted(list(enumerate(self.similarity[index])), key=lambda x: x[1], reverse=True)
        recommended = [self.data.iloc[i[0]].title for i in distances[1:top_n+1]]
        return recommended
