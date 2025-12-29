# 📌 Movie Recommender System (Streamlit)

## 🎬 Overview

This project is a **content-based movie recommender system** built for **learning and exploration**.  
The goal was **not** to build a production-scale system, but to understand how recommendation pipelines work **end-to-end** — from **feature engineering** to **UI deployment**.

The project was genuinely fun to build and helped me explore several **practical machine learning and engineering concepts** along the way.

---

## What the App Does

→ Select a movie from a list  
→ Get **Top-5 similar movies** based on content similarity  
→ View movie posters for a better user experience  
→ Simple, clean UI built using **Streamlit**

---

## 🧠 Concepts Explored

This project helped me explore and understand:

→ **Content-based recommendation systems**  
→ **Vectorization** (TF-IDF / CountVectorizer)  
→ **Cosine similarity**  
→ **Similarity matrices**  
→ **Model persistence** using `pickle`  
→ **Streamlit** for rapid ML app development  
→ **Caching** to improve performance  
→ **External APIs** (OMDb for posters)  
→ **Deployment constraints** (memory limits, free tiers, cold starts)  
→ **Git LFS** for managing large ML artifacts  

The learning came as much from **debugging and deployment** as from the ML itself.

---

## 🛠 Tech Stack

→ **Python**  
→ **pandas**, **NumPy**  
→ **scikit-learn**  
→ **Streamlit**  
→ **OMDb API** (for posters)

---

## 📦 Project Structure
app.py
movies.pkl
similarity.pkl
requirements.txt
README.md


---

## ⚠️ Notes on Deployment

This project uses a **precomputed similarity matrix**, which is **memory-heavy by design**.  
On some **free hosting platforms** with strict RAM limits, this can cause issues.

This is a **known and expected trade-off**, and part of what made the project a good learning experience.  
The app runs correctly in environments with **sufficient memory** and when run **locally**.

---

## 🎯 Project Intent

This project was built as a **learning exercise**, not as a production system.

→ It helped me understand **recommender systems** more deeply  
→ It exposed me to **real-world constraints** beyond just ML code  
→ It reinforced the importance of **system design and trade-offs**

Overall, it was a **small project with big learning value**.

---

## 🙌 Final Thoughts

This was a **fun project** to work on.  
It wasn’t about perfection — it was about **exploration, curiosity, and learning by doing**.

I’m glad I built it 🙂
Please give it a try!
https://ml-movie-recommender-fvqgacmxyfaejawflhs9sa.streamlit.app/
