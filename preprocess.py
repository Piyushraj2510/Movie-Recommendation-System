import pandas as pd
import ast

def load_and_merged_data(movie_path, credit_path):
    movies = pd.read_csv(movie_path)
    credits = pd.read_csv(credit_path)
    movies = movies.merge(credits, on='title')
    return movies

def convert(obj):
    try:
        return [i['name'] for i in ast.literal_eval(obj)]
    except:
        return []

def get_top_cast(obj):
    try:
        return [i['name'] for i in ast.literal_eval(obj)][:3]
    except:
        return []

def get_director(obj):
    try:
        for i in ast.literal_eval(obj):
            if i['job'] == 'Director':
                return [i['name']]
        return []
    except:
        return []

def preprocess_data(movies):
    movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]
    movies['genres'] = movies['genres'].apply(convert)
    movies['keywords'] = movies['keywords'].apply(convert)
    movies['cast'] = movies['cast'].apply(get_top_cast)
    movies['crew'] = movies['crew'].apply(get_director)
    movies['overview'] = movies['overview'].fillna('')
    movies['tags'] = movies['overview'] + ' ' + \
                     movies['genres'].apply(lambda x: ' '.join(x)) + ' ' + \
                     movies['keywords'].apply(lambda x: ' '.join(x)) + ' ' + \
                     movies['cast'].apply(lambda x: ' '.join(x)) + ' ' + \
                     movies['crew'].apply(lambda x: ' '.join(x))
    movies['tags'] = movies['tags'].apply(lambda x: x.lower())
    return movies[['movie_id', 'title', 'tags']]
