import React, { useState } from 'react';
import MessageList from './MessageList';
import UserInput from './UserInput';

const ChatWindow = () => {
  const [messages, setMessages] = useState([]);

  const handleSend = (text) => {
    if (!text.trim()) return;

    const userMessage = { sender: 'user', text };
    setMessages(prev => [...prev, userMessage]);

    // Mock AI response (replace this with LLM API call)
    const aiResponse = { sender: 'ai', text: `You said: ${text}` };
    setTimeout(() => {
      setMessages(prev => [...prev, aiResponse]);
    }, 500);
  };

  return (
    <div className="chat-window">
      <MessageList messages={messages} />
      <UserInput onSend={handleSend} />
    </div>
  );
};

export default ChatWindow;
