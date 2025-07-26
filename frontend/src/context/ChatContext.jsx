// ChatContext.jsx
import React, { createContext, useContext, useState } from "react";

const ChatContext = createContext();

export const ChatProvider = ({ children }) => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [conversationHistory, setConversationHistory] = useState([]); // For Milestone 8

  const addMessage = (message) => {
    setMessages((prev) => [...prev, message]);
  };

  const clearInput = () => setInput("");

  const loadConversation = (sessionId) => {
    const session = conversationHistory.find((s) => s.id === sessionId);
    if (session) setMessages(session.messages);
  };

  const saveConversation = (session) => {
    setConversationHistory((prev) => [...prev, session]);
  };

  return (
    <ChatContext.Provider
      value={{
        messages,
        input,
        setInput,
        addMessage,
        clearInput,
        isLoading,
        setIsLoading,
        conversationHistory,
        loadConversation,
        saveConversation,
      }}
    >
      {children}
    </ChatContext.Provider>
  );
};

export const useChat = () => useContext(ChatContext);
