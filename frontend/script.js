const chatMessages = document.getElementById('chatMessages');
const userInput = document.getElementById('userInput');

const API_URL = 'http://localhost:5000/chat';

userInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') sendMessage();
});

async function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    addMessage(message, 'user');
    userInput.value = '';

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: message })
        });
        const data = await response.json();
        addMessage(data.response, 'bot');
    } catch (error) {
        addMessage('Error connecting to server. Make sure backend is running.', 'bot');
    }
}

function addMessage(text, sender) {
    const div = document.createElement('div');
    div.className = `message ${sender}-message`;
    div.innerHTML = `
        <span class="avatar">${sender === 'bot' ? '🤖' : '👤'}</span>
        <div class="content">${text}</div>
    `;
    chatMessages.appendChild(div);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}
