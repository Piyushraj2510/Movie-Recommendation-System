import streamlit as st
from preprocess import load_and_merged_data, preprocess_data
from recommendor import MovieRecommenderr

# Load data once
@st.cache_data
def setup():
    movie_path = 'tmdb_5000_movies.csv'
    credit_path = 'tmdb_5000_credits.csv'
    raw = load_and_merged_data(movie_path, credit_path)
    processed = preprocess_data(raw)
    model = MovieRecommenderr(processed)
    return model, processed

model, processed_data = setup()

# App title
st.title("🎬 Movie Recommendation System")
st.markdown("Get movie recommendations based on **content similarity** (plot, genres, cast, etc).")

# Movie selector
movie_list = processed_data['title'].sort_values().tolist()
selected_movie = st.selectbox("Choose a movie", movie_list)

# Recommend button
if st.button("Recommend"):
    with st.spinner("Finding similar movies..."):
        recommendations = model.recommend(selected_movie)
    st.success("Top Recommendations:")
    for i, movie in enumerate(recommendations, 1):
        st.write(f"{i}. {movie}")
