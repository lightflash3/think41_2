import React from 'react';
import MessageList from './MessageList';
import UserInput from './UserInput';
import { useChat } from '../context/ChatContext';

export default function ChatWindow() {
  const { dispatch } = useChat();

  const sendMessage = async (text) => {
    dispatch({ type: 'SET_LOADING', payload: true });
    dispatch({ type: 'ADD_MESSAGE', payload: { role: 'user', text } });

    try {
      const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text }),
      });
      const data = await response.json();
      dispatch({ type: 'ADD_MESSAGE', payload: { role: 'ai', text: data.reply } });
    } catch (error) {
      dispatch({ type: 'ADD_MESSAGE', payload: { role: 'ai', text: 'Error communicating with AI.' } });
    }

    dispatch({ type: 'SET_LOADING', payload: false });
  };

  return (
    <div className="flex flex-col h-screen">
      <MessageList />
      <UserInput onSend={sendMessage} />
    </div>
  );
}