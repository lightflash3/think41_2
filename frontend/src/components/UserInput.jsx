import React from 'react';
import { useChat } from '../context/ChatContext';

export default function UserInput({ onSend }) {
  const { state, dispatch } = useChat();

  const handleChange = (e) => {
    dispatch({ type: 'SET_INPUT', payload: e.target.value });
  };

  const handleSend = () => {
    if (state.userInput.trim()) {
      onSend(state.userInput);
      dispatch({ type: 'CLEAR_INPUT' });
    }
  };

  return (
    <div className="flex gap-2 p-4">
      <input
        type="text"
        value={state.userInput}
        onChange={handleChange}
        placeholder="Type your message..."
        className="flex-1 px-4 py-2 border rounded-xl"
      />
      <button
        onClick={handleSend}
        className="bg-blue-500 text-white px-4 py-2 rounded-xl"
      >
        Send
      </button>
    </div>
  );
}