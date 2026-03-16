// Pousada Maori Chatbot - Frontend JavaScript

const API_URL = window.location.origin + '/api/chat';
const messagesContainer = document.getElementById('messagesContainer');
const userInput = document.getElementById('userInput');
const sendButton = document.getElementById('sendButton');

// Inicialização
document.addEventListener('DOMContentLoaded', () => {
    userInput.focus();
});

// Envia mensagem do formulário
function sendMessage(event) {
    event.preventDefault();

    const message = userInput.value.trim();
    if (!message) return;

    // Limpa input
    userInput.value = '';

    // Adiciona mensagem do usuário
    addMessage(message, 'user');

    // Mostra indicador de digitação
    showTypingIndicator();

    // Envia para API
    fetch(API_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        // Remove indicador de digitação
        removeTypingIndicator();

        if (data.success) {
            // Adiciona resposta do bot
            addMessage(data.response, 'bot');
        } else {
            // Erro
            addMessage('❌ Desculpe, ocorreu um erro. Tente novamente.', 'bot');
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        removeTypingIndicator();
        addMessage('❌ Erro de conexão. Verifique se o servidor está rodando.', 'bot');
    });
}

// Envia pergunta rápida
function sendQuickQuestion(question) {
    userInput.value = question;
    sendMessage(new Event('submit'));
}

// Adiciona mensagem ao chat
function addMessage(text, sender) {
    // Remove mensagem de boas-vindas na primeira interação
    const welcomeMessage = document.querySelector('.welcome-message');
    if (welcomeMessage && sender === 'user') {
        welcomeMessage.remove();
    }

    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;

    const bubbleDiv = document.createElement('div');
    bubbleDiv.className = 'message-bubble';

    // Formata texto com markdown básico
    bubbleDiv.innerHTML = formatMessage(text);

    messageDiv.appendChild(bubbleDiv);
    messagesContainer.appendChild(messageDiv);

    // Scroll para última mensagem
    scrollToBottom();
}

// Formata mensagem com markdown básico
function formatMessage(text) {
    return text
        // Bold (**texto**)
        .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
        // Links
        .replace(/(https?:\/\/[^\s]+)/g, '<a href="$1" target="_blank">$1</a>')
        // Quebras de linha
        .replace(/\n/g, '<br>');
}

// Mostra indicador de digitação
function showTypingIndicator() {
    const typingDiv = document.createElement('div');
    typingDiv.className = 'message bot';
    typingDiv.id = 'typing-indicator';

    const typingBubble = document.createElement('div');
    typingBubble.className = 'typing-indicator';
    typingBubble.innerHTML = `
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
    `;

    typingDiv.appendChild(typingBubble);
    messagesContainer.appendChild(typingDiv);

    scrollToBottom();
}

// Remove indicador de digitação
function removeTypingIndicator() {
    const typingIndicator = document.getElementById('typing-indicator');
    if (typingIndicator) {
        typingIndicator.remove();
    }
}

// Scroll suave para o final
function scrollToBottom() {
    setTimeout(() => {
        messagesContainer.scrollTo({
            top: messagesContainer.scrollHeight,
            behavior: 'smooth'
        });
    }, 100);
}

// Permite enviar com Enter
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage(e);
    }
});
