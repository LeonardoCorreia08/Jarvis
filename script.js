const output = document.getElementById("output");
const startButton = document.getElementById("startButton");
let finalTranscript = "";

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();
recognition.lang = "pt-BR"; // Alterado para português
recognition.interimResults = true;

startButton.addEventListener('click', () => {
    finalTranscript = '';
    output.textContent = '';
    recognition.start();
    startButton.textContent = 'Escutando...';
});

recognition.addEventListener('result', (e) => {
    const transcript = Array.from(e.results).map(result =>
        result[0].transcript).join('');

    if (e.results[0].isFinal) {
        finalTranscript = transcript;
        output.textContent = finalTranscript;
    }
});

recognition.addEventListener('end', () => {
    startButton.textContent = 'Iniciar';
    recognition.start();
});

document.addEventListener('keydown', (e) => {
    if (e.key == 'Escape') {
        recognition.stop();
        startButton.textContent = 'Iniciar';
    }
});