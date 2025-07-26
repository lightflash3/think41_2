import React from 'react';
import { useChat } from '../context/ChatContext';
import Message from './Message';

export default function MessageList() {
  const { state } = useChat();

  return (
    <div className="flex-1 overflow-y-auto p-4 bg-gray-100">
      {state.messages.map((msg, index) => (
        <Message key={index} role={msg.role} text={msg.text} />
      ))}
      {state.isLoading && <Message role="ai" text="Thinking..." />}
    </div>
  );
}