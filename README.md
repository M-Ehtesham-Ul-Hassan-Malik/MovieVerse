
# MovieVerse - Netflix-like Movie Recommendation System  

**MovieVerse** is a **content-based movie recommender system** built with **Streamlit**, trained on a **5000-movie dataset from Kaggle**. It provides personalized movie recommendations based on user-selected movies, leveraging machine learning and **TMDB API** for additional details like posters, ratings, and release years.  


## Features  
✅ **Netflix-style UI** with dark mode & interactive elements  
✅ **Movie recommendations** based on similarity scores  
✅ **Real-time fetching** of movie details (poster, rating, year)  
✅ **Responsive design** for desktop & mobile  



## Live Demo  
[MovieVerse](https://mymovieverse.streamlit.app/)  



## Dataset Details  

- **Source**: Kaggle (5000 movies)  
- **Features Used**:  
  - **Title**  
  - **Genre**  
  - **Overview (Description)**   
  - **Cast & Crew**   
- **Processing Steps**:  
  - Data cleaning  
  - Text preprocessing  
  - Feature extraction  

## Recommendation Model  

### Algorithm Used: Content-Based Filtering

This system **recommends movies** based on similarity between movies, calculated using **TF-IDF Vectorization** and **Cosine Similarity**.  

###  **Model Training Steps**  
1️⃣ **Data Preprocessing**  
   - Remove stopwords & special characters  
   - Convert text to lowercase  
   - Apply TF-IDF vectorization  
   
2️⃣ **Feature Engineering**  
   - Combine title, genres, and descriptions  
   - Convert into numerical vectors  

3️⃣ **Similarity Calculation**  
   - Compute **cosine similarity** between all movie vectors  
   - Find the **top 5 most similar movies**  

4️⃣ **Storing the Model**  
   - Save similarity scores as `similarity.pkl`  
   - Save movie metadata as `movies.pkl`  

## 🛠️ Tech Stack  
- **Python (3.8+)**  
- **Streamlit** (for UI & deployment)  
- **Pickle** (for saving models)  
- **Pandas & NumPy** (for data handling)  
- **Scikit-learn** (for vectorization & ML)  
- **TMDB API** (for fetching movie details)  
- **Google Drive API** (for model storage)  



## Installation & Usage  

### 1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/M-Ehtesham-Ul-Hassan-Malik/MovieVerse
cd MovieVerse
```

### 2️⃣ **Install Dependencies**  
```bash
pip install -r requirements.txt
```

### 3️⃣ **Run the Application**  
```bash
streamlit run system.py
```


## How It Works  
1️⃣ **Select a movie** from the dropdown menu.  
2️⃣ **Click "Get Recommendations"** to fetch similar movies.  
3️⃣ **Movie details** (poster, rating, release year) are displayed.  


## Future Enhancements  
✅ **Hybrid Model** (Collaborative + Content-Based Filtering)  
✅ **Deep Learning Integration** (Word2Vec / BERT)  
✅ **Real-time Trending Movies** (Integrate with TMDB API)  
✅ **User Authentication & Preferences**  




## 📧 Contact  
👤 **M Ehtesham Ul Hassan Malik**  
📧 Email: malikehtesham.ths@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/m-ehtesham-ul-hassan-malik/) | [GitHub](https://github.com/M-Ehtesham-Ul-Hassan-Malik/)  
