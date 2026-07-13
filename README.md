# 🧠 Applied AI & NLP Engineering Portfolio (`CodeAlpha Internship`)

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Computer_Vision-0052FF?style=for-the-badge&logo=yolo&logoColor=white)](https://docs.ultralytics.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-TF--IDF_%7C_Cosine-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Web Speech API](https://img.shields.io/badge/Web_Speech_API-Voice_I%2FO-ff7eb3?style=for-the-badge&logo=googlechrome&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

> **CodeAlpha Applied Artificial Intelligence Internship Showcase**  
> A production-oriented collection of three distinct AI/ML and Natural Language Processing systems engineered to solve real-world challenges across **multilingual speech translation**, **semantic customer support triage**, and **real-time multi-object video tracking**.

---

## 🏗️ System Architecture & Task Matrix

Each subproject inside this repository represents a complete, self-contained AI system built from the ground up with modular code architecture, isolated dependencies, and automated test coverage.

| Task | Project Name & Link | Domain & Core Problem | Key AI / Mathematical Models | Frontend / UI Architecture | Key Performance Metric |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Task 1** | **[🌍 Smart Language Translator](./CodeAlpha_LanguageTranslationTool)** | Eliminating manual typing barriers in multilingual web translation | MyMemory Neural MT API + Native Speech-to-Text / Text-to-Speech | Vanilla ES6 JS + Glassmorphism CSS3 (`backdrop-filter`) | Asynchronous, zero-blocking UI execution (`<100ms` DOM updates) |
| **Task 2** | **[🛍️ E-Commerce FAQ Chatbot](./CodeAlpha_FAQ_Chatbot)** | Semantic query matching without rigid keywords or expensive LLM calls | High-Dimensional Sparse TF-IDF Vectorization + Cosine Similarity | Streamlit (`st.chat_message`) + Stateful Session Memory | `<5ms` local vector similarity search with `≥20%` confidence thresholds |
| **Task 3** | **[🎥 Real-Time Object Tracker](./CodeAlpha_Object_Tracker)** | Persistent multi-object identification across video frame occlusions | Ultralytics YOLOv8 Architecture + ByteTrack / BoT-SORT MOT Algorithms | OpenCV Dynamic Video Overlay (`cv2.putText` / `cv2.imshow`) | Real-time live webcam processing with delta-timestamp FPS counters |

---

## 🛠️ Repository Directory Structure

```
codealpha_tasks/
├── CodeAlpha_LanguageTranslationTool/ # Task 1: Multilingual Voice & Text Translator
│   ├── index.html                     # Semantic HTML5 layout with dual translation panels
│   ├── style.css                      # Responsive Glassmorphism design tokens & animations
│   ├── script.js                      # Asynchronous REST fetch & Web Speech API handlers
│   └── README.md                      # Task 1 architectural overview & quickstart guide
│
├── CodeAlpha_FAQ_Chatbot/             # Task 2: Semantic TF-IDF Customer Support Bot
│   ├── app.py                         # Modular TF-IDF vectorizer engine & Streamlit UI
│   ├── faqs.json                      # Decoupled E-Commerce knowledge base taxonomy
│   ├── requirements.txt               # Minimal dependencies (streamlit, scikit-learn, nltk, pytest)
│   ├── tests/
│   │   └── test_faq_bot.py            # Automated PyTest suite verifying cosine thresholds
│   └── README.md                      # Task 2 mathematical breakdown & quickstart guide
│
├── CodeAlpha_Object_Tracker/          # Task 3: Real-Time YOLOv8 Vision & MOT Pipeline
│   ├── tracker.py                     # Object-oriented tracking class & CLI argument parser
│   ├── yolov8n.pt                     # Pre-trained YOLOv8 Nano PyTorch weights (6.5 MB)
│   ├── requirements.txt               # Vision dependencies (ultralytics, opencv-python)
│   └── README.md                      # Task 3 vision architecture & quickstart guide
│
├── .gitignore                         # Global exclusion rules for venv, cache, and IDE files
├── LICENSE                            # MIT License
└── README.md                          # Root engineering showcase hub (This document)
```

---

## 🚀 Engineering Principles & Design Choices

1. **Zero Hallucination in Customer Support (Task 2):** Rather than using generative cloud LLMs for simple static E-Commerce policies (`30-day returns`, `standard shipping rates`), Task 2 implements exact high-dimensional cosine similarity matching over a decoupled JSON file. This guarantees 100% policy compliance, zero cloud inference costs, and instantaneous local execution.
2. **Persistent Tracking Memory across Occlusions (Task 3):** Standard frame-by-frame object detection flickers ID numbers as bounding boxes intersect. By integrating memory-aware ByteTrack/BoT-SORT object tracking (`persist=True`), Task 3 preserves permanent identity assignments across live webcam feeds.
3. **Native Browser Acceleration without Heavy Bundlers (Task 1):** By leveraging browser-native `SpeechRecognition` and `SpeechSynthesis` APIs directly inside clean ES6 modules, the language translation tool eliminates the need for multi-megabyte frontend client bundles, ensuring ultra-fast loading over mobile connections.

---

## 💻 Quickstart & Verification

Navigate into any task subdirectory and follow its dedicated README for isolated execution. For automated continuous integration verification on **Task 2**:

```bash
cd CodeAlpha_FAQ_Chatbot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=. pytest -v tests/test_faq_bot.py
```

---

## 📄 License & Author
This repository is licensed under the **MIT License**.  
Developed and engineered by **Hafsat Abdulhamid** during the **CodeAlpha Artificial Intelligence Internship**.
