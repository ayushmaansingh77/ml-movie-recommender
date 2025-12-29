import streamlit as st
import pickle
import requests
import pandas as pd
movies_df=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
def recommend(movie):
    movie_ind = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_ind]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recMov=[]
    for i in movie_list:
        recMov.append(movies_df.iloc[i[0]].title)

    return recMov
@st.cache_data(show_spinner=False)
def fetch_poster(movie_name):
    url = f"http://www.omdbapi.com/?t={movie_name}&apikey=41882f3e"
    data = requests.get(url).json()

    if data.get("Response") == "True":
        return data.get("Poster")
    else:
        return None



st.title('Movie Recommender System')
st.markdown("Discover movies similar to your favorite ones 🍿")
movies_list=movies_df['title'].values
selected_movie_name = st.selectbox(
    "Choose a movie",
    movies_list
)

if st.button('Recommend'):
    st.write(f" similar to **{selected_movie_name}**:")

    recommendations = recommend(selected_movie_name)

    cols = st.columns(5)

    for col, movie in zip(cols, recommendations):
        poster = fetch_poster(movie)
        with col:
            if poster:
                st.image(poster, use_container_width=True)
                st.caption(movie)
            else:
                st.write(movie)

