// chatbot.js

const chatInput = document.querySelector('.chat-input textarea');
const sendChatBtn = document.querySelector('.chat-input span');
const chatbox = document.querySelector('.chatbox');

const createChatLi = (message, className) => {
  const chatLi = document.createElement('li');
  chatLi.classList.add('chat', className);
  let chatContent = className === 'outgoing' ? `<p>${message}</p>` : `<span class='material-symbols-outlined'>smart_toy</span><p>${message}</p>`;
  chatLi.innerHTML = chatContent;
  return chatLi;
};

const handleChat = () => {
  let userMessage = chatInput.value.trim();
  if (!userMessage) return;
  chatbox.appendChild(createChatLi(userMessage, 'outgoing'));
  chatInput.value = ''; // Clear the input field after sending the message

  // Send the user message to the backend
  fetch('/chatbot-response/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken') // Add CSRF token for security
    },
    body: JSON.stringify({ message: userMessage })
  })
  .then(response => response.json())
  .then(data => {
    chatbox.appendChild(createChatLi(data.response, 'incoming'));
  })
  .catch(error => {
    console.error('Error:', error);
    chatbox.appendChild(createChatLi('Sorry, something went wrong.', 'incoming'));
  });
};

// Function to get CSRF token from cookies
const getCookie = (name) => {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
};

sendChatBtn.addEventListener('click', handleChat);


// chatbot.js

// chatbot.js

document.addEventListener('DOMContentLoaded', function() {
    const chatbotToggler = document.querySelector('.chatbot-toggler');
    const chatbot = document.querySelector('.chatbot');
    const body = document.body;
  
    chatbotToggler.addEventListener('click', function() {
      body.classList.toggle('show-chatbot');
    });
  
    const closeBtn = document.querySelector('.chatbot header span');
    closeBtn.addEventListener('click', function() {
      body.classList.remove('show-chatbot');
    });
  });