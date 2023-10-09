import pickle
import streamlit as st
import requests
from PIL import Image
               

img=Image.open('netflix.png')

st.set_page_config(page_title='Netflix-Recommendation-System', page_icon=img,layout="wide")

with st.sidebar:
  with st.echo():
    " This is My first Python Project. "



def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('•---•» 𝙈𝙊𝙑𝙄𝙀 𝙍𝙀𝘾𝙊𝙈𝙈𝙀𝙉𝘿𝘼𝙏𝙄𝙊𝙉 𝙎𝙔𝙎𝙏𝙀𝙈 «•---• :cinema:',divider='rainbow')

movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "✎﹏﹏Type or Select a movie from the dropdown﹏﹏",
    movie_list
)

if st.button('★彡 Show Recommendation 彡★'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2]) 
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

hide_st_style = """
                <style>
                [data-testid="stAppViewContainer"]
                 { background-image: url("https://wallpaperaccess.com/full/2772922.png");
                   background-repeat: no-repeat;
                   background-size: 1500px 800px;
                   background-position-x: center;

                    border: 15px groove red;
                    padding: 25px;
                    background-clip: content-box;

                  }

                #Main Menu {visibility: hidden;}
                header {visibility: hidden;}
                footer {visibility: hidden;}
                   

                
                </style>

               
                """

st.markdown(hide_st_style, unsafe_allow_html=True)




