
# 🎬 Movie Recommender System (TMDb Dataset)  

A **content-based** movie recommender system using **cosine similarity** and **TMDb API**. This project allows users to get movie recommendations based on their selection, along with movie posters.  

🚀 **Built with**:  
- 🐍 Python  
- 🖥️ Streamlit (for web interface)  
- 🔍 Cosine Similarity (for recommendations)  
- 🎞️ TMDb API (for fetching movie posters)  

---

## 📌 Features  
✅ **Movie Recommendation** – Get 5 similar movies based on your choice  
✅ **Movie Posters** – Fetch posters using TMDb API  
✅ **Interactive Web Interface** – Built using Streamlit  
✅ **Precomputed Similarity Model** – Fast recommendations  

---

## ⚙️ Installation  

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/meloch287/Movie-Recommendation-System-using-TMDb/tree/main.git
cd movie-recommender-system
```

2️⃣ **Install dependencies**  
```bash
pip install -r requirements.txt
```

3️⃣ **Download TMDb API key**  
- Sign up at [TMDb](https://www.themoviedb.org/) and get an API key  
- Replace the API key in `fetch_poster()` function  

---

## 🚀 Usage  

1️⃣ **Run the Streamlit app**  
```bash
streamlit run app.py
```

2️⃣ **Select a movie** from the dropdown list  

3️⃣ **Click "Show Recommendation"** to get 5 recommended movies  

---

## 🛠️ How It Works  

1️⃣ **Data Loading**  
- Precomputed similarity matrix (`similarity.pkl`) and movie list (`movie_list.pkl`) are loaded using `pickle`.  

2️⃣ **Cosine Similarity**  
- Finds similar movies based on cosine similarity scores.  

3️⃣ **Movie Poster Fetching**  
- Uses TMDb API to fetch movie posters dynamically.  

4️⃣ **Web Interface**  
- Built using Streamlit with a dropdown selection and image display.  

---

## 📜 License  
This project is **MIT Licensed**.  
