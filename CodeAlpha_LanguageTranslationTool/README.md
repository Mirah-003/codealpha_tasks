# 🌍 Smart Language Translation & Voice dictated Tool (`CodeAlpha Task 1`)

[![Web Speech API](https://img.shields.io/badge/Web_Speech_API-Voice_I%2FO-ff7eb3?style=for-the-badge&logo=googlechrome&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)
[![MyMemory API](https://img.shields.io/badge/REST_API-MyMemory_Translation-2575fc?style=for-the-badge)](https://mymemory.translated.net/doc/spec.php)
[![Glassmorphism UI](https://img.shields.io/badge/UI%2FUX-Glassmorphism_CSS3-6a11cb?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)

> **CodeAlpha Applied AI & NLP Internship Showcase**  
> A real-time, multilingual translation web application integrating **Speech-to-Text (`SpeechRecognition`)** and **Text-to-Speech (`SpeechSynthesis`)** browser APIs with RESTful neural machine translation over a sleek Glassmorphism interface.

---

## 💡 The Engineering Problem & Solution

Traditional web translation tools often require manual typing, constant page reloads, or heavy client-side language model downloads that freeze browser threads.

**Task 1 (`CodeAlpha_LanguageTranslationTool`)** delivers an asynchronous, low-overhead voice and text translation pipeline built entirely with **Vanilla ES6 JavaScript** and HTML5/CSS3. By orchestrating native browser **Web Speech APIs** alongside the asynchronous **MyMemory Translation REST API (`fetch`)**, the application provides real-time voice capture, accurate multilingual translation across 7 major world languages, and native accent pronunciation without heavy external libraries or UI blocking.

---

## 🏗️ Technical Features & Architecture

* **Speech-to-Text Pipeline (`micBtn.addEventListener`):** Instantiates `window.webkitSpeechRecognition` to transcribe spoken audio streams directly into source input buffers with real-time visual feedback (`"Listening... Speak now."`).
* **Asynchronous Translation Engine (`translateText`):** Executes URI-encoded REST queries against `https://api.mymemory.translated.net/get` with dynamic language pair routing (`translateFrom|translateTo`) and robust error catch boundaries.
* **Text-to-Speech Acoustic Playback (`speakBtn.addEventListener`):** Leverages `SpeechSynthesisUtterance` to synthesize natural speech output matching the selected target language code (`en`, `es`, `fr`, `de`, `it`, `ar`, `hi`).
* **Glassmorphism & Micro-Interactions:** Engineered with CSS `backdrop-filter: blur(15px)`, animated background gradients, and 1-click clipboard copying (`navigator.clipboard.writeText`) with temporary confirmation icons.

---

## 🛠️ Tech Stack & Structure

```
CodeAlpha_LanguageTranslationTool/
├── index.html     # Accessible semantic HTML5 layout with dual translation boxes
├── style.css      # Responsive Glassmorphism tokens, gradients, and media queries
└── script.js      # Stateless ES6 DOM manipulation, REST fetch, and Web Speech API handlers
```

---

## 🚀 Local Quickstart

1. Clone or navigate into the task directory:
   ```bash
   cd CodeAlpha_LanguageTranslationTool
   ```
2. Open `index.html` directly inside your web browser (or launch via VS Code **Live Server** extension):
   ```bash
   # On macOS:
   open index.html
   # On Linux:
   xdg-open index.html
   ```
3. **Voice Input Tip:** Ensure you allow microphone access in Google Chrome or Microsoft Edge when clicking the microphone (`🎤`) button.