let token = localStorage.getItem('token');
const authSection = document.getElementById('auth-section');
const chatSection = document.getElementById('chat-section');
const loginForm = document.getElementById('login-form');
const chatForm = document.getElementById('chat-form');
const chatMessages = document.getElementById('chat-messages');
const typingIndicator = document.getElementById('typing-indicator');

// Verificar si ya hay token
if (token) {
    // Verificar si el token es válido
    fetch('/chat/test', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({test: 'data'})
    }).then(response => {
        if (response.ok) {
            showChatSection();
            loadHistory();
        } else {
            // Token inválido, limpiar
            localStorage.removeItem('token');
            token = null;
            showAuthSection();
        }
    }).catch(() => {
        localStorage.removeItem('token');
        token = null;
        showAuthSection();
    });
} else {
    showAuthSection();
}

// Login
loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('/auth/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();
        
        if (response.ok) {
            token = data.access_token;
            localStorage.setItem('token', token);
            showChatSection();
            loadHistory();
        } else {
            alert(data.error || 'Error al iniciar sesión');
        }
    } catch (error) {
        alert('Error de conexión');
    }
});

// Registro
document.getElementById('register-btn').addEventListener('click', async () => {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    if (!email || !password) {
        alert('Por favor completa todos los campos');
        return;
    }

    try {
        const response = await fetch('/auth/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();
        
        if (response.ok) {
            alert('Usuario registrado exitosamente. Ahora puedes iniciar sesión.');
        } else {
            alert(data.error || 'Error al registrar usuario');
        }
    } catch (error) {
        alert('Error de conexión');
    }
});

// Enviar mensaje
chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const messageInput = document.getElementById('message-input');
    const content = messageInput.value.trim();

    if (!content) return;

    // Mostrar mensaje del usuario
    addMessage(content, 'user');
    messageInput.value = '';
    
    // Mostrar indicador de escritura
    typingIndicator.style.display = 'block';
    scrollToBottom();

    try {
        console.log('Enviando mensaje:', content);
        console.log('Token:', token ? 'Presente' : 'Ausente');
        
        const response = await fetch('/chat/send', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ content })
        });

        console.log('Response status:', response.status);
        const data = await response.json();
        console.log('Response data:', data);
        
        if (response.ok) {
            const responseText = data.response || 'Sin respuesta';
            console.log('Respuesta de Gemini:', responseText);
            addMessage(responseText, 'assistant');
        } else {
            const errorMsg = data.error || data.errors || `Error ${response.status}`;
            console.log('Error del servidor:', errorMsg);
            addMessage(`Error: ${errorMsg}`, 'assistant');
        }
    } catch (error) {
        console.error('Error de conexión:', error);
        addMessage(`Error de conexión: ${error.message}`, 'assistant');
    } finally {
        typingIndicator.style.display = 'none';
        scrollToBottom();
    }
});

// Logout
document.getElementById('logout-btn').addEventListener('click', () => {
    localStorage.removeItem('token');
    token = null;
    chatMessages.innerHTML = '';
    showAuthSection();
});

function showAuthSection() {
    authSection.style.display = 'block';
    chatSection.style.display = 'none';
}

function showChatSection() {
    authSection.style.display = 'none';
    chatSection.style.display = 'flex';
}

function addMessage(content, role) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${role}-message`;
    messageDiv.textContent = content;
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

async function loadHistory() {
    try {
        const response = await fetch('/chat/history', {
            headers: { 'Authorization': `Bearer ${token}` }
        });

        const data = await response.json();
        
        if (response.ok) {
            chatMessages.innerHTML = '';
            data.history.forEach(msg => {
                addMessage(msg.content, msg.role);
            });
        }
    } catch (error) {
        console.error('Error loading history:', error);
    }
}