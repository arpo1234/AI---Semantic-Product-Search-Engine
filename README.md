# AI - Semantic Product Search Engine

**Dazzle AI** is a smart e-commerce semantic search application built with **Django**, **ChromaDB**, and **Sentence-Transformers**. Unlike traditional keyword-based search engines, Dazzle AI understands the intent and context of customer queries using vector embeddings, returning the most relevant products along with a real-time **AI Match Score**.

---

## ✨ Features

- **Semantic Intent Search:** Powered by `SentenceTransformer` (`all-MiniLM-L6-v2`) to capture deep natural language context beyond simple keyword matching.
- **High-Performance Vector Storage:** Uses **ChromaDB** for fast vector similarity search and metadata retrieval.
- **Dynamic AI Match Score:** Calculates precise match percentages using L2-to-Cosine similarity transformation for every result.
- **Responsive E-Commerce UI:** Clean, intuitive UI built with **Bootstrap 5**, featuring interactive product cards, lazy-loaded thumbnails, and discount displays.

---

## 🛠️ Tech Stack

- **Backend:** Python 3.x, Django 5.x / 6.x
- **Vector Database:** ChromaDB
- **ML / AI Model:** Sentence-Transformers (`all-MiniLM-L6-v2`)
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5

---

## 📁 Project Structure

```text
dazzle_search/
│
├── core/
│   ├── templates/
│   │   └── core/
│   │       └── index.html      # Main Search Interface
│   ├── views.py                # Vector Search Logic & Rendering
│   └── ...
│
├── dazzle_vector_db/           # ChromaDB Persistent Storage
├── dazzle_search/
│   ├── settings.py             # Global Project Configuration
│   └── urls.py
│
├── manage.py
└── requirements.txt