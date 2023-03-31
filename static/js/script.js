document.addEventListener("DOMContentLoaded", function () {
  const gptForm = document.getElementById("gpt-form");
  const messageList = document.getElementById("message-list");

  gptForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const userInput = document.getElementById("user-input");
    const userMessage = userInput.value;
    userInput.value = "";

    addMessage("user", userMessage);

    addMessage("bot", "답변 생성 중...");

    const response = await fetch("/", {
      method: "POST",
      body: new FormData(e.target),
    });
    const data = await response.json();
    const botMessage = data.response;

    updateLastBotMessage(botMessage);
  });

  function addMessage(sender, text) {
    const messageItem = document.createElement("li");
    messageItem.classList.add("message", sender);
    messageItem.innerText = text;
    messageList.appendChild(messageItem);
    messageList.scrollTop = messageList.scrollHeight;
  }

  function updateLastBotMessage(text) {
    const lastBotMessage = messageList.querySelector(".bot:last-child");
    lastBotMessage.innerText = text;
    messageList.scrollTop = messageList.scrollHeight;
  }
});
