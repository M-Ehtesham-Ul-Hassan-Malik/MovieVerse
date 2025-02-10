import pickle
import streamlit as st
import requests
import os
import gdown

# Page Configuration (MUST BE FIRST)
st.set_page_config(page_title="Netflix-like Recommender", layout="wide")

# Google Drive se download karne ke liye direct link
drive_file_id = "15OVcpDYArS81gt5s8dzh4NUdzhHVQF0X"  # Apni file ka ID yahan paste karo
drive_link = f"https://drive.google.com/uc?id={drive_file_id}"


# Check if similarity.pkl exists, if not, download
if not os.path.exists("similarity.pkl"):
    with st.spinner("Downloading model... Please wait!"):
        gdown.download(drive_link, "similarity.pkl", quiet=False)

# Load Data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Custom CSS for a Netflix-like UI
st.markdown("""
<style>
:root {
    --netflix-red: #E50914;
    --netflix-dark: #141414;
    --netflix-gray: #808080;
}

* {
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    margin: 0;
    padding: 0;
}

body {
    background: var(--netflix-dark);
}

/* Set the overall app background */
.stApp {
    background: linear-gradient(to right, rgba(20, 20, 20, 0.9) 0%, rgba(20, 20, 20, 0.7) 100%), 
                url('https://assets.nflxext.com/ffe/siteui/vlv3/9c5457b8-9ab0-4a04-9fc1-e608d5670f1a/710f74e0-7158-408e-8d9b-23c219dee5df/IN-en-20210719-popsignuptwoweeks-perspective_alpha_website_small.jpg');
    background-size: cover;
}

/* Top Navigation Bar */
.navbar {
    display: flex;
    align-items: center;
    padding: 10px 50px;
    background-color: var(--netflix-dark);
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 100;
}

.navbar img {
    height: 50px;
}

.navbar ul {
    list-style: none;
    display: flex;
    margin-left: auto;
}

.navbar ul li {
    margin-left: 30px;
    color: white;
    font-weight: bold;
    cursor: pointer;
    transition: color 0.3s;
}

.navbar ul li:hover {
    color: var(--netflix-red);
}

/* Main Content Container */
.main-content {
    padding-top: 100px; /* To prevent overlap with fixed navbar */
    width: 90%;
    margin: auto;
}

/* Movie Card Styling */
.movie-card {
    transition: transform 0.3s ease;
    border-radius: 8px;
    overflow: hidden;
    margin-bottom: 20px;
    background: #000;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
}

.movie-poster-container {
    position: relative;
    overflow: hidden;
    border-radius: 8px;
}

.movie-poster {
    width: 100%;
    height: 300px;
    object-fit: cover;
    transition: transform 0.3s ease;
}

.movie-card:hover .movie-poster {
    transform: scale(1.08);
}

.movie-details {
    padding: 15px;
    background: #141414;
}

.movie-title {
    color: white;
    font-weight: bold;
    margin: 0;
    font-size: 16px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.movie-info {
    color: var(--netflix-gray);
    font-size: 14px;
    margin: 5px 0 0;
}

/* Custom styling for Streamlit selectbox and button */
.stSelectbox div[data-baseweb="select"] > div {
    background-color: rgba(36, 36, 36, 0.8) !important;
    color: white !important;
    border: 1px solid var(--netflix-gray) !important;
    border-radius: 4px !important;
    padding: 12px !important;
}

.stButton button {
    background-color: var(--netflix-red) !important;
    color: white !important;
    border: none !important;
    padding: 12px 30px !important;
    border-radius: 4px !important;
    font-weight: bold !important;
    transition: all 0.3s ease !important;
}

.stButton button:hover {
    background-color: #F40612 !important;
    transform: scale(1.05);
}

/* Hide default Streamlit menu and footer */
#MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
.footer {
    position: fixed;
    bottom: 0;
    width: 100%;
    background: var(--netflix-dark);
    text-align: center;
    padding: 10px 0;
}
.stDeployButton {display: none;}
</style>
""", unsafe_allow_html=True)

# Function to fetch movie details from TMDB API
def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'poster': f"https://image.tmdb.org/t/p/w500/{data['poster_path']}" if data.get('poster_path') else "https://via.placeholder.com/500",
            'rating': round(data['vote_average'], 1) if data.get('vote_average') else 'N/A',
            'year': data['release_date'].split('-')[0] if data.get('release_date') else 'N/A'
        }
    return {'poster': "https://via.placeholder.com/500", 'rating': 'N/A', 'year': 'N/A'}

# Function to get movie recommendations
def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
    except IndexError:
        return []
    distances = sorted(enumerate(similarity[index]), reverse=True, key=lambda x: x[1])
    recommendations = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        details = fetch_movie_details(movie_id)
        recommendations.append({
            'title': movies.iloc[i[0]].title,
            'poster': details['poster'],
            'rating': details['rating'],
            'year': details['year']
        })
    return recommendations

# Load Data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Top Navigation Bar (Netflix-like header)
st.markdown("""
<div class="navbar">
    <img src="https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg" alt="Netflix Logo">
    <ul>
        <li>Home</li>
        <li>TV Shows</li>
        <li>Movies</li>
        <li>New & Popular</li>
        <li>My List</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Main Content Container
st.markdown('<div class="main-content">', unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white; margin-bottom: 40px;'>MovieVerse</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: var(--netflix-gray); margin-bottom: 40px;'>Find your next favorite movie with MovieVerse.</h2>", unsafe_allow_html=True)

# Movie Selection and Recommendations
selected_movie = st.selectbox("Search Movies", movies['title'].values, key="movie_select")
if st.button("Get Recommendations", key="recommend_btn"):
    with st.spinner("Finding the best matches..."):
        recommendations = recommend(selected_movie)
        if recommendations:
            st.markdown("<h2 style='color: white; margin: 40px 0 20px 0;'>Recommended For You</h2>", unsafe_allow_html=True)
            cols = st.columns(5)
            for idx, col in enumerate(cols):
                with col:
                    st.markdown(f"""
                        <div class="movie-card">
                            <div class="movie-poster-container">
                                <img src="{recommendations[idx]['poster']}" class="movie-poster">
                            </div>
                            <div class="movie-details">
                                <p class="movie-title">{recommendations[idx]['title']}</p>
                                <p class="movie-info">⭐ {recommendations[idx]['rating']} | {recommendations[idx]['year']}</p>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
        else:
            st.error("No recommendations found. Please try another movie.")
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; color: var(--netflix-gray); margin-top: 50px; padding: 20px;">
    <p>Developed with ❤️ by Ehtesham • Powered by TMDB</p>
</div>
""", unsafe_allow_html=True)
