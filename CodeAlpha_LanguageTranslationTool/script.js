const sourceText = document.getElementById("source-text");
const targetText = document.getElementById("target-text");
const sourceLang = document.getElementById("source-lang");
const targetLang = document.getElementById("target-lang");
const translateBtn = document.getElementById("translate-btn");
const copyBtn = document.getElementById("copy-btn");
const speakBtn = document.getElementById("speak-btn");
const micBtn = document.getElementById("mic-btn");

async function translateText() {
    let text = sourceText.value.trim();
    let translateFrom = sourceLang.value;
    let translateTo = targetLang.value;

    if (!text) return; 

    targetText.placeholder = "Translating...";
    
    let apiUrl = `https://api.mymemory.translated.net/get?q=${encodeURI(text)}&langpair=${translateFrom}|${translateTo}`;

    try {
        const response = await fetch(apiUrl);
        const data = await response.json();
        
        targetText.value = data.responseData.translatedText;
    } catch (error) {
        targetText.value = "An error occurred. Please try again.";
        console.error("Translation Error:", error);
    }
}

translateBtn.addEventListener("click", translateText);

sourceText.addEventListener("keyup", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
        translateText();
    }
});

copyBtn.addEventListener("click", () => {
    if (targetText.value) {
        navigator.clipboard.writeText(targetText.value);
        
        const originalIcon = copyBtn.innerHTML;
        copyBtn.innerHTML = '<i class="fa-solid fa-check"></i>';
        setTimeout(() => {
            copyBtn.innerHTML = originalIcon;
        }, 1500);
    }
});

speakBtn.addEventListener("click", () => {
    if (targetText.value) {
        const utterance = new SpeechSynthesisUtterance(targetText.value);
        utterance.lang = targetLang.value; 
        speechSynthesis.speak(utterance);
    }
});

micBtn.addEventListener("click", () => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    
    if (SpeechRecognition) {
        const recognition = new SpeechRecognition();
        recognition.lang = sourceLang.value; 
        
        recognition.onstart = () => {
            sourceText.placeholder = "Listening... Speak now.";
            micBtn.style.color = "#ff7eb3"; 
        };

        recognition.onspeechend = () => {
            recognition.stop();
            micBtn.style.color = "#fff";
        };

        recognition.onresult = (result) => {
            sourceText.value = result.results[0][0].transcript;
            translateText();
        };

        recognition.start();
    } else {
        alert("Sorry, your browser doesn't support Voice Input. Try Google Chrome.");
    }
});