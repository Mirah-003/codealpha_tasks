import json
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st


try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

def load_faqs():
    with open('faqs.json', 'r') as file:
        return json.load(file)

faq_data = load_faqs()
faq_questions = list(faq_data.keys()) 
faq_answers = list(faq_data.values()) 

def get_best_answer(user_question):
    all_questions = faq_questions + [user_question]
    
    vectorizer = TfidfVectorizer()
    
    tfidf_matrix = vectorizer.fit_transform(all_questions)
    
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    best_match_index = similarity_scores.argmax()
    highest_score = similarity_scores[0][best_match_index]

    if highest_score < 0.2:
        return "I'm sorry, I don't understand. Could you rephrase your question or contact our human support?"
    
    return faq_answers[best_match_index]


st.title("🛍️ E-Commerce Support Bot")
st.write("Hello! I can help you with returns, shipping, and order tracking. Ask me anything!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a question... (e.g., How do I track my order?)"):
    
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})
    
    answer = get_best_answer(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(answer)
        
    st.session_state.messages.append({"role": "assistant", "content": answer})