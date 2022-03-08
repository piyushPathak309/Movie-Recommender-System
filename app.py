import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movie_list[movie_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        #i=int(i)
        recommended_movies.append(movies_list.iloc[i[0]].title)
    return recommended_movies


movie_list = pickle.load(open('movies.pkl', 'rb'))
movie_list = movie_list['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title("Movie Recommender System")

option = st.selectbox(
    'How would you like to be contacted?',
    (movie_list))

if st.button('Recommend'):
    recommendations=recommend(option)
    for i in recommendations:
        st.write(i)
