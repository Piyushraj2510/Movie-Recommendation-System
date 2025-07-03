## 📽️ Movie Recommendation System 🎬

A content-based movie recommendation system built using **pandas**, **scikit-learn**, and deployed with **Streamlit**. This app suggests similar movies based on plot, genre, cast, and crew — using the TMDB 5000 Movie Dataset.

---

📂 **Dataset Source**: [Kaggle - TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

---

### 📁 Project Structure

```
Movie-Recommendation-System/
├── app.py                  ← Streamlit frontend
├── recommender.py          ← Recommendation engine
├── preprocess.py           ← Data cleaning and feature engineering
├── tmdb_5000_movies.csv
│── tmdb_5000_credits.csv
├── requirements.txt
└── README.md
```

---

### ⚙️ How It Works

1. Loads and merges movie metadata and credits.
2. Extracts meaningful features: `overview`, `genres`, `keywords`, `cast`, `director`.
3. Converts textual data into numerical vectors using `CountVectorizer`.
4. Calculates **cosine similarity** between movies.
5. Suggests top 5 similar movies based on input.

---

### 📦 Installation

#### 🖥️ Run Locally

1. **Clone the repo:**

   ```bash
   git clone https://github.com/Piyushraj2510/Movie-Recommendation-System.git
   cd Movie-Recommendation-System
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**

   ```bash
   streamlit run app.py
   ```

---

### 🧠 Example

**Input**: `Inception`
**Output**:

* The Dark Knight Rises
* Interstellar
* The Prestige
* Batman Begins
* The Dark Knight

---

### 📚 Tech Stack

* Python 🐍
* Pandas
* scikit-learn
* Streamlit
* TMDB Dataset (from Kaggle)

---

### ✨ Future Enhancements

* Add movie posters via TMDB API
* Add user ratings or collaborative filtering
* Add genre/year filters
* Better NLP using TF-IDF or BERT

---

### 🙌 Credits

* Dataset: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
* Inspired by various NLP content-based filtering tutorials

---

### 📜 License

MIT License © 2025 [Piyush Raj](https://github.com/Piyushraj2510)

---
