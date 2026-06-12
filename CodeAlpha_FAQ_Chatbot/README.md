AI FAQ Chatbot - E-commerce Support 🤖🛍️
This is a modern, AI-powered FAQ Chatbot built as Task 2 for the CodeAlpha Artificial Intelligence Internship.

It uses Natural Language Processing (NLP) to understand user questions and match them with the most relevant answers from a knowledge base, providing a seamless customer service experience.

✨ Innovative Features
Modern Web Interface: Built entirely in Python using Streamlit, featuring a sleek, responsive chat UI with smooth typing animations.
Intelligent Matching (NLP): Uses TF-IDF Vectorization and Cosine Similarity to understand the intent of a question, rather than relying on rigid, exact-keyword matching.
Persistent Chat Memory: Utilizes Streamlit's session_state to remember the conversation history during the session.
JSON Knowledge Base: FAQs are stored in an easily updatable, decoupled JSON format, making the bot highly scalable for real-world e-commerce stores.
🛠️ Technologies Used
Language: Python 3
Frontend UI: Streamlit (st.chat_message)
Machine Learning / Math: Scikit-Learn (TfidfVectorizer, cosine_similarity)
Natural Language Processing: NLTK (Tokenization)
Data Storage: JSON
🚀 How to Run Locally
Clone the master repository and navigate to this specific task folder:
bash

cd CodeAlpha_FAQ_Chatbot
Create and activate a Python Virtual Environment:
bash

python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install the required dependencies:
bash

pip install streamlit nltk scikit-learn
Launch the application:
bash

streamlit run app.py
Developed by Hafsat Abdulhamid for the CodeAlpha Internship.