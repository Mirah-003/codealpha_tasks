# 🛍️ E-Commerce Support FAQ Chatbot (`CodeAlpha Task 2`)

[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-1.3+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Tests](https://img.shields.io/badge/PyTest-100%25_Passing-3b82f6?style=for-the-badge&logo=pytest)](https://docs.pytest.org/)

> **CodeAlpha Applied AI & NLP Internship Showcase**  
> An NLP-powered customer service triage engine using **TF-IDF Vectorization** and **Cosine Similarity** to match natural language queries against an extensible, decoupled JSON knowledge base with real-time confidence scoring.

---

## 💡 The Engineering Problem & Solution

Rule-based customer support bots that rely on exact string matching frequently fail when users paraphrase questions (e.g., asking *"Where is my order tracking link?"* instead of *"How can I track my order?"*). Conversely, deploying heavyweight LLMs for simple static E-Commerce FAQs introduces unnecessary cloud latency, high API costs, and hallucination risks around exact store policies (`30-day returns`, `student discounts`).

**Task 2 (`CodeAlpha_FAQ_Chatbot`)** bridges this gap by implementing a **fast, deterministic semantic matching engine**. By converting user queries and canonical FAQ questions into sparse high-dimensional vector representations (`TfidfVectorizer`), the system computes exact angle-based similarity scores (`cosine_similarity`) in `<5 milliseconds` while enforcing strict confidence thresholds (`≥20%`) before answering.

---

## 🏗️ Architectural Workflow

```
+----------------------------------------------------------------------------+
|                            FAQ Chatbot Pipeline                            |
+----------------------------------------------------------------------------+
|                                                                            |
|   [User Query] ----> (NLTK Tokenization & Stop-Word Filtering)            |
|                                |                                           |
|                                v                                           |
|                 [TF-IDF High-Dimensional Matrix]                           |
|                                |                                           |
|                                v                                           |
|           [Cosine Similarity vs. Decoupled faqs.json]                      |
|                                |                                           |
|             +------------------+------------------+                        |
|             | (Score >= 0.2)                      | (Score < 0.2)          |
|             v                                     v                        |
|    [Return Best Match + Score]       [Trigger Out-of-Domain Fallback]      |
+----------------------------------------------------------------------------+
```

### Key Technical Highlights
* **Decoupled JSON Taxonomy (`faqs.json`):** Separates application logic (`app.py`) from domain data, enabling content managers to update return windows or shipping guidelines without touching Python code.
* **Semantic Thresholding (`get_best_answer`):** Prevents irrelevant or off-topic questions from triggering incorrect advice by returning a helpful human-support escalation message when similarity scores drop below `0.2`.
* **Stateful Streamlit Memory (`st.session_state`):** Maintains full multi-turn chat history cleanly within the user's browser session.

---

## 🛠️ Tech Stack & Structure

```
CodeAlpha_FAQ_Chatbot/
├── app.py                # Core TF-IDF vectorizer engine & Streamlit UI logic
├── faqs.json             # Structured E-Commerce knowledge base (returns, shipping, tracking)
├── requirements.txt      # Minimal dependencies (streamlit, scikit-learn, nltk, pytest)
└── tests/
    └── test_faq_bot.py   # Automated PyTest suite verifying vectorizer thresholds
```

---

## 🚀 Local Quickstart & Testing

### 1. Setup Virtual Environment
```bash
cd CodeAlpha_FAQ_Chatbot
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run Automated Tests
```bash
PYTHONPATH=. pytest -v tests/test_faq_bot.py
```
Expected output:
```text
tests/test_faq_bot.py::test_load_faqs PASSED                              [ 20%]
tests/test_faq_bot.py::test_exact_match_queries PASSED                    [ 40%]
tests/test_faq_bot.py::test_semantic_paraphrased_queries PASSED           [ 60%]
tests/test_faq_bot.py::test_out_of_domain_queries PASSED                  [ 80%]
tests/test_faq_bot.py::test_empty_and_stopword_queries PASSED             [100%]
```

### 3. Launch the Streamlit App
```bash
streamlit run app.py
```
Access the interactive web UI at `http://localhost:8501`.