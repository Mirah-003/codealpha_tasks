// 1. Select all the elements we need to interact with
const sourceText = document.getElementById("source-text");
const targetText = document.getElementById("target-text");
const sourceLang = document.getElementById("source-lang");
const targetLang = document.getElementById("target-lang");
const translateBtn = document.getElementById("translate-btn");
const copyBtn = document.getElementById("copy-btn");
const speakBtn = document.getElementById("speak-btn");
const micBtn = document.getElementById("mic-btn");

// 2. The Core Translation Function using MyMemory API
async function translateText() {
    let text = sourceText.value.trim();
    let translateFrom = sourceLang.value;
    let translateTo = targetLang.value;

    if (!text) return; // If input is empty, do nothing

    // Provide immediate visual feedback
    targetText.placeholder = "Translating...";
    
    // Construct the API URL
    // Format required by MyMemory: /get?q=TEXT&langpair=SOURCE|TARGET
    let apiUrl = `https://api.mymemory.translated.net/get?q=${encodeURI(text)}&langpair=${translateFrom}|${translateTo}`;

    try {
        // Fetch data from the API
        const response = await fetch(apiUrl);
        const data = await response.json();
        
        // Output the translated text
        targetText.value = data.responseData.translatedText;
    } catch (error) {
        targetText.value = "An error occurred. Please try again.";
        console.error("Translation Error:", error);
    }
}

// 3. Event Listeners (Triggers)
translateBtn.addEventListener("click", translateText);

// Optional: Translate automatically when pressing 'Enter'
sourceText.addEventListener("keyup", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
        translateText();
    }
});

// 4. Feature: Copy to Clipboard
copyBtn.addEventListener("click", () => {
    if (targetText.value) {
        // Use the modern Clipboard API
        navigator.clipboard.writeText(targetText.value);
        
        // Visual feedback
        const originalIcon = copyBtn.innerHTML;
        copyBtn.innerHTML = '<i class="fa-solid fa-check"></i>';
        setTimeout(() => {
            copyBtn.innerHTML = originalIcon;
        }, 1500);
    }
});

// 5. Feature: Text to Speech (Listen to Translation)
speakBtn.addEventListener("click", () => {
    if (targetText.value) {
        // Web Speech API built into browsers
        const utterance = new SpeechSynthesisUtterance(targetText.value);
        utterance.lang = targetLang.value; // Speak in the target language accent
        speechSynthesis.speak(utterance);
    }
});

// 6. Feature: Speech to Text (Voice Input)
micBtn.addEventListener("click", () => {
    // Check if the browser supports Speech Recognition
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    
    if (SpeechRecognition) {
        const recognition = new SpeechRecognition();
        recognition.lang = sourceLang.value; // Listen for the selected source language
        
        recognition.onstart = () => {
            sourceText.placeholder = "Listening... Speak now.";
            micBtn.style.color = "#ff7eb3"; // Change color to indicate listening
        };

        recognition.onspeechend = () => {
            recognition.stop();
            micBtn.style.color = "#fff"; // Revert color
        };

        recognition.onresult = (result) => {
            sourceText.value = result.results[0][0].transcript;
            // Automatically translate after speaking
            translateText();
        };

        recognition.start();
    } else {
        alert("Sorry, your browser doesn't support Voice Input. Try Google Chrome.");
    }
});