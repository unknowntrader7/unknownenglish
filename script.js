const inputText = document.getElementById('input-text');
const sendButton = document.getElementById('send-button');
const chatContainer = document.getElementById('chat-container');

sendButton.addEventListener('click', sendMessage);
inputText.addEventListener('keypress', (e) => {
  if (e.key === 'Enter') {
    sendMessage();
  }
});

function sendMessage() {
  const message = inputText.value.trim();
  if (!message) return;

  // 사용자의 질문을 화면에 표시
  displayMessage('user', message);
  inputText.value = '';

  // 서버에 질문 전송
  fetch('http://127.0.0.1:5000/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ message })
  })
    .then((response) => response.json())
    .then((data) => {
      // 서버에서 받은 답변을 화면에 표시
      displayMessage('bot', data.chatgpt_response);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

function displayMessage(sender, message) {
  const div = document.createElement('div');
  div.className = sender === 'user' ? 'user-message' : 'bot-message';
  div.textContent = message;
  chatContainer.appendChild(div);
  chatContainer.scrollTop = chatContainer.scrollHeight;
}
