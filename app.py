# import streamlit as st
# import pickle
# import requests

# def fetch_poster(movie_id):
#      url = "https://api.themoviedb.org/3/movie/{}?api_key=705cffb9563b7b7e9711bab983b95e46&language=en-US".format(movie_id)
#      data=requests.get(url)
#      data=data.json()
#      poster_path = data['poster_path']
#      full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
#      return full_path

# movies = pickle.load(open("movies_list.pkl","rb"))
# similarity = pickle.load(open("similarity.pkl","rb"))

# movies_list = movies['title'].values

# st.header("Movie Recommender System")



# selectvalue = st.selectbox("Select Movie from dropdown",movies_list)

# def recommend(movie):
#   index = movies[movies['title'] == movie].index[0]
#   distance = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
#   recommend_movie = []
#   recommend_poster=[]
#   for i in distance[1:6]:
#     movies_id=movies.iloc[i[0]].id
#     recommend_movie.append(movies.iloc[i[0]].title)
#     recommend_poster.append(fetch_poster(movies_id))
#   return recommend_movie,recommend_poster

# if st.button("Show Recommend"):
#     movie_name, movie_poster = recommend(selectvalue)
#     col1,col2,col3,col4,col5 = st.columns(5)
#     with col1:
#        st.write(movie_name[0])
#        st.image(movie_poster[0])
#     with col2:
#        st.write(movie_name[1])
#        st.image(movie_poster[1])
#     with col3:   
#         st.write(movie_name[2])
#         st.image(movie_poster[2])
#     with col4:
#         st.write(movie_name[3])
#         st.image(movie_poster[3])
#     with col5:
#         st.write(movie_name[4])
#         st.image(movie_poster[4])

# import streamlit as st
# import pickle
# import requests
# import time

# # Function to fetch poster URL using TMDb API
# def fetch_poster(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=705cffb9563b7b7e9711bab983b95e46&language=en-US"
#     try:
#         response = requests.get(url)
#         #response.raise_for_status()  # Raises an HTTPError for bad responses
#         data = response.json()
        
#         # Check for poster path in the response
#         poster_path = data.get('poster_path')
#         if poster_path:
#             full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
#             return full_path
#         else:
#             return 'https://via.placeholder.com/500x750?text=No+Image+Available'
        
#     except requests.exceptions.RequestException as e:
#         # Log the error and return a placeholder image
#         #st.error(f"Error fetching poster for movie ID {movie_id}: {e}")
#         return 'https://via.placeholder.com/500x750?text=image'

# # Load data from pickle files
# movies = pickle.load(open("movies_list.pkl", "rb"))
# similarity = pickle.load(open("similarity.pkl", "rb"))

# # Extract movie titles
# movies_list = movies['title'].values

# # Streamlit UI
# st.header("Movie Recommender System")

# # Dropdown for movie selection
# selectvalue = st.selectbox("Select Movie from dropdown", movies_list)

# # Function to recommend movies based on similarity
# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
#     recommend_movie = []
#     recommend_poster = []
    
#     # Iterate over top 5 similar movies
#     for i in distances[1:6]:
#         movie_id = movies.iloc[i[0]].id
#         recommend_movie.append(movies.iloc[i[0]].title)
#         poster_url = fetch_poster(movie_id)
        
#         # Output poster URL for debugging
#         #st.write(f"Poster URL for {movies.iloc[i[0]].title}: {poster_url}")
        
#         recommend_poster.append(poster_url)
    
#     return recommend_movie, recommend_poster

# # Show recommendations when button is clicked
# if st.button("Show Recommend"):
#     movie_name, movie_poster = recommend(selectvalue)
#     col1, col2, col3, col4, col5 = st.columns(5)
    
#     # Display recommendations and posters
#     for i, col in enumerate([col1, col2, col3, col4, col5]):
#         with col:
#             st.write(movie_name[i])
#             st.image(movie_poster[i])

import streamlit as st
import pickle
import requests

# Function to fetch poster URL using TMDb API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=705cffb9563b7b7e9711bab983b95e46&language=en-US"
    try:
        response = requests.get(url)
        data = response.json()
        
        # Check for poster path in the response
        poster_path = data.get('poster_path')
        if poster_path:
            full_path = f"https://image.tmdb.org/t/p/w92{poster_path}"  # Small icon size
            return full_path
        else:
            return 'https://via.placeholder.com/92x138?text=No+Image'
        
    except requests.exceptions.RequestException:
        # Return a placeholder image on error
        return 'https://via.placeholder.com/92x138?text=No+Image'

# Load data from pickle files
movies = pickle.load(open("movies_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# Extract movie titles
movies_list = movies['title'].values

# Streamlit UI
st.header("Movie Recommender System")

import streamlit.components.v1 as components

imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")


imageUrls = [
    fetch_poster(1632),
    fetch_poster(299536),
    fetch_poster(17455),
    fetch_poster(2830),
    fetch_poster(429422),
    fetch_poster(9722),
    fetch_poster(13972),
    fetch_poster(240),
    fetch_poster(155),
    fetch_poster(598),
    fetch_poster(914),
    fetch_poster(255709),
    fetch_poster(572154)
   
    ]


imageCarouselComponent(imageUrls=imageUrls, height=200)

# Dropdown for movie selection
selectvalue = st.selectbox("Select Movie from dropdown", movies_list)

# Function to recommend movies based on similarity
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommend_movie = []
    recommend_poster = []
    
    # Iterate over top 10 similar movies
    for i in distances[1:11]:  # Get 10 movies
        movie_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        poster_url = fetch_poster(movie_id)
        recommend_poster.append(poster_url)
    
    return recommend_movie, recommend_poster

# Show recommendations when button is clicked
if st.button("Show Recommendations"):
    movie_name, movie_poster = recommend(selectvalue)
    
    # Display recommendations in a list format
    for i in range(5):
        st.markdown(f"""
            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                <img src="{movie_poster[i]}" alt="{movie_name[i]}" style="width: 50px; height: auto; margin-right: 10px;">
                <span style="font-size: 18px;">{movie_name[i]}</span>
            </div>
        """, unsafe_allow_html=True)
