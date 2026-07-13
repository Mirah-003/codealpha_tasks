"""
NLP-Powered FAQ Chatbot for E-Commerce Customer Support.
Uses TF-IDF Vectorization and Cosine Similarity to semantic-match user queries against a JSON knowledge base.
"""
import json
import os
from typing import Dict, List, Tuple
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# Ensure NLTK punkt tokenizer is available without failing in offline environments
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    try:
        nltk.download('punkt', quiet=True)
    except Exception as e:
        print(f"Warning: Could not download NLTK punkt tokenizer: {e}")

FAQ_PATH = os.path.join(os.path.dirname(__file__), "faqs.json")


def load_faqs(filepath: str = FAQ_PATH) -> Dict[str, str]:
    """Loads knowledge base questions and answers from JSON file."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


def get_best_answer(user_question: str, faq_data: Dict[str, str] = None, threshold: float = 0.2) -> Tuple[str, float]:
    """
    Computes semantic similarity between the user query and knowledge base questions using TF-IDF.
    
    Args:
        user_question: The raw text string input from the user.
        faq_data: Optional dictionary of {question: answer}. Defaults to loading faqs.json.
        threshold: Minimum cosine similarity score required to return a matched answer.
        
    Returns:
        Tuple[str, float]: (Best matched answer or fallback message, Cosine similarity score)
    """
    if faq_data is None:
        faq_data = load_faqs()

    if not faq_data or not user_question.strip():
        return "I'm sorry, I don't understand. Could you rephrase your question or contact our human support?", 0.0

    faq_questions = list(faq_data.keys())
    faq_answers = list(faq_data.values())

    all_questions = faq_questions + [user_question]
    vectorizer = TfidfVectorizer(stop_words="english", lowercase=True)
    
    try:
        tfidf_matrix = vectorizer.fit_transform(all_questions)
    except ValueError:
        # Handles edge case where query contains only stop words or symbols
        return "I'm sorry, I couldn't process those terms. Could you rephrase your question with more details?", 0.0

    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])[0]
    best_match_index = int(similarity_scores.argmax())
    highest_score = float(similarity_scores[best_match_index])

    if highest_score < threshold:
        return "I'm sorry, I don't understand. Could you rephrase your question or contact our human support?", highest_score

    return faq_answers[best_match_index], highest_score


def run_ui():
    """Renders the interactive Streamlit E-Commerce Support interface."""
    st.set_page_config(page_title="E-Commerce Support Bot", page_icon="🛍️", layout="centered")
    st.title("🛍️ E-Commerce Support Bot")
    st.write("Hello! I can help you with returns, shipping, payment options, and order tracking. Ask me anything!")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask a question... (e.g., How do I track my order?)"):
        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.messages.append({"role": "user", "content": prompt})

        answer, score = get_best_answer(prompt)

        with st.chat_message("assistant"):
            st.markdown(answer)
            if score > 0:
                st.caption(f"Semantic Match Confidence: `{score:.2%}`")

        st.session_state.messages.append({"role": "assistant", "content": answer})


if __name__ == "__main__":
    run_ui()